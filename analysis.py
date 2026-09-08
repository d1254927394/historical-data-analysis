'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2026-09-08 21:29:36
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2026-09-08 22:12:25
FilePath: \historical data analysis\analysis.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("output.csv")

df["growth_rate"] = df["output"].pct_change() * 100

print(df)
df["growth_rate"] = (df["output"].pct_change() * 100).round(2)

df["year_gap"] = df["year"].diff()

df["annualized_growth"] = (
    ((df["output"] / df["output"].shift(1)) ** (1 / df["year_gap"]) - 1) * 100
).round(2)
print
plt.plot(df["year"], df["output"], marker="o")

plt.xlabel("Year")
plt.ylabel("Output")
plt.title("Industrial Output Trend")
plt.savefig("output_trend.png", dpi=300, bbox_inches="tight")
plt.show()
plt.bar(df["year"], df["annualized_growth"])

plt.xlabel("Year")
plt.ylabel("Annualized Growth (%)")
plt.title("Annualized Growth Rate")

plt.savefig("annualized_growth.png", dpi=300, bbox_inches="tight")
plt.show()
df.to_excel("analysis_result.xlsx", index=False)
# 自动生成摘要

start_year = df["year"].iloc[0]
end_year = df["year"].iloc[-1]

start_output = df["output"].iloc[0]
end_output = df["output"].iloc[-1]

total_growth = ((end_output / start_output) - 1) * 100

year_gap_total = end_year - start_year

overall_cagr = (
    (end_output / start_output) ** (1 / year_gap_total) - 1
) * 100

highest_growth_row = df.loc[df["annualized_growth"].idxmax()]
lowest_growth_row = df.loc[df["annualized_growth"].idxmin()]

summary = f"""
===== 分析摘要 =====

{int(start_year)}年至{int(end_year)}年，总产值由
{start_output:.1f}增长至{end_output:.1f}。

累计增长率为：{total_growth:.2f}%

期间年均复合增长率为：{overall_cagr:.2f}%

年均增长最快的记录为{int(highest_growth_row['year'])}年，
增长率为{highest_growth_row['annualized_growth']:.2f}%。

下降最明显的记录为{int(lowest_growth_row['year'])}年，
增长率为{lowest_growth_row['annualized_growth']:.2f}%。
"""

print(summary)
with open("analysis_summary.txt", "w", encoding="utf-8") as file:
    file.write(summary)
    print("分析摘要已保存到 analysis_summary.txt")