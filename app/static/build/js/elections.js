/*
global
alertify: false
*/

/**
 * Create a new account.
 */

function openModal() {
    $('#election-form *').filter(':input').each(function() {
        //for select option
        this.value = "";
    });
    $('#modalBox').modal('show');

}

function addElection() { // eslint-disable-line no-unused-vars
    if ($('#election-form').parsley().validate()) {
        $.ajax({
            type: 'POST',
            url: '/admin/api/elections',
            dataType: 'json',
            data: $('#election-form').serialize(),
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

function getElection(id) { // eslint-disable-line no-unused-vars
    $.ajax({
        type: 'GET',
        url: '/admin/api/elections/' + id,
        success: function(result) {
            $('#election-form *').filter(':input').each(function() {
                //for select option
                if (this.type == "select-one") {
                    $('#' + this.id).val(result[this.name+"_id"]);
                } else {
                    this.value = result[this.name];
                }
            });
            // replace text and function that going to be called so it can update Election
            $('#modalBoxTitle').text("Update Election");
            $("#formButton").attr("onclick", "updateElection('" + id + "')");
            // pop up box here
            $('#modalBox').modal('show');
        }
    });
}

function updateElection(id) { // eslint-disable-line no-unused-vars
    if ($('#election-form').parsley().validate()) {
        $.ajax({
            type: 'PUT',
            url: '/admin/api/elections/' + id,
            dataType: 'json',
            data: $('#election-form').serialize(),
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

function deleteElection(id) { // eslint-disable-line no-unused-vars
    // open confirmation box
    $("#confirmBox").modal('show');

    modalConfirm(function(confirm) {
        if (confirm) {
            $.ajax({
                type: 'DELETE',
                url: '/admin/api/elections/' + id,
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