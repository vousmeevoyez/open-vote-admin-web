/*
global
alertify: false
*/

var origin   = window.location.origin;

/**
 * Create a new account.
 */
function signup() { // eslint-disable-line no-unused-vars
  if ($('#create-user-form').parsley().validate()) {
    $.ajax({
      type: 'POST',
      url: '/auth/api/register',
      dataType: 'json',
      data: $('#create-user-form').serialize(),
      success: function(result) {
        if (result.status == 'failed') {
          alertify.notify(result.message, 'error', 5);
        } else {
          alertify.notify(result.message, 'success', 5);
          document.getElementById('login-button').click();
        }
      },
    });
  }
}

/**
 * login
 */
function signIn() { // eslint-disable-line no-unused-vars
  if ($('#login-user-form').parsley().validate()) {
    $.ajax({
      type: 'POST',
      url: '/auth/api/login',
      dataType: 'json',
      data: $('#login-user-form').serialize(),
      success: function(result) {
        if (result.status == 'failed') {
          alertify.notify(result.message, 'error', 5);
        } else {
          alertify.notify(result.message, 'success', 5);
          window.location.replace(origin + result.redirect);
        }
      },
    });
  }
}
