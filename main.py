# sum of deadline
# sum of all amount
# sum of all lenght of nodeArray

from Claster import *
from reader_xlsx import *

types = str()
Orders_read = read_order()
Machines = read_machine()
Orders = Claster.qck_sort(Orders_read)
Mnodes = CreateKnots(Machines)
Mnodes = Claster.sort_orders(Orders, Mnodes)
Finished = MNode("finish", "")
# f = open('text.txt', 'w')
# for x in Mnodes[0].Order_arr:
#      f.write(str(x.amount)+'\n')
# f = open('text1.txt', 'w')
# for x in Mnodes[1].Order_arr:
#      f.write(str(x.amount)+'\n')
# for i in range(len(Mnodes)):
#      print(len(Mnodes[i].Order_arr))
# #
# # print(Mnodes[0].type_)
# # for x in Mnodes:
# #     print(x.type_)
# # for x in range(len(Mnodes[1].Machines)):
# #     print(Mnodes[1].Machines[x].id_)
for i in range(10):
    for x in Mnodes:
        x.simulate()
