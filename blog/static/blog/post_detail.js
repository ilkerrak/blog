(function($){
	$('.reply-link').on('click', function(){
		var comment_id = $(this).attr('comment-pk');
		$("#replymodal input[name=comment_id]").val(comment_id);
		$("#replymodal").modal("show");
	});
})(jQuery);