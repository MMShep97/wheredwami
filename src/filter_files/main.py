import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please try again with the correct params...\npython <file.py> <desired file> <threshold between 0 and 1>\nExiting...")
        exit(1)
    if float(sys.argv[2]) > 1:
        print("Threshold between 0 and 1, please!\nExiting...")
        exit(1)

    ##################################################### 
    path = sys.argv[1]
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    #####################################################

    ####################### GET FILTERED LIST THAT PASS THE THRESHOLD ##############################
    router_count_dictionary = {}
    total_objects = 0
    # for each line in file
    for line in data:
        total_objects += 1
        # grab object 
        for router_name, signal_strength in line.items():
            if router_name in router_count_dictionary:
                router_count_dictionary[router_name]['count'] += 1
            else: 
                router_count_dictionary[router_name]= {'signal_strength': signal_strength, 'count': 1}


    threshold = float(sys.argv[2])
    filtered_routers = {}
    for router_name, values in router_count_dictionary.items():
        if ( values['count'] / total_objects) >= threshold:
            filtered_routers[router_name] = values['signal_strength']
    #####################################################
    filtered_data = []
    i = 0
    for line in data:
        temp_dict = {}
        for router_name, signal_strength in line.items():
            if router_name in filtered_routers.keys():
                temp_dict[router_name] = signal_strength
            
        filtered_data.append(dict(temp_dict))
        i += 1

    # print(*router_count_dictionary.items(), sep="\n")
    # print(total_objects)
    # print(*filtered_routers.items(), sep="\n")
    # print(*filtered_data, sep="\n")

    with open('output.txt', 'w') as fout:
        json.dump(filtered_data, fout)
    
    print("Outputting to file & EXITING!!!")
