$(document).ready(function() {
    $('#notesForm').submit(function() {
        var options = {
                    dataType: 'json',
                    success: function(data) {
                        if (data.errors){
                            if (!($('#success-alert').hasClass('hidden'))){
                                $('#success-alert').addClass('hidden')
                            }
                            if (data.errors.text){
                                $('#text-field').addClass('has-error')
                                $('#errors-text').html(data.errors.text)
                            }
                            else {
                                $('#text-field').removeClass('has-error')
                                $('#errors-text').html('')
                            }
                            if (data.errors.image){
                                $('#image-field').addClass('has-error')
                                $('#errors-image').html(data.errors.image)
                            }
                            else {
                                $('#image-field').removeClass('has-error')
                                $('#errors-image').html('')
                            }
                            $('#error-alert').removeClass('hidden')
                            $('#non-field-errors').html(data.non_field_errors)
                        }
                        else {
                            if (!($('#error-alert').hasClass('hidden'))){
                                $('#error-alert').addClass('hidden')
                            }
                            $('#success-alert').removeClass('hidden')
                            $('#success-alert').html(data.message)
                            $('#text-field').removeClass('has-error')
                            $('#errors-text').html('')
                            $('#text').val('')
                            $("#image-input").val('')
                            $('#notes-count').html(data.notes_count)
                        };
                    },
        };
        $(this).ajaxSubmit(options);
        return false;
        });

    var title = document.title
    var viewed_requests_pk_list = []

    Visibility.every(1000, function() {
        document.title = "Active | " + title;
        $.get("/last_requests/", function(data) {
            $('#request_list').empty();
            for (index in data){
                $('#request_list').append($('<li>').append(
                    data[index].timestamp+
                    " url: "+data[index].url+
                    ", method: "+data[index].method
                    )
                );
                if (!viewed_requests_pk_list.includes(data[index].pk)) {
                    viewed_requests_pk_list.push(data[index].pk)
                };
            };
        console.log(viewed_requests_pk_list)
        });
    });

    Visibility.change(function (e, state) {
        if (state=='visible'){
            document.title = "Active | " + title;
        }
        else if (state=='hidden'){
            
        };
    });
});
