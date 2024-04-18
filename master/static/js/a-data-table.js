// $(document).ready(function () {
//     $('#myTable thead tr')
//         .clone(true)
//         .addClass('filters')
//         .appendTo('#myTable thead');
//     $('#myTable').DataTable({
//         "rowCallback": function(row, data, index) {
//             if (index % 2 === 0) {
//                 $(row).css("background-color", "#f2f2f2"); // Light color
//             } else {
//                 $(row).css("background-color", "white"); // White
//             }
//         },
//         language: {
//             searchPlaceholder: "Search records",
//             search: "",
//         },
//     });
// });

$(document).ready(function () {
    // Setup filter
    // $('#myTable thead tr')
    //     .clone(true)
    //     .addClass('filters')
    //     .appendTo('#myTable thead');
 
    var table = $('#myTable').DataTable({
        "rowCallback": function(row, data, index) {
            if (index % 2 === 0) {
                $(row).css("background-color", "#f2f2f2"); // Light color
            } else {
                $(row).css("background-color", "white"); // White
            }
        },
        language: {
            searchPlaceholder: "Search records",
            search: "",
        },
        orderCellsTop: true,
        fixedHeader: true,

        dom: '<"card-header flex-column flex-md-row"<"head-label text-center"><"dt-action-buttons text-end pt-3 pt-md-0"B>><"row"<"col-sm-12 col-md-6"l><"col-sm-12 col-md-6 d-flex justify-content-center justify-content-md-end"f>>t<"row"<"col-sm-12 col-md-6"i><"col-sm-12 col-md-6"p>>',
        buttons: [
            { text: '<i class="bx bx-plus me-sm-1"></i> <span class="d-none d-sm-inline-block">Add New Record</span>', className: "create-new btn btn-primary" },
        ],
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal({
                    header: function (e) {
                        return "Details of " + e.data().full_name;
                    },
                }),
                type: "column",
                renderer: function (e, t, a) {
                    a = $.map(a, function (e, t) {
                        return "" !== e.title ? '<tr data-dt-row="' + e.rowIndex + '" data-dt-column="' + e.columnIndex + '"><td>' + e.title + ":</td> <td>" + e.data + "</td></tr>" : "";
                    }).join("");
                    return !!a && $('<table class="table"/><tbody />').append(a);
                },
            },
        },
        // filter function
        // initComplete: function () {
        //     var api = this.api();
 
        //     // For each column
        //     api.columns()
        //         .eq(0)
        //         .each(function (colIdx) {
        //             // Set the header cell to contain the input element
        //             var cell = $('.filters th').eq(
        //                 $(api.column(colIdx).header()).index()
        //             );
        //             var title = $(cell).text();
        //             // $(cell).html('<input type="text" placeholder="' + title + '" />');
        //             $(cell).html('<input type="text" style="width: 100%" placeholder="' + title + '" />');
 
        //             // On every keypress in this input
        //             $(
        //                 'input',
        //                 $('.filters th').eq($(api.column(colIdx).header()).index())
        //             )
        //                 .off('keyup change')
        //                 .on('change', function (e) {
        //                     // Get the search value
        //                     $(this).attr('title', $(this).val());
        //                     var regexr = '({search})'; //$(this).parents('th').find('select').val();
 
        //                     var cursorPosition = this.selectionStart;
        //                     // Search the column for that value
        //                     api
        //                         .column(colIdx)
        //                         .search(
        //                             this.value != ''
        //                                 ? regexr.replace('{search}', '(((' + this.value + ')))')
        //                                 : '',
        //                             this.value != '',
        //                             this.value == ''
        //                         )
        //                         .draw();
        //                 })
        //                 .on('keyup', function (e) {
        //                     e.stopPropagation();
 
        //                     $(this).trigger('change');
        //                     $(this)
        //                         .focus()[0]
        //                         .setSelectionRange(cursorPosition, cursorPosition);
        //                 });
        //         });
        // },

    });
});