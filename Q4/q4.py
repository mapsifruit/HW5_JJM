import csv

def main() :
    
    f = open("q4.csv")
    data = csv.reader(f)

    header = next(data)

    line_use = [0,0,0,0]
    least_use = [0,0,0,0]
    busiest_name = ["","","",""]
    least_name = ["","","",""]
    for row in data :
        if row[1] == '1호선' :
            temp_use = float(row[4]) + float(row[5])
            if temp_use > line_use[0] :
                line_use[0] = temp_use
                busiest_name[0]= row[3]

            if least_use[0] == 0 :
                least_use[0] = temp_use
                least_name[0] = row[3]
            elif temp_use < least_use[0] :
                least_use[0] = temp_use
                least_name[0] = row[3]
                
        if row[1] == '2호선' :
            temp_use = float(row[4]) + float(row[5])
            if temp_use > line_use[1] :
                line_use[1] = temp_use
                busiest_name[1] = row[3]

            if least_use[1] == 0 :
                least_use[1] = temp_use
                least_name[1] = row[3]
            elif temp_use < least_use[1] :
                least_use[1] = temp_use
                least_name[1] = row[3]
                
        if row[1] == '3호선' :
            temp_use = float(row[4]) + float(row[5])
            if temp_use > line_use[2] :
                line_use[2] = temp_use
                busiest_name[2] = row[3]

            if least_use[2] == 0 :
                least_use[2] = temp_use
                least_name[2] = row[3]
            elif temp_use < least_use[2] :
                least_use[2] = temp_use
                least_name[2] = row[3]
                
        if row[1] == '4호선' :
            temp_use = float(row[4]) + float(row[5])
            if temp_use > line_use[3] :
                line_use[3] = temp_use
                busiest_name[3] = row[3]

            if least_use[3] == 0 :
                least_use[3] = temp_use
                least_name[3] = row[3]
            elif temp_use < least_use[3] :
                least_use[3] = temp_use
                least_name[3] = row[3]
        
    
    print("*** Subway Report for Seoul on March 2023 ***\n")
    print("Line 1\n")
    print("Busiest Station : ",busiest_name[0],"({0:.0f})".format(line_use[0]))
    print("Least used Station : ",least_name[0],"({0:.0f})".format(least_use[0],"\n"))

    print("Line 2\n")
    print("Busiest Station : ",busiest_name[1],"({0:.0f})".format(line_use[1]))
    print("Least used Station : ",least_name[1],"({0:.0f})".format(least_use[1]),"\n")

    print("Line 3\n")
    print("Busiest Station : ",busiest_name[2],"({0:.0f})".format(line_use[2]))
    print("Least used Station : ",least_name[2],"({0:.0f})".format(least_use[2]),"\n")

    print("Line 4\n")
    print("Busiest Station : ",busiest_name[3],"({0:.0f})".format(line_use[3]))
    print("Least used Station : ",least_name[3],"({0:.0f})".format(least_use[3]),"\n")
  
    f.close()

if __name__ == "__main__" :
    main()
