def common(set1,set2):
    return set(set1).intersection(set2)
set1=(input("Enter a list of numbers separated by space: ").split())
set2=(input("Enter a list of numbers separated by space: ").split())
print(common(set1,set2))