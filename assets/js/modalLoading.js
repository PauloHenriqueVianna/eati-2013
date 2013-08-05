(function ($) {
    $.fn.modalLoading = function (height, message) {
    	if (!message) message = 'Loading...';

		modalLoading = $('<div style="position: fixed; display: block; z-index: 999999; text-align: center; font-size: 20px; background-color:rgba(238,238,238,0.8);">'+
							'<div style="display: inline-block; position:relative; top:50%;">'+
								'<i class="icon-spinner icon-spin blue bigger-125"></i> &nbsp; &nbsp; '+message+
							'</div>'+
						'</div>');

    	modalLoading.attr('id', 'modalLoading');

		modalLoading.css('width', this.innerWidth());

		if (height && height > 0) height = height+'%';
		else height = this.innerHeight();
		modalLoading.css('height', height);

		offset = this.offset();
		modalLoading.css('top', offset.top+'px');
		modalLoading.css('left', offset.left+'px');

    	this.append(modalLoading);

		return $(modalLoading);
    }
})(jQuery);