function DataTable (settings){
    this.selector = settings["selector"];
    this.columns = settings["columns"];
    if( settings["vertical"] ){
        this.vertical = settings["vertical"];
    }else{
        this.vertical = false;
    }
    if( settings["data"] ){
        this.data = settings["data"];
    }else{
        this.data = null;
    }

    this.showDataTable = function() {
        /* 컬럼과 데이터 형식 */
        var columnForm = "<th class='ind_th01 %K'>%C</th>\n"
        var dataForm = "<td class='ind_td01 %K'>%D</td>\n";
        var resultHtml = ""

        if( this.vertical ){ /* 데이터를 세로로 출력*/
            for( key in this.columns ){
                resultHtml += "<tr>\n";
                var columnHtml = "";
                var dataHtml = "";
                if ( this.columns[key] instanceof Object ) {
                    // 객체일때 여러줄로 출력
                    columnHtml = columnForm.replace("%C", this.columns[key].name).replace("%K", key);
                    var data = "";
                    for ( dataNameKey in this.columns[key].dataName ){
                        data += this.columns[key].dataName[dataNameKey] + " " + this.data[key][dataNameKey] + "<br/>";
                    }
                    dataHtml = dataForm.replace("%D", data).replace("%K", key);
                } else if ( this.data[key] instanceof Array ) {
                    // 배열일때 ul, li태그로 묶어 출력
                    columnHtml = columnForm.replace("%C", this.columns[key]).replace("%K", key);
                    var data = "<ul>";
                    for ( i in this.data[key]){
                        data += "<li>" + this.data[key][i] + "</li>";
                    }
                    data += "</ul>";
                    dataHtml = dataForm.replace("%D", data).replace("%K", key);
                } else {
                    var link = "";
                    if ( this.columns[key].indexOf(":link") != -1 ) {
                        /* class 에 link 를 포함 */
                        this.columns[key] = this.columns[key].replace(":link", "");
                        link = " link";
                    }

                    columnHtml = columnForm.replace("%C", this.columns[key]).replace("%K", key);
                    if( this.data[key] instanceof Object ){
                        for ( dataNameKey in this.data[key] ){
                            dataHtml = dataForm.replace("%D", this.data[key][dataNameKey]).replace("%K", key + link);
                        }
                    } else {
                        dataHtml = dataForm.replace("%D", this.data[key]).replace("%K", key + link);
                    }
                }
                var data = this.data[key];
                resultHtml += columnHtml;
                resultHtml += dataHtml;
                resultHtml += "</tr>\n";
            }
        }else{
            var columnHtml = "<tr>";
            for( key in this.columns ){
                columnHtml += "<th class='ind_th01 " + key + "'>" + this.columns[key] + "</th>\n";
            }
            columnHtml += "</tr>";

            var dataHtml = "";
            for( i in this.data ){
                dataHtml += "<tr>\n";
                for( key in this.columns ){
                    var link = "";
                    if ( this.columns[key].indexOf(":link") != -1 ) {
                        /* class 에 link 를 포함 */
                        link = " link";
                    }
                    if ( key.indexOf(".") != -1 ){
                        var mainKey = key.replace(/\.\w+/g, "");
                        var subKey = key.replace(/\w+(\..+)/g, "$1");
                        console.log(this.data[i]);
                        var jsonData = JSON.parse(this.data[i][mainKey]);
                        dataHtml += "<td class='ind_td01 " + key + link + "'>" + eval("jsonData" + subKey) + "</td>\n";
                    } else {
                        dataHtml += "<td class='ind_td01 " + key + link + "'>" + this.data[i][key] + "</td>\n";
                    }
                }
                dataHtml += "</tr>\n";
            }
            resultHtml = columnHtml + dataHtml;
            resultHtml = resultHtml.replace(":link", "");
        }
        $(this.selector + " table").html(resultHtml);
    };

    this.setLink = function(url) {
        var linkTagList = $(this.selector + " table .link").get();
        for ( i in linkTagList ){
            var linkTag = linkTagList[i];
            var beforHtml = linkTag.innerHTML;
            var resultHtml = "<a href='/dashboard/admin/" + url + "/" + this.data[i].id + "'>" + beforHtml + "</a>";
            linkTag.innerHTML = resultHtml;
        }
    }

    return this;
}