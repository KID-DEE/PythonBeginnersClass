with open("DaliyasPdf.pdf", "x") as pdf:
    pdf.write("Daliya is a student of nigerian Navy Military school\n")
    pdf.write("He is a very good student\n")
    pdf.close()


with open("DaliyasPdf.pdf", "r") as pdf:
    print(pdf.read())

