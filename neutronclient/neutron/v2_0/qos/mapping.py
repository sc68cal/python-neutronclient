from neutronclient.neutron import v2_0 as neutronV20


class ListPortMapping(neutronV20.ListCommand):
    resource = 'ports'

    list_columns = ['id', 'qos']
