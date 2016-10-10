var service;
function getServiceAjax(csrf_token){
    $.ajax({
        type:"POST",
        url : '',
        data : { csrfmiddlewaretoken: csrf_token },
        success:function(data){
            service = data.serviceList;
            getService();
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
    $("#nova").hide();
    $("#storage").hide();
    $("#agent").hide();

    var tabList = ["service", "nova", "storage", "agent"];

    $(".service").on("click", function(){tabClick(0, tabList)});
    $(".nova").on("click", function(){tabClick(1, tabList)});
    $(".storage").on("click", function(){tabClick(2, tabList)});
    $(".agent").on("click", function(){tabClick(3, tabList)});
});