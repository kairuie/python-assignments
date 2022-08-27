import emoji

convert = input()
face = convert.replace(":)", emoji.emojize(":slightly_smiling_face:")).replace(":(", emoji.emojize(":slightly_frowning_face:"))

print(face)

