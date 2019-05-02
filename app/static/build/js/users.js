/*
global
alertify: false
*/

/**
 * Create a new account.
 */

function openModal() {
    $('#user-form *').filter(':input').each(function() {
        //for select option
        this.value = "";
    });
    $('#modalBox').modal('show');

}

function addUser() { // eslint-disable-line no-unused-vars
    if ($('#user-form').parsley().validate()) {
        $.ajax({
            type: 'POST',
            url: '/admin/api/users',
            dataType: 'json',
            data: $('#user-form').serialize(),
            success: function(result) {
                if (result.status == 'failed') {
                    alertify.notify(result.message, 'error', 5);
                } else {
                    alertify.notify(result.message, 'success', 5);
                    location.reload();
                }
            },
        });
    }
}

function getUser(id) { // eslint-disable-line no-unused-vars
    $.ajax({
        type: 'GET',
        url: '/admin/api/users/' + id,
        success: function(result) {
            $('#user-form *').filter(':input').each(function() {
                //for select option
                if (this.type == "select-one") {
                    $('#' + this.id).val(result[this.name+"_id"]);
                } else {
                    this.value = result[this.name];
                }
            });
            // replace text and function that going to be called so it can update user
            $('#modalBoxTitle').text("Update User");
            $("#formButton").attr("onclick", "updateUser('" + id + "')");
            // pop up box here
            $('#modalBox').modal('show');
        }
    });
}

function updateUser(id) { // eslint-disable-line no-unused-vars
    if ($('#user-form').parsley().validate()) {
        $.ajax({
            type: 'PUT',
            url: '/admin/api/users/' + id,
            dataType: 'json',
            data: $('#user-form').serialize(),
            success: function(result) {
                if (result.status == 'failed') {
                    alertify.notify(result.message, 'error', 5);
                } else {
                    alertify.notify(result.message, 'success', 5);
                    location.reload();
                }
            },
        });
    }
}

function deleteUser(id) { // eslint-disable-line no-unused-vars
    // open confirmation box
    $("#confirmBox").modal('show');

    modalConfirm(function(confirm) {
        if (confirm) {
            $.ajax({
                type: 'DELETE',
                url: '/admin/api/users/' + id,
                success: function(result) {
                    if (result.status == 'failed') {
                        alertify.notify(result.message, 'error', 5);
                    } else {
                        alertify.notify(result.message, 'success', 5);
                        location.reload();
                    }
                }
            });
        } else {
            console.log("something happen here on no ");
        }
    });
}