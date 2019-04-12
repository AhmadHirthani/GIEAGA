import csv
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
import json as simplejson

gdp_list={}
edu_list={}
interval=0
with open('GDP by Country.csv','r') as gdp_csv_file:
    gdp_csv_reader=csv.DictReader(gdp_csv_file)
    for line in gdp_csv_reader:
        if line['ï»¿"Country Name"']=="Austria":
            for count in range(1961, 1966):
                endofinterval = 1965
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval]=interval / 200000000000
            interval = 0


            for count in range(1966, 1971):
                endofinterval = 1970
                interval = interval + float(line['' + str(count) + ''])
                gdp_list[endofinterval]=interval / 200000000000
            interval = 0
            print(gdp_list)

            for count in range(1971, 1976):
                endofinterval=1975
                interval=interval+float(line['' + str(count)+''])
                gdp_list[endofinterval]=interval / 200000000000
            interval=0

            for count in range(1976, 1981):
                endofinterval=1980
                interval=interval+float(line['' + str(count)+''])
                gdp_list[endofinterval]=interval / 200000000000
            interval = 0
            for count in range(1981, 1986):
                endofinterval=1985
                interval=interval+float(line['' + str(count)+''])
                gdp_list[endofinterval]=interval / 200000000000
            interval = 0
            for count in range(1986, 1991):
                endofinterval=1990
                interval=interval+float(line['' + str(count)+''])
                gdp_list[endofinterval]=interval / 200000000000
            interval = 0
            for count in range(1991, 1996):
                endofinterval=1995
                interval=interval+float(line['' + str(count)+''])
                gdp_list[endofinterval]=interval / 200000000000
            interval = 0
            for count in range(1996, 2001):
                endofinterval=2000
                interval=interval+float(line['' + str(count)+''])
                gdp_list[endofinterval]=interval / 200000000000
            interval = 0
            for count in range(2001, 2006):
                endofinterval=2005
                interval=interval+float(line['' + str(count)+''])
                gdp_list[endofinterval]=interval / 200000000000
            interval = 0
            for count in range(2006, 2011):
                endofinterval=2010
                interval=interval+float(line['' + str(count)+''])
                gdp_list[endofinterval]=interval / 200000000000

    print(gdp_list)

with open('BL2013_MF1599_v2.2.csv', 'r') as edu_csv_file:
    edu_csv_reader = csv.DictReader(edu_csv_file)
    for line in edu_csv_reader:
        for c in range(1965, 2011):
            if line['country'] == "Austria" and '' + str(c) + '' == line['year']:
                edu_list[c]= float(line['lhc']) / float(line['lh'])*100

    # gdp_list[1975][0]=100
    print(edu_list)
    names = []
    values1 = []
    values2 = []

    i = 1965
    while i < 2011:
        names.append(i)
        values1.append(gdp_list[i][0])
        values2.append(gdp_list[i][1])
        i += 5



f = open('output.csv', 'a+')
simplejson.dump(names , f)
f.write('\n')
simplejson.dump(values1, f)
f.write('\n')
simplejson.dump(values2, f)
f.close()

fig = plt.figure(1)

host = HostAxes(fig, [0.1, 0.1, 0.8, 0.8])
par1 = ParasiteAxes(host, sharex=host)
host.parasites.append(par1)
host.set_ylabel("Density")
host.set_xlabel("Distance")

host.axis["right"].set_visible(True)
par1.axis["right"].set_visible(True)
par1.set_ylabel("Temperature")

par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)



fig.add_axes(host)

host.set_xlim(1975,2010)
host.set_ylim(0, 100)

host.set_xlabel("Years Intervals")
host.set_ylabel("Income")
par1.set_ylabel("Pass Rate")


p1, = host.plot(names, values1, label="Income")
p2, = par1.plot(names,values2 , label="Pass Rate")

par1.set_ylim(56, 65)

host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())

plt.show()