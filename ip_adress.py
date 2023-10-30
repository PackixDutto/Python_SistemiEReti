def completa8bit(strbin);
    b = strbin[2:]
    l = len(b)
    return "0"*(8-l)+b

def main(): 

    ip = "10.172.14.4"
    group = ip.split('.')
    print (group)
    group = [int(group) for group in group]
    print (group)
    group_bin = [bin(group) for group in group]
    print (group_bin)
    print (completa8bit(group_bin[2]))
    group_strbin = [completa8bit(strbin) for strbin in group_bin]
    print(group_strbin)
    print(":)".join(group_strbin))

if __name__ == "__main__":
    main()