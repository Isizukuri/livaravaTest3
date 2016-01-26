$(document).ready(function() {
    $('#notesForm').submit(function() {
        var options = {
                    dataType: 'json',
                    success: function(data) {
                        if (data.errors){
                            if (!($('#success-alert').hasClass('hidden'))){
                                $('#success-alert').addClass('hidden')
                            }
                            $('#text-field').addClass('has-error')
                            $('#errors').html(data.errors.text)
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
                            $('#errors').html('')
                            $('#text').val('')
                            $('#notes-count').html(data.notes_count)
                        };
                    },
        };
        $(this).ajaxSubmit(options);
        return false;
        });
    });
