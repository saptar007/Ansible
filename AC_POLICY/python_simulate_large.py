for i in range (0,10):
  print ("    - name: Create an FQDN network for Cisco DevNet
        ftd_configuration:
          operation: upsertNetworkObject
          data:
            name: CiscoDevNetNetwork"i
            "subType: FQDN
            value: developer"i".cisco.com
            type: networkobject
            dnsResolution: IPV4_AND_IPV6

      - name: Create an access rule allowing trafic from Cisco DevNet"i
        "ftd_configuration:
          operation: upsertAccessRule
          data:
            name: AllowCiscoTraffic"i
            "type: accessrule
            sourceNetworks:
              - '{{ networkobject_ciscodevnetnetwork"i" }}'
            ruleAction: PERMIT
            eventLogAction: LOG_BOTH
          path_params:
            parentId: default")
