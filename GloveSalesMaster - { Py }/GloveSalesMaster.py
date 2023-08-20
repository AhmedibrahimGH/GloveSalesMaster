def months():
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']
    sales = []
    for sale in month_list:
        sales.append(eval(input("Enter the sales for " + sale + ": ")))

    total = sum(sales)
    print("Total sales: {:.2f}".format(total))

    average = sum(sales) / len(sales)
    print("Average sales: {:.2f}".format(average))

    highest = month_list[sales.index(max(sales))]
    print("Highest sales:", highest)

    lowest = month_list[sales.index(min(sales))]
    print("Lowest sales:", lowest)


months()
