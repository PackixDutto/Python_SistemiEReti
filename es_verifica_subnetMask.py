import ipaddress

def main():
    ip_addresses = ["192.168.222.0/27", "192.168.100.0/24", "192.168.200.0/28", "192.168.50.0/22"]
    with open("mask.txt", "w") as file:
        for ip_address in ip_addresses:
            ip, subnetmask = ip_addresses.split("/")
            subnet_mask_int = int(subnet_mask)
            subnet_mask_bin = '1'*subnet_mask_int + '0'*(32-subnet_mask_int) # fai tanti 1 quanti la lungheza di subnet_mask_int
            subnet_mask_bin = [subnet_mask_bin[:8] + '.' + subnet_mask_bin[8:16] +  '.' + subnet_mask_bin[16:24] + subnet_mask_bin[24:]]
            file.write(f"{ip} - Subnet mask({subnet_mask}): {subnet_mask_bin}\n")
       

if _name_ == "_main_":
    main()