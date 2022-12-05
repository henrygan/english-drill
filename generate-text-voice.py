import argparse
import configparser

source_path = None
result_path = None
voice_common_path = None

config = configparser.ConfigParser()
config.read("./generate-text-voice.ini") 

source_path = config['DEFAULT']['source_path']
result_path = config['DEFAULT']['result_path']
voice_common_path = config['DEFAULT']['voice_common_path']

# input : index , english , chinese , segment
# ouput 1 : ** chinese , english  , segment

parser = argparse.ArgumentParser()
parser.add_argument("--source_path", help="source english file name")
parser.add_argument("--result_path", help="result org drill file name")
parser.add_argument("--voice_common_path", help="base path")
args = parser.parse_args()

if args.source_path:
    print("source path : %(path)s" % {"path" : args.source_path})
    source_path = args.source_path

if args.result_path:
    print("result path : %(path)s" % {"path" : args.result_path})
    result_path = args.result_path

if args.voice_common_path:
    print("voice common path : %(path)s" % {"path" : args.voice_common_path})
    voice_common_path = args.voice_common_path 

fread = open(source_path, "r")
fwrite = open(result_path, "w")

x_np = fread.readlines()

output_content = """
* 单句
"""
fwrite.write(output_content)

for line in x_np:
    print(line)
    _, index, segment, english, chinese, _ = line.split(sep="|")
    mp3_path = voice_common_path + index.strip()  + ".mp3"
    template = """
** %(chinese)s :drill:
    :PROPERTIES:
    :MP3:   %(mp3_path)s 
    :END:
    [%(english)s]
    [[play:%(mp3_path)s][听读]]
    """
    output_content = template % {"english": english, "chinese": chinese, "mp3_path": mp3_path}
    print(output_content)
    fwrite.write(output_content)
    
fread.close()
fwrite.close()
