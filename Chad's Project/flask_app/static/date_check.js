$(document).ready(function() {
    var bookedDates = [];

    // Retrieve booked dates from the HTML template
    $(".booked-dates li").each(function() {
        var dateRange = $(this).text().split(" - ");
        var start = new Date(dateRange[0]);
        var end = new Date(dateRange[1]);
        bookedDates.push({ start: start, end: end });
    });

    $("#check_in_date").datepicker({
        minDate: 0,
        beforeShowDay: function(date) {
            for (var i = 0; i < bookedDates.length; i++) {
                var startDate = bookedDates[i].start;
                var endDate = bookedDates[i].end;
                if (date >= startDate && date <= endDate) {
                    return [false, "booked-date", "Booked"];
                }
            }
            return [true, ""];
        }
    });

    $("#check_out_date").datepicker({
        minDate: 0,
        beforeShowDay: function(date) {
            for (var i = 0; i < bookedDates.length; i++) {
                var startDate = bookedDates[i].start;
                var endDate = bookedDates[i].end;
                if (date >= startDate && date <= endDate) {
                    return [false, "booked-date", "Booked"];
                }
            }
            return [true, ""];
        }
    });

    // Highlight the range of selected dates
    $("#check_in_date").change(function() {
        $("#check_out_date").datepicker("option", "minDate", $("#check_in_date").val());
    });
    $("#check_out_date").change(function() {
        $("#check_in_date").datepicker("option", "maxDate", $("#check_out_date").val());
    });
});




