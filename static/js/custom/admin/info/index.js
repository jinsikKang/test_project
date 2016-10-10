var service;
function getServiceAjax(csrf_token){
    $.ajax({
        type:"POST",
        url : '',
        data : { csrfmiddlewaretoken: csrf_token },
        success:function(data){
            service = data.serviceList;
            getService();
            getNovaServiceList(csrf_token);
            getNetworkAgent(csrf_token);
        }
    });
}

function getService() {
    var dataTable = new DataTable({
        "selector" : "#service",
        "columns" : {
            "Name" : "이름",
            "Type" : "서비스",
        },
        "data" : service
    });
    dataTable.showDataTable();
}

function getNovaServiceList(csrf_token){
    $.ajax({
        type:"POST",
        url : 'nova_service',
        data : { csrfmiddlewaretoken: csrf_token },
        success:function(data){
            var dataTable = new DataTable({
                "selector" : "#nova_service",
                "columns" : {
                    "binary" : "이름",
                    "host" : "호스트",
                    "zone" : "Zone",
                    "status" : "Status",
                    "state" : "State",
                    "updated_at" : "마지막 업데이트 됨",
                },
                "data" : data.novaServiceList
            });
            dataTable.showDataTable();
        }
    });
}

function getNetworkAgent(csrf_token) {
    $.ajax({
        type:"POST",
        url : 'agent',
        data : { csrfmiddlewaretoken: csrf_token },
        success:function(data){
            var dataTable = new DataTable({
                "selector" : "#agent",
                "columns" : {
                    "agent_type" : "유형",
                    "binary" : "이름",
                    "host" : "호스트",
                    "alive" : "Status",
                    "admin_state_up" : "State",
                    "Type" : "마지막 업데이트 됨",
                },
                "data" : data.agentList
            });
            dataTable.showDataTable();
        }
    });
}


$(function(){
//탭 클릭시 이벤트들

    var tabList = ["service", "nova_service", "storage", "agent"];

    $("." + tabList[0]).on("click", function(){tabClick(0, tabList)});

    $("#" + tabList[1]).hide();
    $("." + tabList[1]).on("click", function(){tabClick(1, tabList)});

    $("#" + tabList[2]).hide();
    $("." + tabList[2]).on("click", function(){tabClick(2, tabList)});

    $("#" + tabList[3]).hide();
    $("." + tabList[3]).on("click", function(){tabClick(3, tabList)});
});