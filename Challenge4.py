#   Note that this script expects HTTP port 80 on the APIC, which is off by default.
# 	To enable HTTP in the APIC, navigate to FABRIC, FABRIC POLICIES Pod Policies     Policies   Management Acces    default  then enable HTTP
import requests
import json

def get_cookies(apic):
	username = 'admin'
	password = 'ciscoapic'
	url = apic + '/api/aaaLogin.json'
	auth = dict(aaaUser=dict(attributes=dict(name=username, pwd=password)))
	authenticate = requests.post(url, data=json.dumps(auth), verify=False)
	return authenticate.cookies

def add_tenant(apic,cookies):
#	jsondata = {"fvTenant":{"attributes":{"dn":"uni/tn-Procurement","name":"Procurement","rn":"tn-Procurement","status":"created"},"children":[]}}
    jsondata = {"fvTenant":{"attributes":{"descr":"","dn":"uni/tn-acme","name":"acme","ownerKey":"","ownerTag":""},"children":[{"vzBrCP":{"attributes":{"descr":"","name":"Web","ownerKey":"","ownerTag":"","prio":"unspecified","scope":"context"},"children":[{"vzSubj":{"attributes":{"consMatchT":"AtleastOne","descr":"","name":"Web","prio":"unspecified","provMatchT":"AtleastOne","revFltPorts":"yes"},"children":[{"vzRsSubjFiltAtt":{"attributes":{"tnVzFilterName":"Web"}}}]}}]}},{"drawCont":{"attributes":{},"children":[{"drawInst":{"attributes":{"info":"{'epg-Payroll-undefined':{'x':541,'y':342},'ctrct_provider-Web-undefined':{'x':441,'y':5},'epg-Bills-undefined':{'x':279,'y':214}}","oDn":"uni/tn-acme/ap-Accounting"}}}]}},{"fvCtx":{"attributes":{"descr":"","knwMcastAct":"permit","name":"VRF_A","ownerKey":"","ownerTag":"","pcEnfPref":"enforced"},"children":[{"fvRsCtxToExtRouteTagPol":{"attributes":{"tnL3extRouteTagPolName":""}}},{"fvRsBgpCtxPol":{"attributes":{"tnBgpCtxPolName":""}}},{"vzAny":{"attributes":{"descr":"","matchT":"AtleastOne","name":""}}},{"fvRsOspfCtxPol":{"attributes":{"tnOspfCtxPolName":""}}},{"fvRsCtxToEpRet":{"attributes":{"tnFvEpRetPolName":""}}}]}},{"fvBD":{"attributes":{"arpFlood":"no","descr":"","epMoveDetectMode":"","limitIpLearnToSubnets":"no","llAddr":"::","mac":"AA:AA:AA:AA:AA:AA","multiDstPktAct":"bd-flood","name":"BRIDGE_DOMAIN_TEST1","ownerKey":"","ownerTag":"","unicastRoute":"yes","unkMacUcastAct":"proxy","unkMcastAct":"flood"},"children":[{"fvRsBDToNdP":{"attributes":{"tnNdIfPolName":""}}},{"fvRsCtx":{"attributes":{"tnFvCtxName":"VRF_A"}}},{"fvRsIgmpsn":{"attributes":{"tnIgmpSnoopPolName":""}}},{"fvSubnet":{"attributes":{"ctrl":"","descr":"","ip":"10.1.2.1/24","name":"","preferred":"no","scope":"private"}}},{"fvRsBdToEpRet":{"attributes":{"resolveAct":"resolve","tnFvEpRetPolName":""}}}]}},{"fvBD":{"attributes":{"arpFlood":"no","descr":"","epMoveDetectMode":"","limitIpLearnToSubnets":"no","llAddr":"::","mac":"AA:AA:AA:AA:AA:AA","multiDstPktAct":"bd-flood","name":"BRIDGE_DOMAIN_TEST","ownerKey":"","ownerTag":"","unicastRoute":"yes","unkMacUcastAct":"proxy","unkMcastAct":"flood"},"children":[{"fvRsBDToNdP":{"attributes":{"tnNdIfPolName":""}}},{"fvRsCtx":{"attributes":{"tnFvCtxName":"VRF_A"}}},{"fvRsIgmpsn":{"attributes":{"tnIgmpSnoopPolName":""}}},{"fvSubnet":{"attributes":{"ctrl":"","descr":"","ip":"10.1.1.1/14","name":"","preferred":"no","scope":"private"}}},{"fvRsBdToEpRet":{"attributes":{"resolveAct":"resolve","tnFvEpRetPolName":""}}}]}},{"vzFilter":{"attributes":{"descr":"","name":"Web","ownerKey":"","ownerTag":""},"children":[{"vzEntry":{"attributes":{"applyToFrag":"no","arpOpc":"unspecified","dFromPort":"http","dToPort":"http","descr":"","etherT":"ip","icmpv4T":"unspecified","icmpv6T":"unspecified","name":"Web","prot":"tcp","sFromPort":"https","sToPort":"65535","stateful":"no","tcpRules":""}}}]}},{"fvRsTenantMonPol":{"attributes":{"tnMonEPGPolName":""}}},{"fvAp":{"attributes":{"descr":"","name":"Accounting","ownerKey":"","ownerTag":"","prio":"unspecified"},"children":[{"fvAEPg":{"attributes":{"descr":"","matchT":"AtleastOne","name":"Bills","prio":"unspecified"},"children":[{"fvRsCustQosPol":{"attributes":{"tnQosCustomPolName":""}}},{"fvRsBd":{"attributes":{"tnFvBDName":"BRIDGE_DOMAIN_TEST"}}},{"fvCrtrn":{"attributes":{"descr":"","name":"default","ownerKey":"","ownerTag":""}}},{"fvRsProv":{"attributes":{"matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"Web"}}}]}},{"fvAEPg":{"attributes":{"descr":"","matchT":"AtleastOne","name":"Payroll","prio":"unspecified"},"children":[{"fvRsCons":{"attributes":{"prio":"unspecified","tnVzBrCPName":"Web"}}},{"fvRsCustQosPol":{"attributes":{"tnQosCustomPolName":""}}},{"fvRsBd":{"attributes":{"tnFvBDName":"BRIDGE_DOMAIN_TEST"}}},{"fvCrtrn":{"attributes":{"descr":"","name":"default","ownerKey":"","ownerTag":""}}}]}}]}}]}}
    result = requests.post('{0}://{1}/api/node/mo/uni/tn-Procurement.json'.format(protocol,host), cookies=cookies, data=json.dumps(jsondata), verify=False)
    print result.status_code
    print result.text

def get_tenants(apic,cookies):
	uri = '/api/class/fvTenant.json'
	url = apic + uri
	req = requests.get(url, cookies=cookies, verify=False)
	response = req.text
	return response

if __name__ == "__main__":
	protocol = 'http'
	host = '192.168.10.1'
	apic = '{0}://{1}'.format(protocol, host)
	cookies = get_cookies(apic)
	add_tenant(apic,cookies)
	rsp = get_tenants(apic,cookies)

rsp_dict = json.loads(rsp)
tenants = rsp_dict['imdata']

for tenant in tenants:
	print tenant['fvTenant']['attributes']['name']
