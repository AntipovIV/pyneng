# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf = ospf_route.split()
protocol = ospf[0]
prefix = ospf[1]
ad = ospf[2]
hop = ospf[4]
update = ospf[5]
interface = ospf[6]

protocol = protocol.replace('O', 'OSPF')
ad = ad.strip('[]')
hop = hop.rstrip(',')
update = update.rstrip(',')

ospf_route = """
Protocol:             {0:18}
Prefix:               {1:18}
AD/Metric:            {2:18}
Next-Hop:             {3:18}
Last update:          {4:18}
Outbound Interface:   {5:18}
"""
print(ospf_route.format(protocol, prefix, ad, hop, update, interface))
