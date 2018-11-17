total_price = int(input("合計金額を教えてね(円): "))
number_of_people = int(input("人数を教えてね(人): "))
try:
    print(f"1人あたり:{total_price//number_of_people}円 端数:{total_price%number_of_people}円")

except ZeroDivisionError:
    print("0で割ってはいけませねん")

finally:
    pass
