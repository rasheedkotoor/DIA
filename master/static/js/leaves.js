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
// --------------------
"use strict";
let fv, offCanvasEl;
document.addEventListener("DOMContentLoaded", function (e) {
    var t;
    (t = document.getElementById("form-add-new-record")),
    setTimeout(() => {
        const e = document.querySelector(".create-new"),
        t = document.querySelector("#add-new-record");
        e && e.addEventListener("click", function () {
            (offCanvasEl = new bootstrap.Offcanvas(t)),
            (t.querySelector(".dt-user").value = ""),
            (t.querySelector(".dt-mv_reason").value = ""),
            (t.querySelector(".dt-destination").value = ""),
            (t.querySelector(".dt-leave_permitted_from").value = ""),
            (t.querySelector(".dt-leave_permitted_to").value = ""),
            // (t.querySelector(".dt-status").value = ""),
            offCanvasEl.show();
        });
    }, 200),
    (fv = FormValidation.formValidation(t, {
        fields: {
            user: { validators: { notEmpty: { message: "The name is required" } } },
            mv_reason: { validators: { notEmpty: { message: "Reason field is required" } } },
            destination: { validators: { notEmpty: { message: "Destination field is required" } } },
            leave_permitted_from: { validators: { notEmpty: { message: "Leave from Date is required" } } },
            // leave_permitted_to: { validators: { notEmpty: { message: "Leave to Date is required" } } },
            // status: { validators: { notEmpty: { message: "Status is required" } } },
        },
        plugins: {
            trigger: new FormValidation.plugins.Trigger(),
            bootstrap5: new FormValidation.plugins.Bootstrap5({ eleValidClass: "", rowSelector: ".col-sm-12" }),
            submitButton: new FormValidation.plugins.SubmitButton(),
            autoFocus: new FormValidation.plugins.AutoFocus(),
        },
        init: (e) => {
            e.on("plugins.message.placed", function (e) {
                e.element.parentElement.classList.contains("input-group") && e.element.parentElement.insertAdjacentElement("afterend", e.messageElement);
            });
        },
    }))


})