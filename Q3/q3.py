import csv

def main() :

    f = open("q3.csv")
    data = csv.reader(f)

    header = next(data)

    line_use = [0,0,0,0,0,0,0,0,0]

    for row in data :
        if row[1] == '1호선' :
            line_use[0] += float(row[4]) + float(row[5])
        if row[1] == '2호선' :
            line_use[1] += float(row[4]) + float(row[5])
        if row[1] == '3호선' :
            line_use[2] += float(row[4]) + float(row[5])
        if row[1] == '4호선' :
            line_use[3] += float(row[4]) + float(row[5])
        if row[1] == '5호선' :
            line_use[4] += float(row[4]) + float(row[5])
        if row[1] == '6호선' :
            line_use[5] += float(row[4]) + float(row[5])
        if row[1] == '7호선' :
            line_use[6] += float(row[4]) + float(row[5])
        if row[1] == '8호선' :
            line_use[7] += float(row[4]) + float(row[5])
        if row[1] == '9호선' :
            line_use[8] += float(row[4]) + float(row[5])
        

    first_busy = 0
    fb_line = 0
    second_busy = 0
    sb_line = 0
    first_least = line_use[0]
    fl_line = 1
    second_least = line_use[0]
    sl_line = 1

    for i in range(len(line_use)) :
        if line_use[i] > first_busy :
            first_busy = line_use[i]
            fb_line = i+1
        elif line_use[i] > second_busy :
            second_busy = line_use[i]
            sb_line = i+1
    for i in range(len(line_use)) :
        if line_use[i] < first_least :
            first_least = line_use[i]
            fl_line = i+1
        elif line_use[i] <second_least :
            second_least = line_use[i]
            sl_line = i+1

    print("*** Subway Report for Seoul on March 2023 ***\n")
    print("1st Busiest Line : Line {0:d} ({1:.0f}) ".format(fb_line,first_busy),"\n")
    print("2nd Busiest Line : Line {0:d} ({1:.0f}) ".format(sb_line,second_busy),"\n")
    print("1st Least used Line : Line {0:d} ({1:.0f}) ".format(fl_line,first_least),"\n")
    print("2nd Least used Line : Line {0:d} ({1:.0f}) ".format(sl_line,second_least),"\n")

    f.close()

if __name__ == "__main__" :
    main()
