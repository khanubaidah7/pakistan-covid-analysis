import pandas as pd
df = pd.read_csv("C:/Users/Al Kareem Traders/OneDrive/Desktop/Data Science/Final Projects/PK COVID-19.csv")
# print(df.info()) # checking data set
# print(df.isnull().sum()) # checking null values
#                                                overall situation
total_cases = df["Cases"].sum()
total_deaths = df["Deaths"].sum()
total_recovered = df["Recovered"].sum()
# print(f"Total cases: {total_cases}, Total deaths: {total_deaths}, Total recovered: {total_recovered}")
recovery_rate = (total_recovered / total_cases)*100 
death_rate = (total_deaths/total_cases)*100
# print(f"Recovery rate:  {recovery_rate}")
# print(f"Death rate:  {death_rate}")

#                                          checking peak day and peak cases
df['Date'] = pd.to_datetime(df['Date'])
daily_cases = df.groupby("Date")["Cases"].sum()
# print(daily_cases.head(10))
peak_day = daily_cases.idxmax()
# print(peak_day)
peak_cases = daily_cases.max()
# print(f"maximum cases reported on the date {peak_day} and the numbers of cases is {peak_cases}")

#                                           checking province wise cases,deaths,recovered
province_wise_total_cases = df.groupby("Province").aggregate({
    'Cases':'sum',
    'Deaths':'sum',
    'Recovered':'sum'
}).reset_index()
# print(province_wise_total_cases)

#                                checking province wise recovery rate, deaths rate
province_wise_total_cases['Recovery_Rate'] = (
    province_wise_total_cases['Recovered'] / province_wise_total_cases['Cases']
) * 100
province_wise_total_cases['Recovery_Rate'] = province_wise_total_cases['Recovery_Rate'].round(2)
# print(province_wise_total_cases)
province_wise_total_cases["Death_rate"] = (province_wise_total_cases["Deaths"]/province_wise_total_cases['Cases'])*100
province_wise_total_cases["Death_rate"] = province_wise_total_cases["Death_rate"].round(2)
# print(province_wise_total_cases)
# province_wise_total_cases.to_csv("province_summary.csv",index=False)

#                                   checking city wise cases
city_wise_cases = df.groupby("City")["Cases"].sum().sort_values(ascending=False).reset_index()
# print(city_wise_cases)
# city_wise_cases.to_csv("city_wise_report.csv",index=False)

#                                       checking travel_history cases
travel_cases = df.groupby("Travel_history")["Cases"].sum().sort_values(ascending=False)
# travel_cases.to_csv("traveling_impact.csv",index=False)
# print(travel_cases)
travel_cases_rate = (travel_cases/travel_cases.sum())*100
# print(travel_cases_rate)

#                                       checking month wise cases
df["month"]  = df['Date'].dt.to_period('M')
# monthly_cases = df.groupby("month")["Cases"].sum().sort_values(ascending=False).reset_index()
# print(monthly_cases)
# monthly_cases.to_csv("monthly_cases.csv",index=False)