$(function(){
    $.ajax({
        type:"POST",
        url : '',
        data : { id:"{{ port_id }}", csrfmiddlewaretoken: "{{ csrf_token }}" },
        success:function(data){
            $(".header_title_d01").html(data.port.name); // header 셋팅
            for( key in data.port ){    // 데이터 넣기
                var resultHtml = "";
                resultHtml = data.subnet[key];
                if( resultHtml == "" ){
                    resultHtml = "None"
                }
                $("#"+key).html(resultHtml);
            }
        }
    });
});