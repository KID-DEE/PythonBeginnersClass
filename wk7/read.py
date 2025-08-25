# """
# Implementing Read from file 
# Daliya Daniel
# 4th august 2025
# Python Bootcamp
# """
import pymupdf

pymupdf=open("Endline.pdf","r")
data=pymupdf.read()
print(data)
pymupdf.close()

# with open("myfiles.txt","r") as f:
#     print("\n With open")
#     data2=f.read()
#     print(data2)
# print(f"This is the data from the file: {data2}")


# #"""Read manipulation """

# input_file='myfile.txt'
# output_file='output.txt'

# words=[]
# with open(input_file,"r") as file:
#     for line in file:
#         # split line into words and add to list
#         words_in_line=line.strip().split()
#         words.extend(words_in_line)

# # Write words to output file
# # with open(output_file,"w") as file:
# #     for word in words:
# #         file.write(word + "\n")

# # print(f"Read {len[words]} words and saved to {output_file}")
