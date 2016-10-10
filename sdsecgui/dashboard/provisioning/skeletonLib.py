#!/usr/bin/python
# -*- coding: utf-8 -*- from credentials import get_keystone_creds
import uuid
from pprint import pprint

# struct -> dict, array -> list

class ControllerEngine:
	def getToken(self,tenant_name, domain_name, user_name, password):
		token_id = '2dc5d35fc791487ebdd32ec38e2edeed'
		result = {'error':{'message':'The request you have made requires authentication','code':401, 'title':'Unauthorized'}}
		result = {'success':{'message':'The token issued','code':200, 'token':token_id}}
		return result

	'''
	def checkToken(self, token):
		result = {'error':{'message':'Something wrong','code':500, 'title':'Function error'}}
		result = {'error':{'message':'The request you have made requires authentication','code':401, 'title':'Unauthorized'}}
		return result 
	'''

	
	def createMap(self, map_data):
		return
	def showMap(self, map_data):
		return
	
	
	def createService(self, token, tenant_name, user_name, service_template_list, map_info=None):
		result = []
		# TODO: 1) CHECK USER & TOKEN (from cookie)
		#glance_endpoint = keystone.service_catalog.url_for(service_type='image')
		#glance = glclient.Client(glance_endpoint, token=keystone.auth_token)     =>    checkToken()
		#images_iter = glance.images.list()  <- If unauthorized, return error message
		
		# TODO: 2) CHECK PARAMETERS
		
		# TODO: 3) MAKE TEMPLATE
		# createTemplate()
		
		# TODO: 4) CALL OPENSTACk LIB
		# createService(tenant_name, user_name, mdc_id, stack_name, hot_path)
		
		# TODO: 5) STORE TEH RETURN VALUES TO DATABASE
		
		# TODO: 6) RETRUN VALUES
		
        # 토큰이 유효하지 않으면 아래와 같은 에러 메시지
        #result = {'error':{'message':'The request you have made requires authentication','code':401, 'title':'Unauthorized'}}
        
		result = [{'region_id':'region-0001','name':'template-0001','service_id':'', 'status':'CREATE_COMPLETE'}]
		return result


	def modifyService(self, token, tenant_name, user_name, service_id, service_template_list):
		result = []	
		result = [{'region_id':'region-0001','name':'template-0001','status':'UPDATE_IN_PROGRESS'}]
		return result


	def deleteService(self, token, tenant_name, user_name, service_id):
		result = []	
		result = [{'region_id':'region-0001','name':'template-0001','status':'DELETE_COMPLETE'}]
		return result	

		
	def showService(self, token, tenant_name, user_name, service_id):	
		service_detail = {}
		service_detail['region_id'] = 'region-0001'
		service_detail['name'] = 'template-0001'
		service_detail['status'] = 'CREATE_COMPLETE'
		
		service_detail['vm_list'] = []
		vm = {}
		vm['vm_name'] = 'test-vm-01'
		vm['vm_id'] = '0553b367-25d5-4285-a343-34b0a2bdda37'		# VM UUID
		vm['vnic_list'] = []
		vnic = {}
		vnic['name'] = 'test-vnic-01'
		vnic['mac'] = 'test-vnic-01'
		vnic['private_ip'] = '192.168.10.99'
		vnic['floating_ip'] = '10.121.17.8'
		vm['vnic_list'].append(vnic)
		vm['status'] = 'Active'
		service_detail['vm_list'].append(vm)
		
		service_detail['volume_list'] = []
		volume = {}
		volume['volume_name'] = 'test-volume-01'
		volume['volume_id'] = ''
		volume['attachment'] = {}
		attachment={}
		attachment['vm_name'] = 'test-vm-01'
		attachment['device'] = ''
		volume['attachment'] = attachment
		volume['status'] = ''
		service_detail['volume_list'].append(volume)
		
		service_detail['network_list'] = []
		network = {}
		network['network_name'] = 'test-net-01'
		network['network_id'] = ''
		network['subnet_id'] = ''
		network['status'] = ''
		service_detail['network_list'].append(network)
		
		service_detail['vrouter_list'] = []
		vrouter = {}
		vrouter['vrouter_name'] = 'test-vrouter-01'
		vrouter['vrouter_id'] = ''
		vrouter['status'] = ''
		service_detail['vrouter_list'].append(vrouter)
		
		service_detail['loadbalancer_list'] = []
		loadbalancer = {}
		loadbalancer['lb_name'] = 'test-lb-01'
		loadbalancer['lb_pool_id'] = ''
		loadbalancer['vip'] = {}
		vip = {}
		vip['vip_id'] = ''
		vip['private_vip'] = ''
		vip['public_vip'] = ''
		loadbalancer['vip'] = vip
		loadbalancer['member_id'] = []
		loadbalancer['monitor_id'] = []
		loadbalancer['status'] = ''
		service_detail['loadbalancer_list'].append(loadbalancer)
		
		service_detail['firewall_list'] = []
		firewall = {}
		firewall['fw_name'] = 'test-fw-01'
		firewall['fw_id'] = ''
		firewall['fw_rule_id'] = []
		firewall['status'] = ''
		service_detail['firewall_list'].append(firewall)
		
		service_detail['vpn_list'] = []
		vpn = {}
		vpn['vpn_name'] = 'test-vpn-01'
		vpn['vpn_id'] = ''
		vpn['status'] = ''
		service_detail['vpn_list'].append(vpn)
		return service_detail

		
	def createSampleServiceTemplate(self):
		service_template = {}
		service_template['region_id'] = 'region-0001'
		service_template['name'] = 'template-0001'
		service_template['description'] = 'test template'
		service_template['vm_template_list'] = []
		
		vm_template = {}
		vm_template['server_name'] ='test-vm-01'
		vm_template['flavor'] = 'm1.tiny'
		vm_template['image'] = 'cirros'
		vm_template['vnic_list'] = []
		
		vnic = {}
		vnic['name'] = 'test-vnic-01'
		vnic['tenant_net'] = ''
		vnic['public_ip'] = False
		vm_template['vnic_list'].append(vnic)
		vm_template['volume_list'] = []
		
		volume = {}
		volume['name'] = 'test-volume-01'
		volume['type'] = 'lvm'
		volume['size'] = 1
		volume['image'] = ''
		volume['snapshot'] = ''
		
		vm_template['volume_list'].append(volume)
		vm_template['admin_pass'] = '1111'
		vm_template['key_name'] = 'my_key'

		service_template['vm_template_list'].append(vm_template)
		service_template['network_list'] = []
		
		network = {}
		network['name'] = 'test-net-01'
		network['cidr'] = '192.168.10.0/24'
		network['gateway_ip'] = '192.168.10.1'
		network['alloc_pools_list'] = []
		
		alloc_pools = {}
		alloc_pools['start'] = ''
		alloc_pools['end'] = ''
		
		network['ip_version'] = 4
		network['dns_list'] = []
		network['enable_dhcp'] = True
		
		service_template['network_list'].append(network)
		service_template['vrouter'] = {}
		
		vrouter = {}
		vrouter['name'] = 'test-vrouter-01'
		vrouter['external_net'] = 'public'
		vrouter['tenant_net_list'] = []
		
		service_template['vrouter'] = vrouter
		service_template['loadbalancer_list'] = []
		
		loadbalancer = {}
		loadbalancer['name'] = 'test-lb-01'
		loadbalancer['description'] = ''
		loadbalancer['pool_member_list'] = []
		
		pool_member = {}
		pool_member['name'] = 'test-pool-01'
		pool_member['protocol_port'] = ''
		pool_member['weight'] = 1
		
		loadbalancer['pool_member_list'].append(pool_member)
		loadbalancer['tenant_net'] = ''
		loadbalancer['public_vip'] = False
		loadbalancer['lb_method'] = ''
		loadbalancer['protocol'] = ''
		loadbalancer['port'] = 80
		loadbalancer['connection_limit'] = 100
		loadbalancer['persistence'] = ''
		loadbalancer['cookie_name'] = ''
		loadbalancer['monitors_list'] = []
		
		monitors = {}
		monitors['name'] = 'test-monitor-01'
		monitors['type'] = 'HTTP'
		monitors['delay'] = 60
		monitors['timeout'] = 600
		monitors['max_retries'] = 6
		monitors['http_method'] = ''
		monitors['url_path'] = ''
		monitors['expected_codes_list'] = []
		
		service_template['loadbalancer_list'].append(loadbalancer)
		service_template['firewall'] = {}
		
		firewall = {}
		firewall['name'] = 'test-fw-01'
		firewall['description'] = ''
		firewall['fw_rule_list'] = []
		
		fw_rule = {}
		fw_rule['name'] = 'test-fw-rule-01'
		fw_rule['description'] = ''
		fw_rule['protocol'] = 'TCP'
		fw_rule['src_ip'] = '192.168.0.99'
		fw_rule['dst_ip'] = ''
		fw_rule['src_port'] = ''
		fw_rule['dst_port'] = ''
		fw_rule['action'] = 'ALLOW'
		fw_rule['enabled'] = True
		
		service_template['firewall'] = firewall
		service_template['vpn_list'] = []
		
		vpn = {}
		vpn['name'] = 'test-vpn-01'
		vpn['description'] = ''
		vpn['tenant_net'] = ''
		vpn['peer_region_id'] = ''
		vpn['peer_tenant_net'] = ''
		vpn['mtu'] = 1500
		vpn['psk'] = ''
		service_template['vpn_list'].append(vpn)
		return service_template

		
	def suspendService(self, token, tenant_name, user_name, service_id, region_id=None):
		result = []	
		result = [{'region_id':'region-0001','name':'template-0001','status':'SUSPEND_COMPLETE'}]
		return result

		
	def resumeService(self, token, tenant_name, user_name, service_id, region_id=None):
		result = []	
		result = [{'region_id':'region-0001','name':'template-0001','status':'RESUME_COMPLETE'}]
		return result
		
		
	def suspendResource(self, token, tenant_name, user_name, service_id, region_id, resource_id, resource_type):
		# RESOURCE_TYPE : VM, NETWORK, PORT, ROUTER, VOLUME, LB, FW, VPN
		result = []	
		result = [{'status':'SUSPENDED'}]
		return result	
			
		
	def resumeResource(self, token, tenant_name, user_name, service_id, region_id, resource_id, resource_type):
		result = []	
		result = [{'status':'ACTIVE'}]
		return result	
		

	def showResource(self, token, tenant_name, user_name, service_id, region_id, resource_id, resource_type):
		result = []	
		result = [{'status':'ACTIVE'}]
		return result
		


		
c1 = ControllerEngine()
		
#sample_uuid = uuid.uuid1()	# Generate uuid
sample_uuid = '25d87c92-6b40-11e6-9961-0800277992df'
sample_service_template_list = []
sample_service_template = c1.createSampleServiceTemplate()
sample_service_template_list.append(sample_service_template)



print c1.getToken('demo', 'demo', 'admin', 'supersecret')
print
print c1.createService('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid, sample_service_template_list)
print
print c1.modifyService('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid, sample_service_template_list)
print
print c1.deleteService('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid)
print
print c1.suspendService('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid)
print
print c1.resumeService('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid)	
print
pprint (c1.showService('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid))
print
print c1.suspendResource('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid, 'region-0001', '0553b367-25d5-4285-a343-34b0a2bdda37', 'VM')
print
print c1.resumeResource('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid, 'region-0001', '0553b367-25d5-4285-a343-34b0a2bdda37', 'VM')	
print
print c1.showResource('demo', '2dc5d35fc791487ebdd32ec38e2edeed', 'admin', sample_uuid, 'region-0001', '0553b367-25d5-4285-a343-34b0a2bdda37', 'VM')




