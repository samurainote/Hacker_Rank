
import sys
import pandas as pd

def find_most_purchased_color(transactions_file_name, product_file_name):
    A = input().strip()
    B = input().strip()

    data = pd.read_csv(A)
    prod = pd.read_csv(B)
    merge = pd.merge(data, prod, on='product_id')

    # pivot = pd.pivot_table(merge, index='color', columns='purchased_quantity', values='purchased_quantity', margins=True)
    part = merge[["color", "purchased_quantity"]]
    grouped = part.groupby("color")

    answer = grouped.sum().idxmax()
    if type(answer) == str:
        sys.stdout.write(answer)
        sys.stdout.flush()
    else:
        sys.stdout.write(str(answer))
        sys.stdout.flush()
