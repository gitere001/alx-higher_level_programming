$(document).ready(function() {
    // Add item
    $('#add_item').click(function() {
        $('<li>Item</li>').appendTo('ul.my_list');
    });

    // Remove last item
    $('#remove_item').click(function() {
        $('ul.my_list li:last-child').remove();
    });

    // Clear list
    $('#clear_list').click(function() {
        $('ul.my_list').empty();
    });
});
