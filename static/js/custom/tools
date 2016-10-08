function tabClick(i, tempTabList){
    var tabList = [];
    for (idx in tempTabList) {
        var tempTab = tempTabList[idx];
        tabList.push(tempTab);
    }
    var tab = tabList.splice(i, 1);
    for (j in tabList) {
        $("#" + tabList[j]).hide();
        $("." + tabList[j]).removeClass("header_title_d04_click");
        $("." + tabList[j]).addClass("header_title_d05");
    }
    $("." + tab).addClass("header_title_d04_click");
    $("." + tab).removeClass("header_title_d05");
    $("#" + tab).show();
}