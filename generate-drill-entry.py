# import numpy as np
import argparse
import eng_to_ipa as p

parser = argparse.ArgumentParser()
parser.add_argument("--source_path", help="source english file name", default="./source.org")
parser.add_argument("--result_path", help="result org drill file name")
parser.add_argument("--direction", help="english to chinese (ec) or chinse to english (ce) or both", default="ce")
args = parser.parse_args()

if args.source_path:
    print("source path : %(path)s" % {"path" : args.source_path})

if args.result_path:
    print("result path : %(path)s" % {"path" : args.result_path})

input_file_path = "./source.org"
fread = open(args.source_path, "r")
tbl_data = [["book", "书本"],["giant", "巨人"],["pilot", "飞行员"]]
output_file_path = "./chinese_to_english.org"
fwrite = open(args.result_path, "w")

def output_english_to_chinese(english, chinese, ipa):
    # english_syllable = f.syllabify(english)
    # print(english_syllable)
    template = """
* %(english)s :drill:
    :PROPERTIES:
    :VOICE:   %(english)s 
    :END:

    [%(chinese)s] 

** Pronounce
   %(ipa)s
    """
    output_content = template % {"english": english, "chinese": chinese, "ipa": ipa}
    print(output_content)
    fwrite.write(output_content)

def output_chinese_to_english(english, chinese, ipa):
    # english_syllable = f.syllabify(english)
    # print(english_syllable)
    template = """
* %(chinese)s :drill:
    :PROPERTIES:
    :DRILL_CARD_TYPE: hide2cloze
    :VOICE:   %(english)s 
    :END:

    %(ipa)s

    [%(english)s]

* %(chinese)s :drill:
   :PROPERTIES:
   :VOICE:   %(english)s 
   :END:
   [%(english)s]
** Pronounce
   %(ipa)s
    """
    output_content = template % {"english": english, "chinese": chinese, "ipa": ipa}
    print(output_content)
    fwrite.write(output_content)

# x_np = np.array(tbl_data)
# x_np = np.fromfile(input_file_path, sep = "|", dtype=str)
# x_np = np.loadtxt(input_file_path, delimiter = "|", dtype=str)
x_np = fread.readlines()
print(x_np)

# for english, chinese in x_np:
for line in x_np:
    words = line.split()
    chinese = words[-1]
    english = " ".join(words[0:-1])
    ipa = "/ " + p.convert(english) + " /"
    if args.direction == "ce":
        output_chinese_to_english(english, chinese, ipa)

    if args.direction == "ec":
        output_english_to_chinese(english, chinese, ipa)

    if args.direction == "both":
        output_chinese_to_english(english, chinese, ipa)
        output_english_to_chinese(english, chinese, ipa)

fread.close()
fwrite.close()
