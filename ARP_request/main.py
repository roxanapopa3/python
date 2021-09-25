#!/bin/env_python

import scapy.all as scapy
import argparse


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/ IP range")
    option = parser.parse_args()
    return option


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list


def print_result(results_list):
    print("IP\t\t\tMAC Address\n-----------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_options()
scan_result = scan(options.target)
print_result(scan_result)
