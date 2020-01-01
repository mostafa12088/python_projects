import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


excel_file1 = r"C:\\Users\\BME7ABT\\Desktop\\shift-data.xlsx"
excel_file2 = r"C:\\Users\\BME7ABT\\Desktop\\third-shift-data.xlsx"

df_first_shift = pd.read_excel(excel_file1, sheet_name="first")
df_second_shift = pd.read_excel(excel_file1, sheet_name="second")
df_third_shift = pd.read_excel(excel_file2)

# print(df_first_shift)
# print(df_first_shift["Product"])

df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])
print(df_all)  # to print all the data together

df_all.to_excel("Output.xlsx")  # to save the output as excel file

pivot = df_all.groupby(["Shift"]).mean()  #
shift_productivity = pivot.loc[
    :, "Production Run Time (Min)":"Products Produced (Units)"
]
print(shift_productivity)  # to find the most productive shift

shift_productivity.plot(kind="bar")
plt.show()

