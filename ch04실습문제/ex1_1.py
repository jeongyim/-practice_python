for i in range(1,13):
    with open("2022년"+str(i)+"월.txt","w",encoding="utf8") as sing_file:
        sing_file.write("-2022년 {}월 인기가요-".format(i))
        sing_file.write("\n인기가요 1위:")
        sing_file.write("\n인기가요 2위:")
        sing_file.write("\n이달의 신곡:")
for i in range(1,13):
    with open("2022년"+str(i)+"월.txt","r",encoding="uif8") as sing_file:
        print(sing_file.read())       
