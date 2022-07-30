# with open('ALLpasses.txt') as f:
#     f_out = None
#     for line in f:
#         if line.startswith('\n\ntestingg\n\n'):      # we need a new output file
#             title = line.split(' ', 1)[1]
#             if f_out:
#                 f_out.close()
#             f_out = open(f'{title}.txt', 'w')
#         if f_out:
#             f_out.write(line)
#     if f_out:
#         f_out.close()
with open("ALLpasses.txt") as f:
    lines = f.readlines()

indices = [0]

for idx, line in enumerate(lines):
    if "testingg" in line:
        indices.append(idx) # idx number of line where -THE END- is occurred

chapter_counter = 2

while chapter_counter <= len(indices):
    with open(f"Chapter_{chapter_counter-1}.txt", "a") as w:
        lines_chapter = lines[indices[chapter_counter-2]+1:indices[chapter_counter-1]+1] # From -THE END- to -THE END-
        for line_chapter in lines_chapter:
            w.write(f"{line_chapter}")

    chapter_counter += 1
