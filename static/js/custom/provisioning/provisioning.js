function Provisioning(){
    this.nodes = [{id: 0, reflexive: false, x: 100, y: 100, name: "hi", fixed:true},
    {id: 1, reflexive: true , x: 200, y: 200, name: "베르나르베르베르", fixed:true},
    {id: 2, reflexive: false, x: 300, y: 100, name: "타나타노트"},
    {id: 3, reflexive: true , x: 200, y: 200, name: "hello my world, kia"},
    {id: 4, reflexive: false, x: 300, y: 100},
    {id: 5, reflexive: false, x: 300, y: 100},
    {id: 6, reflexive: false, x: 300, y: 100}];
    this.lastNodeId = 6;

    /*
        this.links format
        {source: this.nodes[0], target: this.nodes[1], left: false, right: true },
        {source: this.nodes[1], target: this.nodes[2], left: false, right: true }
    */
    this.links = [
    {source: this.nodes[0], target: this.nodes[1], left: false, right: true },
    {source: this.nodes[1], target: this.nodes[2], left: false, right: true }];

    /*
        this.groups format
        {id:0, nodeList:[this.nodes[0], this.nodes[1], this.nodes[2]]},
        {id:1, nodeList:[this.nodes[3], this.nodes[4]]},
        {id:2, nodeList:[this.nodes[5]]}
    */
    this.groups = [{id:0, nodeList:[this.nodes[0], this.nodes[1], this.nodes[2]]},
    {id:1, nodeList:[this.nodes[3], this.nodes[4]]},
    {id:2, nodeList:[this.nodes[5]]}];
    this.width  = 1280;
    this.height = 720;
    this.colors = d3.scale.category10();


    this.svg = d3.select('#vis')
        .append('svg')
        .attr('oncontextmenu', 'return false;')
        .attr('width', this.width)
        .attr('height', this.height);

    this.addNode = function(this.node){
        /*{
            id:node.region_id,
            name:"name",
            reflexive:false,
            x:node.x,
            y:node.y,
            data:{
    //            vm_list = node.
            }
        }*/
    }

    this.getServiceAjax = function(csrf_token) { // token, tenant_name, user_name, service_id
        $.ajax({
            type:"POST",
            url : 'get_service',
            data : { csrfmiddlewaretoken : csrf_token },
            success:function(jsonData){
                addNode(jsonData.node);
            }
        });
    }




    this.nodesRadius = 30;
    // init D3 force layout
    this.force = d3.layout.force()
            .nodes(this.nodes)
            //.links(this.links)     //링크된 노드의 거리 유지
            .size([this.width, this.height])
            //.linkDistance(150)    //링크된 노드의 거리
            .charge(-1000)       //노드간의 거리
            .on('tick', this.tick);
    this.focusNodeName = false;

    // define arrow markers for graph links
    this.svg.append('svg:defs').append('svg:marker')
            .attr('id', 'end-arrow')
            .attr('viewBox', '0 -5 10 10')
            .attr('refX', 6)
            .attr('markerWidth', 3)
            .attr('markerHeight', 3)
            .attr('orient', 'auto')
            .append('svg:path')
            .attr('d', 'M0,-5L10,0L0,5')
            .attr('fill', '#000');

    this.svg.append('svg:defs').append('svg:marker')
            .attr('id', 'start-arrow')
            .attr('viewBox', '0 -5 10 10')
            .attr('refX', 4)
            .attr('markerWidth', 3)
            .attr('markerHeight', 3)
            .attr('orient', 'auto')
            .append('svg:path')
            .attr('d', 'M10,-5L0,0L10,5')
            .attr('fill', '#000');

    // line displayed when dragging new nodes
    this.drag_line = this.svg.append('svg:path')
        .attr('class', 'link dragline hidden')
        .attr('d', 'M0,0L0,0');

    // handles to link and node element groups
    // 생성순서에따라 위아래가 바뀜(태그위치)
    // 만약 gGroup 이 pathLink 보다 위에 있다면 화면에서 그룹이 링크를 가려 눌리지않음
    this.gGroup = this.svg.append('svg:g');
    this.pathLink = this.svg.append('svg:g').selectAll('path');
    this.gCircle = this.gGroup.attr('group', '1').selectAll('g');
    this.pathGroup = this.gGroup.selectAll('path');
    // mouse event vars
    this.selected_node = null;
    this.selected_link = null;
    this.mousedown_link = null;
    this.mousedown_node = null;
    this.mouseup_node = null;

    this.tempCnt = 0

    this.resetMouseVars = function() {
        this.mousedown_node = null;
        this.mouseup_node = null;
        this.mousedown_link = null;
    }

    // update force layout (called automatically each iteration)
    this.tick = function() {
        this.pathGroup.attr('d', function(d) {
            var data = "";
            for(var j in d.nodeList)
                data += (j != 0 ? "L" : "M") + d.nodeList[j].x + "," + d.nodeList[j].y;
            if (data.length !== 2) data += "Z"; // work around Firefox bug.
            return data;
        });
        // draw directed edges with proper padding from node centers
        this.pathLink.attr('d', function(d) {
            var deltaX = d.target.x - d.source.x;       //선 연결 X좌표 중앙에서출발
            var deltaY = d.target.y - d.source.y;       //선 연결 Y좌표 중앙에서출발
            var dist = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
            var normX = deltaX / dist;
            var normY = deltaY / dist;
            var sourcePadding = d.left ? this.nodesRadius + 5 : this.nodesRadius;
            var targetPadding = d.right ? this.nodesRadius + 5 : this.nodesRadius;
            var sourceX = d.source.x + (sourcePadding * normX);
            var sourceY = d.source.y + (sourcePadding * normY);
            var targetX = d.target.x - (targetPadding * normX);
            var targetY = d.target.y - (targetPadding * normY);
            return 'M' + sourceX + ',' + sourceY + 'L' + targetX + ',' + targetY;
        });

        this.gCircle.attr('transform', function(d) {
            return 'translate(' + d.x + ',' + d.y + ')';
        });
        showNodeInfo();
        var nodeName = $('#nodeName');
        nodeName.focus(function(){
            this.focusNodeName = true;
        });
        nodeName.blur(function(){
            this.focusNodeName = false;
        });
        $('#nameBtn').on('click', function(){
            this.selected_node.name = nodeName.val();
            this.restart();
        });
    }

    this.showNodeInfo = function(){
        var node_info_html = ""
        if (this.selected_node != null) {
            var selected_nodeKeyArray = Object.keys(this.selected_node);
            for(var i in selected_nodeKeyArray) {
                if (selected_nodeKeyArray[i] != "px" && selected_nodeKeyArray[i] != "py" && selected_nodeKeyArray[i] != "px" && selected_nodeKeyArray[i] != "py" ) {
                    node_info_html += "<tr><td>" + selected_nodeKeyArray[i] + "</td><td> " + eval("selected_node." + selected_nodeKeyArray[i]) + "</td></tr>";
                }
            }
            this.tempCnt += 1;
            if (this.tempCnt / 50 == 1) {
                console.log("selected_nod[key] : "+Object.keys(this.selected_node));
                this.tempCnt = 0;
            }
        }
        else {
            node_info_html += "<tr><td>node를 선택하세요.</td></tr>";
        }
        d3.select("#infoTable").html(node_info_html);
    }
    // update graph (called when needed)
    this.restart = function() {
        this.pathGroup = this.pathGroup.data(this.groups);
        this.pathGroup.enter().append('path')
            .attr('class', 'subset')
            .style("fill", function(d) { return colors(d.id); })
            .style("stroke", function(d) { return colors(d.id); });
        this.pathGroup.exit().remove();

        // path (link) group
        this.pathLink = this.pathLink.data(this.links);
        // update existing links
        this.pathLink.classed('selected', function(d) { return d === this.selected_link; })
            .style('marker-start', function(d) { return d.left ? 'url(#start-arrow)' : ''; })
            .style('marker-end', function(d) { return d.right ? 'url(#end-arrow)' : ''; });
            // add new links
        this.pathLink.enter().append('svg:path')
            .attr('class', 'link')
            .classed('selected', function(d) { return d === this.selected_link; })
            .style('marker-start', function(d) { return d.left ? 'url(#start-arrow)' : ''; })
            .style('marker-end', function(d) { return d.right ? 'url(#end-arrow)' : ''; })
            .on('mousedown', function(d) {
                if(d3.event.ctrlKey) return;
                 // select link
                this.mousedown_link = d;
                if(this.mousedown_link === this.selected_link) this.selected_link = null;
                else this.selected_link = this.mousedown_link;
                this.selected_node = null;
                this.restart();
            });
        // remove old links
        this.pathLink.exit().remove();
            // gCircle (node) group
        // NB: the function arg is crucial here! nodes are known by id, not by index!
        this.gCircle = this.gCircle.data(this.nodes, function(d) { return d.id; });
        // update existing nodes (reflexive & selected visual states)
        this.gCircle.selectAll('circle')
            .style('fill', function(d) { return (d === this.selected_node) ? d3.rgb(colors(d.id)).brighter().toString() : colors(d.id); })
            .classed('reflexive', function(d) { return d.reflexive; });
        this.gCircle.selectAll('text')
            .text(function(d) { return d.name; });
        // add new nodes
        var g = this.gCircle.enter().append('svg:g');
        g.append('svg:circle')
            .attr('class', 'node')
            .attr('r', this.nodesRadius)          //반지름
            .style('fill', function(d) { return (d === this.selected_node) ? d3.rgb(colors(d.id)).brighter().toString() : colors(d.id); })
            .style('stroke', function(d) { return d3.rgb(colors(d.id)).darker().toString(); })
            .classed('reflexive', function(d) { return d.reflexive; })
            .on('mouseover', function(d) {
                if(!this.mousedown_node || d === this.mousedown_node) return;
                // enlarge target node
                d3.select(this).attr('transform', 'scale(1.1)');
            })
            .on('mouseout', function(d) {
                if(!this.mousedown_node || d === this.mousedown_node) return;
                // unenlarge target node
                d3.select(this).attr('transform', '');
            })
            .on('mousedown', function(d) {
                if(d3.event.ctrlKey) return;
                 // select node
                this.mousedown_node = d;
                if(this.mousedown_node === this.selected_node) {  //node 선택 해제
                    this.selected_node = null;
                    var nodeNameTableHtml = "";
                    d3.select("#nameTable").html(nodeNameTableHtml);
                }
                else {  //node 선택
                    this.selected_node = this.mousedown_node;
                    var nodeNameTableHtml = "";
                    nodeNameTableHtml += '    <tr>';
                    nodeNameTableHtml += '        <td><input type="text" id="nodeName" value="' + this.selected_node.name + '"/></td>';
                    nodeNameTableHtml += '        <td><input id="nameBtn" type="button" value="변경"/></td>';
                    nodeNameTableHtml += '    </tr>';
                    d3.select("#nameTable").html(nodeNameTableHtml);
                }
                this.selected_link = null;
                 // reposition drag line
                this.drag_line
                    .style('marker-end', 'url(#end-arrow)')
                    .classed('hidden', false)
                    .attr('d', 'M' + this.mousedown_node.x + ',' + this.mousedown_node.y + 'L' + this.mousedown_node.x + ',' + this.mousedown_node.y);
                 this.restart();
            })
            .on('mouseup', function(d) {
                if(!this.mousedown_node) return;
                 // needed by FF
                this.drag_line
                    .classed('hidden', true)
                    .style('marker-end', '');
                 // check for drag-to-self
                this.mouseup_node = d;
                if(this.mouseup_node === this.mousedown_node) { resetMouseVars(); return; }
                 // unenlarge target node
                d3.select(this).attr('transform', '');
                 // add link to graph (update if exists)
                // NB: links are strictly source < target; arrows separately specified by booleans
                var source, target, direction;
                if(this.mousedown_node.id < this.mouseup_node.id) {
                    source = this.mousedown_node;
                    target = this.mouseup_node;
                    direction = 'right';
                } else {
                    source = this.mouseup_node;
                    target = this.mousedown_node;
                    direction = 'left';
                }
                 var link;
                link = this.links.filter(function(l) {
                    return (l.source === source && l.target === target);
                })[0];
                 if(link) {
                    link[direction] = true;
                } else {
                    link = {source: source, target: target, left: false, right: false};
                    link[direction] = true;
                    this.links.push(link);
                }
                 // select new link
                this.selected_link = link;
                this.selected_node = null;
                this.restart();
            });
        // show node IDs
        g.append('svg:text')
           .attr('x', 0)
           .attr('y', 4)
           .attr('class', 'id')
           .text(function(d) { return d.name; });
    //    g.on("mouseover", function (d) {
    //            d3.select(this).select('text')
    //              .text(function(d){return d.name;});
    //        });
        // remove old nodes
        this.gCircle.exit().remove();
        // set the graph in motion
        this.force.start();
    }

    this.insertNewNode = function(nodeId, name, x, y) {
            var node = {id: nodeId, name: name, reflexive: false, fixed:true};  // fixed : 고정
            node.x = x;
            node.y = y;

            this.nodes.push(node);
    }

    this.mousedown = function() {
        // prevent I-bar on drag
        //d3.event.preventDefault();
        // because :active only works in WebKit?
        this.svg.classed('active', true);
        if(d3.event.ctrlKey || this.mousedown_node || this.mousedown_link) return;

        // insert new node at point
        var point = d3.mouse(this);
        insertNewNode(++this.lastNodeId, "label", point[0], point[1]);
        this.restart();
    }

    this.mousemove = function() {
        if(!this.mousedown_node) return;
        // update drag line
        this.drag_line.attr('d', 'M' + this.mousedown_node.x + ',' + this.mousedown_node.y + 'L' + d3.mouse(this)[0] + ',' + d3.mouse(this)[1]);
        this.restart();
    }

    this.mouseup = function() {
        if(this.mousedown_node) {
            // hide drag line
            this.drag_line
                .classed('hidden', true)
                .style('marker-end', '');
        }
        // because :active only works in WebKit?
        this.svg.classed('active', false);
        // clear mouse event vars
        resetMouseVars();
    }

    this.spliceLinksForNode = function(node) {
        var toSplice = this.links.filter(function(l) {
            return (l.source === node || l.target === node);
        });
        toSplice.map(function(l) {
            this.links.splice(this.links.indexOf(l), 1);
        });
    }

    // only respond once per keydown
    this.lastKeyDown = -1;

    this.keydown = function() {
    //    d3.event.preventDefault();    //기본이벤트없애기

        if(this.lastKeyDown !== -1) return;
        this.lastKeyDown = d3.event.keyCode;
        // ctrl
        if(d3.event.keyCode === 17) {
            this.gCircle.call(this.force.drag);
            this.svg.classed('ctrl', true);
        }
        if((!this.selected_node && !this.selected_link) || this.focusNodeName) return;
        switch(d3.event.keyCode) {
            case 8: // backspace
            case 46: // delete
                if(this.selected_node) {
                    this.nodes.splice(this.nodes.indexOf(this.selected_node), 1);
                    spliceLinksForNode(this.selected_node);
                } else if(this.selected_link) {
                    this.links.splice(this.links.indexOf(this.selected_link), 1);
                }
                this.selected_link = null;
                this.selected_node = null;
                this.restart();
                break;
            case 66: // B
                if(this.selected_link) {
                    // set link direction to both left and right
                    this.selected_link.left = true;
                    this.selected_link.right = true;
                }
                this.restart();
                break;
            case 76: // L
                if(this.selected_link) {
                    // set link direction to left only
                    this.selected_link.left = true;
                    this.selected_link.right = false;
                }
                this.restart();
                break;
            case 82: // R
                if(this.selected_node) {
                    // toggle node reflexivity
                    this.selected_node.reflexive = !this.selected_node.reflexive;
                } else if(this.selected_link) {
                    // set link direction to right only
                    this.selected_link.left = false;
                    this.selected_link.right = true;
                }
                this.restart();
                break;
        }
    }

    this.keyup = function() {
        this.lastKeyDown = -1;
        // ctrl
        if(d3.event.keyCode === 17) {
            this.gCircle
                .on('mousedown.drag', null)
                .on('touchstart.drag', null);
            this.svg.classed('ctrl', false);
        }
    }

    // app starts here
    this.svg.on('mousedown', this.mousedown)
        .on('mousemove', this.mousemove)
        .on('mouseup', this.mouseup);
    d3.select(window)
        .on('keydown', this.keydown)
        .on('keyup', this.keyup);

    return this;
}
