import numpy as np

input_file_path = "./source.org"
fread = open(input_file_path, "r")
tbl_data = [["book", "书本"],["giant", "巨人"],["pilot", "飞行员"]]
output_file_path = "./chinese_to_english.org"
fwrite = open(output_file_path, "w")

def output_english_to_chinese(english, chinese):
    # english_syllable = f.syllabify(english)
    # print(english_syllable)
    template = """* %(english)s :drill:
    :PROPERTIES:
    :VOICE:   %(english)s 
    :END:
    [%(chinese)s] 
    """
    print(template % {"english": english, "chinese": chinese})

def output_chinese_to_english(english, chinese):
    # english_syllable = f.syllabify(english)
    # print(english_syllable)
    template = """
* %(chinese)s :drill:
    :PROPERTIES:
    :DRILL_CARD_TYPE: hide2cloze
    :VOICE:   %(english)s 
    :END:
    %(english)s 

* %(chinese)s :drill:
   :PROPERTIES:
   :VOICE:   %(english)s 
   :END:
   [%(english)s]
    """
    output_content = template % {"english": english, "chinese": chinese}
    print(output_content)
    fwrite.write(output_content)

# x_np = np.array(tbl_data)
# x_np = np.fromfile(input_file_path, sep = "|", dtype=str)
# x_np = np.loadtxt(input_file_path, delimiter = "|", dtype=str)
x_np = fread.readlines()
print(x_np)

# for english, chinese in x_np:
for line in x_np:
    english,chinese = line.split()
    # output_english_to_chinese(english, chinese)
    output_chinese_to_english(english, chinese)

fread.close()
fwrite.close()
