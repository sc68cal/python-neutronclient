import sys

import mox

from neutronclient.neutron.v2_0.qos import qos
from neutronclient.tests.unit import test_cli20

class CLITestV20QoSJson(test_cli20.CLITestV20Base):

    def setUp(self):
        super(CLITestV20QoSJson, self).setUp(plurals={'qoses': 'qos'})


    def test_create_qos_with_params(self):
        resource = 'qos'
        cmd = qos.CreateQoS(test_cli20.MyApp(sys.stdout), None)

        my_id = 'my-id'

        qos_type = 'dscp'
        description = 'test QoS'
        tenant_id = 'my-tenant'
        policies = '{"dscp": "10"}'

        args = ['--type', qos_type,
                '--policies', policies,
                '--description', description,
                '--tenant-id', tenant_id
                ]

        position_names = ['type', 'description', 'policies', 'tenant-id']
        position_values = [qos_type, description, policies, tenant_id]

        self._test_create_resource(resource, cmd, qos_type, my_id, args,
                position_names, position_values)

