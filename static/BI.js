(function () {
	//グラフ作成可能範囲にあるか判断
	var graph_field_flag = false;
	var column_list = {};
	
	$('.column_elm').on('click', function(){
		if(event.shiftKey && graph_field_flag){
			console.log("choice it");
		}
	});
	
	$(".column_elm").draggable()
	
	$(".graph_field").droppable({
		accept : ".column_elm" , // 受け入れる要素を指定
		drop : function(event , ui){ // ドロップされた時に動きます
			graph_field_flag = true;
			console.log("in graph_field");
		}
	});
	
	$(".column_box").droppable({
		accept : ".column_elm" , // 受け入れる要素を指定
		drop : function(event , ui){ // ドロップされた時に動きます
			graph_field_flag = false;
			console.log("in column_box");
		}
	});
	
})();