import csv

def main() :

    f = open("q2.csv", encoding='cp949')
    data = csv.reader(f)

    header = next(data)

    max_diff = 0
    max_date = ""
    min_diff = 100
    min_date = ""

    for row in data :
        if row[-2] == '' :
            continue
        else :
            temp = float(row[-1]) - float(row[-2])
            if max_diff < temp :
                max_diff = temp
                max_date = row[0]
            if min_diff > temp :
                min_diff = temp
                min_date = row[0]



    print("*** Annual Temperature Report for Seoul in 2022 ***\n")

    print("Day with the Largest Temperature Variation : ",max_date.strip(),"\n")
    print("Maximum Temperature Difference : {0:.1f} Celsius\n".format(max_diff))
    print("Day with the Smallest Temperature Variation : ",min_date.strip(),"\n")
    print("Minimum Temperature Difference : {0:.1f} Celsius\n".format(min_diff))

    f.close()


if __name__ == "__main__" :
    main()
