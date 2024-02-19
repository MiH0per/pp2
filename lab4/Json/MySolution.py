import json

with open('sample.json') as file:
    data = json.load(file)

interfaces = data.get('imdata', [])

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in interfaces:
    attributes = interface.get('l1PhysIf', {}).get('attributes', {})
    dn = attributes.get('dn', '')
    start_index = dn.find("eth1/") + len("eth1/")
    substring = dn[start_index:dn.find("/", start_index)]

    description = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')

    
    print("{:<50} {:<20} {:<8} {:<6}".format(dn, description, speed, mtu))