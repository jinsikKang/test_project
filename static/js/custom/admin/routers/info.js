
function getRouterAjax(id, csrf_token){
    $.ajax({
        type:"POST",
        url : '',
        data : { id : id, csrfmiddlewaretoken: csrf_token },
        success:function(data){
            $(".header_title_d01").html(data.router.name); // header 셋팅
            for( key in data.router ){    // 데이터 넣기
                var resultHtml = "";
                if (key == "enable_gateway_info") {
                    continue;
                } else {
                    resultHtml = data.router[key];
                }
                if( resultHtml == "" ){
                    resultHtml = "None"
                }
                $("#"+key).html(resultHtml);
            }
            for ( subKey in data.router.enable_gateway_info ) {
                var resultHtml = "";
                if ( subKey == "enable_snat" ) {
                    resultHtml = "<ul><li>" + data.router.enable_gateway_info[key] + "</li></ul>";
                } else if ( subKey == "external_fixed_ips" ) {
                    var external_fixed_ips = data.router.external_fixed_ips;
                    resultHtml += "<ul>";
                    for( var i = 0; i < external_fixed_ips.length; i++ ){
                        resultHtml += "<li>서브넷 ID " + external_fixed_ips[i]["subnet_id"] + "</li><li>IP주소 " + external_fixed_ips[i]["ip_address"] + "</li>";
                    }
                    resultHtml += "</ul>";
                } else {
                    resultHtml = data.router.enable_gateway_info[key];
                }
                $("#"+subKey).html(resultHtml);
            }
        }
    });
}