



def filtrate_sort(l, num):
    return sorted(l, key=lambda x: x[3], reverse=True)[:num]