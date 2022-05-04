document.addEventListener('DOMContentLoaded', function () {

    let calendarEl = document.getElementById('calendar');

    let calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',

        // 日付をクリック、または範囲を選択したイベント
        selectable: true,
        select: function (info) {
            alert("selected " + info.startStr + " to " + info.endStr);
        },
    });

    calendar.render();
});