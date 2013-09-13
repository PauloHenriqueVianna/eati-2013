$(document).ready(function(){
  $('#verifica').validate({
    rules: {
      email: {
        required: true,
        email: true,
        maxlength: 200
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

$(document).ready(function(){
  $('#inscricao').validate({
    rules: {
      nome: { 
        required: true,
        maxlength: 100
      },
      email: {
        required: true,
        email: true,
        maxlength: 200
      },
      sexo: {
        required: true
      },
      instituicao: {
        maxlength: 100
      },
      endereco: {
        required: true,
        maxlength: 100
      },
      complemento: {
        maxlength: 100
      },
      cep: {
        required: true,
        maxlength: 9
      },
      municipio: {
        required: true,
        maxlength: 100
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

$(document).ready(function(){
  $("#cep").mask("99999-999");
});