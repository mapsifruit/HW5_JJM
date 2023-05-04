import csv

def main() :

    f = open("q1.csv", encoding='cp949')
    data = csv.reader(f)

    header = next(data)

    sum_avg = 0
    sum_min = 0
    sum_max = 0
    count = 0

    for row in data :
        
        if '' in row :
            continue
        else :
            sum_min += float(row[-2])
            sum_avg += float(row[2])
            sum_max += float(row[-1])
            count += 1

    avg = sum_avg/count
    min_avg = sum_min / count
    max_avg = sum_max / count

    print("*** Annual Temperature Report for Seoul in 2022 ***\n")
    print("Average Temperature : {0:.2f} Celsius\n".format(avg))
    print("Average Minimum Temperature : {0:.2f} Celsius\n".format(min_avg))
    print("Average Maximum Temperature : {0:.2f} Celsius\n".format(max_avg))

    f.close()


if __name__ == "__main__" :
    main()
