$(document).ready(function() {
    $('#btn_translate').click(fetchTranslation);

    $('#language_code').keypress(function(event) {
        if (event.keyCode === 13) { // Enter key
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        var languageCode = $('#language_code').val();
        if (languageCode.trim() === '') {
            alert('Please enter a language code');
            return;
        }

        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            dataType: 'json',
            data: { lang: languageCode },
            success: function(response) {
                $('#hello').text(response.hello);
            },
            error: function(xhr, status, error) {
                console.error('Error fetching translation:', error);
                $('#hello').text('Translation not available');
            }
        });
    }
});
