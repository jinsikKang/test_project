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
        var columnPattern = "<th class='ind_th01 %K'>%C</th>\n"
        var dataPattern = "<td class='ind_td01 %K'>%D</td>\n";
        var resultHtml = ""
        if( this.vertical ){
            for( key in this.columns ){
                resultHtml += "<tr>\n";
                var columnHtml = "";
                var dataHtml = "";
                if ( this.columns[key] instanceof Object ) {
                    // 객체일때 여러줄로 출력
                    columnHtml = columnPattern.replace("%C", this.columns[key].name).replace("%K", key);
                    var data = "";
                    for ( dataNameKey in this.columns[key].dataName ){
                        data += this.columns[key].dataName[dataNameKey] + " " + this.data[key][dataNameKey] + "<br/>";
                    }
                    dataHtml = dataPattern.replace("%D", data).replace("%K", key);
                } else if ( this.data[key] instanceof Array ) {
                    // 배열일때 ul, li태그로 묶어 출력
                    columnHtml = columnPattern.replace("%C", this.columns[key]).replace("%K", key);
                    var data = "<ul>";
                    for ( i in this.data[key]){
                        data += "<li>" + this.data[key][i] + "</li>";
                    }
                    data += "</ul>";
                    dataHtml = dataPattern.replace("%D", data).replace("%K", key);
                } else {
                    columnHtml = columnPattern.replace("%C", this.columns[key]).replace("%K", key);
                    if( this.data[key] instanceof Object ){
                        for ( dataNameKey in this.data[key] ){
                            dataHtml = dataPattern.replace("%D", this.data[key][dataNameKey]).replace("%K", key);
                        }
                    } else {
                        dataHtml = dataPattern.replace("%D", this.data[key]).replace("%K", key);
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
                    dataHtml += "<td class='ind_td01 " + key + "'>" + this.data[i][key] + "</td>\n";
                }
                dataHtml += "</tr>\n";
            }
            resultHtml = columnHtml + dataHtml;
        }
        $(this.selector + " table").html(resultHtml);
    };
    return this;
}