function getRouterList(data){
    var dataTable = new DataTable({
        "selector" : "#routerList",
        "columns" : {
            "name" : "이름:link",
            "status" : "Status",
            "external_gateway_info.network_id" : "외부 네트워크",
            "admin_state_up" : "관리자 상태",
            "project_id" : "프로젝트",
        },
        "data" : data

    });
    dataTable.showDataTable();
    dataTable.setLink("routers");
}

function getRouterAjax(routerList, csrf_token){
    $.ajax({
        type:"POST",
        url : '',
        data : { "routerList" : JSON.stringify(routerList), csrfmiddlewaretoken : csrf_token },
        success:function(jsonData){
            var resultData = jsonData.data;
            getRouterList(resultData);
        }
    });
}