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
            "name" : "이름",
            "type" : "서비스",
            }
        },
        "vertical" : true,
        "data" : service
    });
    dataTable.showDataTable();
}
}