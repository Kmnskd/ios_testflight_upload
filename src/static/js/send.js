$(function() {
    $("#uploadForm").bind('click',function(){
      $.post('/upload/upload_package', {
        package_url: $('input[name="package_url"]').val(),
        username: $('input[name="username"]').val(),
        password: $('input[name="password"]').val(),
      }, function(res) {
         $('input[name="package_url"]').val('')
         $('input[name="username"]').val('')
         $('input[name="password"]').val('')
        $("#toast").addClass("show")
        $("#toast").removeClass("hide")
        setTimeout(function(){
            $("#toast").addClass("hide")
            $("#toast").removeClass("show")
        }, 5000)
      });
    })
});