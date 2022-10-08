
def get_cat_strings(input_string):
    tab_list = input_string.split("\t")

    try:
        name = tab_list[0]
        des  = tab_list[1]
        val  = tab_list[2]
        rarity = tab_list[3]
        weight = tab_list[4]
        category = tab_list[5]
        prop = tab_list[6]
        requirement = tab_list[7]

        return name, des, val, rarity, weight, category, prop, requirement

    except:
        return None, None, None, None, None, None, None, None









if __name__ == "__main__":
    input_file = open("raw_tresure_list.tsv", "r")
    output_file = open("output_treasure_list.txt", "w")

    output_line = ""

    item_count = 0


    for raw_line in input_file.readlines():
        name, des, val, rarity, weight, category, prop, requirement = get_cat_strings(raw_line)


        if name == None or name == "":
            continue


        item_count += 1

        output_line = ("\tTreasure(\"" + name + "\",\n" +
                       "\t         \"" + des + "\",\n" +
                       "\t         \"" + val + "\",\n" +
                       "\t         \"" + rarity + "\",\n" +
                       "\t         \"" + weight + "\",\n" +
                       "\t         \"" + category + "\",\n" +
                       "\t         \"" + prop + "\",\n" +
                       "\t         \"" + requirement + "\"),\n\n"
                       )

        # print(output_line)
        output_file.write(output_line)

    print("Item Count: " + str(item_count))


    # print(name)
    # print(des)
    # print(val)
    # print(rarity)
    # print(weight)
    # print(category)
    # print(property)
    # print(requirement)


