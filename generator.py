import hashlib
import os
import re

peace_path = "/Users/KateChristensen/Library/Application Support/Sid Meier's Civilization 5/MODS/GoT Playlist (v 1)/Music/Peace"
war_path = "/Users/KateChristensen/Library/Application Support/Sid Meier's Civilization 5/MODS/GoT Playlist (v 1)/Music/War"

os.listdir(path=peace_path)

full_file_path_list = ["Music/Peace/"+file for file in os.listdir(path=peace_path)]

war_file_path_list = ["Music/War/"+file for file in os.listdir(path=war_path)]

hashlib.md5(open("/Music/Peace/A_Lannister_Pays_their_debts.mp3 ",'rb').read()).hexdigest()

def file_as_bytes(file):
    with file:
        return file.read()

modinfo_file_gen = ['<File md5="{}" import="1">{}</File>'.format(hashlib.md5(file_as_bytes(open(fname, 'rb'))).hexdigest(),fname) for fname in war_file_path_list]

no_mp3_filelist = [re.sub('\.mp3', '', f) for f in os.listdir(path=peace_path)]

war_no_mp3_filelist = [re.sub('\.mp3', '', f) for f in os.listdir(path=war_path)]


num = 1
for fi in no_mp3_filelist:
    print("""
    <Row>
        <SoundID>SND_GOT_PEACE_{}</SoundID>
	    <Filename>{}</Filename>
	    <LoadType>DynamicResident</LoadType>
    </Row>
    """.format(num,fi))
    num += 1

num = 1
for fi in war_no_mp3_filelist:
    print("""
    <Row>
        <SoundID>SND_GOT_WAR_{}</SoundID>
	    <Filename>{}</Filename>
	    <LoadType>DynamicResident</LoadType>
    </Row>
    """.format(num,fi))
    num += 1