import pyeapi
import yaml

file = open('interfaces.yml', 'r')
pyeapi.load_config('eapi.conf')
interface_dict = yaml.safe_load(file)

for switch in interface_dict['devices']:
    connect = pyeapi.connect_to(switch)
    int_api = connect.api('ipinterfaces')
    for interface in interface_dict['devices'][switch]['interfaces']:
        ip = interface_dict['devices'][switch]['interfaces'][interface]['ip']
        mask = interface_dict['devices'][switch]['interfaces'][interface]['mask']
        mask = str(mask)
        ip_mask = ip+"/"+mask
        int_api.create(interface)
        int_api.set_address(interface,ip_mask)

