$(document).ready(function(){
  $('#support').validate({
    rules: {
      name: { 
        required: true
      },
      email: {
        required: true,
        email: true
      },
      subject: {
        required: true
      },
      message: {
        required: true
      }
    },
    highlight: function(element) {
      $(element).closest('.control-group').removeClass('success').addClass('error');
    },
    success: function(element) {
      element
      .addClass('valid')
      .closest('.control-group').removeClass('error').addClass('success');
    },
    submitHandler: function(form) {
      $(document.body).modalLoading(100, '<div class="spinner"></div>');
      form.submit();
    }
 });
});