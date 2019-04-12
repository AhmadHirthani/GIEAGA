import csv
# import matplotlib.pyplot as plt
# from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
# import json as simplejson
#
gdp_list={}
# interval=0
with open('BL2013_MF1599_v2.2.csv', 'r') as edu_csv_file:
    edu_csv_reader = csv.DictReader(edu_csv_file)
    for line in edu_csv_reader:
        for c in range(1965, 2011):
            if line['country'] == "Austria":
                if ('' + str(c) + '') == line['year']:

                    #print(str(c))

                    gdp_list['' + str(c) + '']= float(line['lhc']) / float(line['lh'])*100

print(gdp_list)
#     names = []
#     values1 = []
#     values2 = []
#
#     i = 1965
#     while i < 2011:
#         names.append(i)
#         values1.append(gdp_list[i][0])
#         values2.append(gdp_list[i][1])
#         i += 5
#
#
#
# f = open('output.csv', 'a+')
# simplejson.dump(names , f)
# f.write('\n')
# simplejson.dump(values1, f)
# f.write('\n')
# simplejson.dump(values2, f)
# f.close()
#
# fig = plt.figure(1)
#
# host = HostAxes(fig, [0.1, 0.1, 0.8, 0.8])
# par1 = ParasiteAxes(host, sharex=host)
# host.parasites.append(par1)
# host.set_ylabel("Density")
# host.set_xlabel("Distance")
#
# host.axis["right"].set_visible(True)
# par1.axis["right"].set_visible(True)
# par1.set_ylabel("Temperature")
#
# par1.axis["right"].major_ticklabels.set_visible(True)
# par1.axis["right"].label.set_visible(True)
#
#
#
# fig.add_axes(host)
#
# host.set_xlim(1975,2010)
# host.set_ylim(0, 100)
#
# host.set_xlabel("Years Intervals")
# host.set_ylabel("Income")
# par1.set_ylabel("Pass Rate")
#
#
# p1, = host.plot(names, values1, label="Income")
# p2, = par1.plot(names,values2 , label="Pass Rate")
#
# par1.set_ylim(56, 65)
#
# host.legend()
#
# host.axis["left"].label.set_color(p1.get_color())
# par1.axis["right"].label.set_color(p2.get_color())
# plt.show()