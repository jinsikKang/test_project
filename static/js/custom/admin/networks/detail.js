var network;

function getSummary(){
    var dataTable = new DataTable({
        "selector" : "#summary",
        "columns" : {
            "name" : "이름",
            "id" : "ID",
            "project_id" : "프로젝트 ID",
            "status" : "Status",
            "admin_state_up" : "관리자 상태",
            "shared" : "공유",
            "router" : "외부 네트워크",
            "mtu" : "MTU",
            "provider" : {
                "name" : "공급자 네트워크",
                "dataName" : {
                    "network_type" : "네트워크 타입",
                    "physical_network" : "물리적인 네트워크",
                    "segmentation_id" : "구분 ID"
                }
            }
        },
        "vertical" : true,
        "data" : network
    });
    dataTable.showDataTable();
}

function getSubnet(){
    var dataTable = new DataTable({
        "selector" : "#subnet",
        "columns" : {
            "name" : "이름:link",
            "cidr" : "CIDR",
            "ip_version" : "IP 버전",
            "gateway_ip" : "게이트웨이 IP",
            "revision_number" : "사용된 IP",
            "allocation_pools" : "남는 IP"
        },
        "data" : network.subnets
    });
    dataTable.showDataTable();
    dataTable.setLink("networks/subnets");
}

function getPort(){
    var dataTable = new DataTable({
        "selector" : "#port",
        "columns" : {
            "id" : "이름:link",
            "fixed_ips" : "Fixed IP",
            "device_id" : "장치 연결됨",
            "status" : "Status",
            "admin_state_up" : "관리자 상태"
        },
        "data" : network.ports
    });
    dataTable.showDataTable();
    dataTable.setLink("networks/ports");
}

function getNetworkAjax(id, csrf_token){
    $.ajax({
        type:"POST",
        url : '',
        data : { id:id, csrfmiddlewaretoken: csrf_token },
        success:function(data){
            network = data.data;
            $(".header_title_d01").html(network.name);
            getSummary();
            getSubnet();
            getPort();
        }
    });
}