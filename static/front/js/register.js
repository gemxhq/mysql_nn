$(function () {
    $("#captcha-btn").on("click", function (event) {
        event.preventDefault();

        //发送验证码
        email = $("input[name='email']").val();
        zlajax.get({
            url: '/user/mail/captcha?email=' + email
        }).done(function (result) {
            // alert("验证码发送成功");
            alert(result.message);
        }).fail(function (error) {
            alert(error.message)
        })
    })
})