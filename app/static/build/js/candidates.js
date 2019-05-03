/*
global
alertify: false
*/

/**
 * Create a new account.
 */

 var candidate_id = "";

function openModal() {
    $('#candidate-form *').filter(':input').each(function() {
        //for select option
        this.value = "";
    });
    $('#modalBox').modal('show');

}

function openModal2(id) {
    console.log(id);
    $('#user-candidate-form *').filter(':input').each(function() {
        //for select option
        this.value = "";
    });
    $('#modalBox2').modal('show');
    candidate_id = id;

}

function addCandidate() { // eslint-disable-line no-unused-vars
    // extract election ID from url
    var url = (window.location.pathname).split("/");
    console.log(url);
    var election_id = url[2];

    if ($('#candidate-form').parsley().validate()) {
        $.ajax({
            type: 'POST',
            url: '/admin/api/' + election_id + "/candidates",
            dataType: 'json',
            data: $('#candidate-form').serialize(),
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

function enrollUser() { // eslint-disable-line no-unused-vars
    // extract election ID from url
    if ($('#user-candidate-form').parsley().validate()) {
        var form = $('#user-candidate-form').serialize();
        var user_id = form.split("=")[1];

        $.ajax({
            type: 'POST',
            url: '/admin/api/' + user_id + "/enroll/" + candidate_id,
            dataType: 'json',
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

function getCandidate(id) { // eslint-disable-line no-unused-vars
    var url = (window.location.pathname).split("/");
    console.log(url);
    var election_id = url[2];

    $.ajax({
        type: 'GET',
        url: '/admin/api/' + election_id + "/candidates/" + id,
        success: function(result) {
            $('#candidate-form *').filter(':input').each(function() {
                //for select option
                if (this.type == "select-one") {
                    $('#' + this.id).val(result[this.name+"_id"]);
                } else {
                    this.value = result[this.name];
                }
            });
            // replace text and function that going to be called so it can update candidate
            $('#modalBoxTitle').text("Update candidate");
            $("#formButton").attr("onclick", "updatecandidate('" + id + "')");
            // pop up box here
            $('#modalBox').modal('show');
        }
    });
}

function updateCandidate(id) { // eslint-disable-line no-unused-vars
    var url = (window.location.pathname).split("/");
    var election_id = url[3];

    if ($('#candidate-form').parsley().validate()) {
        $.ajax({
            type: 'PUT',
            url: '/admin/api/' + election_id + "/candidates/" + id,
            dataType: 'json',
            data: $('#candidate-form').serialize(),
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

function deleteCandidate(id) { // eslint-disable-line no-unused-vars
    // open confirmation box
    $("#confirmBox").modal('show');

    var url = (window.location.pathname).split("/");
    console.log(url);
    var election_id = url[2];

    modalConfirm(function(confirm) {
        if (confirm) {
            $.ajax({
                type: 'DELETE',
            url: '/admin/api/' + election_id + "/candidates/" + id,
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