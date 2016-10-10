var service;
function getServiceAjax(csrf_token){
    $.ajax({
        type:"POST",
        url : '',
        data : { csrfmiddlewaretoken: csrf_token },
        success:function(data){
            service = data.data;
            getService();
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