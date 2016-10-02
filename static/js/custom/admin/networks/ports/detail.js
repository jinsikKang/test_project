function getPostAjax(id, csrf_token){
    this.getListData = function(dataList){
        var tempList = dataList.split("\n");
        var resultList = [];
        for( i in tempList ){
            var data = JSON.parse(tempList[i]);
            resultList.push(data);
        }
        return resultList
    }
    $.ajax({
        type:"POST",
        url : '',
        data : { id : id, csrfmiddlewaretoken: csrf_token },
        success:function(data){
            $(".header_title_d01").html(data.port.name); // header 셋팅
            for( key in data.port ){    // 데이터 넣기
                var resultHtml = "";
                if (key == "fixed_ips") {
                    var fixed_ips = getListData(data.port.fixed_ips);
                    for( var i = 0; i < fixed_ips.length; i++ ){
                        if( resultHtml != "" ){
                            resultHtml += "<br/>";
                        }
                        resultHtml += "IP주소 " + fixed_ips[i]["ip_address"] + " 서브넷 ID " + fixed_ips[i]["subnet_id"];
                    }
                } else if (key.indexOf("binding") != -1){
                    if (key == "binding:vif_details") {
                        var vif_details = getListData(data.port["binding:vif_details"]);
                        resultHtml += "<ul>"
                        for( var i = 0; i < vif_details.length; i++ ){
                            resultHtml += "<li><b>port_filter</b> " + vif_details[i]["port_filter"] + "</li><li><b>ovs_hybrid_plug</b> " + vif_details[i]["ovs_hybrid_plug"] + "</li>";
                        }
                        resultHtml += "</ul>"
                    } else {
                        resultHtml = data.port[key];
                    }
                    key = key.replace("binding:","binding_");
                } else {
                    resultHtml = data.port[key];
                }
                if( resultHtml == "" ){
                    resultHtml = "None"
                }
                $("#"+key).html(resultHtml);
            }
        }
    });
}