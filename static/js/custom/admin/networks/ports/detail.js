function getPostAjax(id, csrf_token){
    $.ajax({
        type:"POST",
        url : '',
        data : { id : id, csrfmiddlewaretoken: csrf_token },
        success:function(data){
            $(".header_title_d01").html(data.port.name); // header 셋팅
            for( key in data.port ){    // 데이터 넣기
                var resultHtml = "";
                var tempList = data.port.fixed_ips.split("\n");
                var fixed_ips = [];
                for( i in tempList ){
                    var fixed_ip = JSON.parse(tempList[i]);
                    fixed_ips.push(fixed_ip);
                }
                if (key == "fixed_ips") {
                    for( var i = 0; i < fixed_ips.length; i++ ){
                        if( resultHtml != "" ){
                            resultHtml += "<br/>";
                        }
                        resultHtml += "IP주소 " + fixed_ips[i]["ip_address"] + " 서브넷 ID " + fixed_ips[i]["subnet_id"];
                    }
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