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
"use strict";
let fv, offCanvasEl;
document.addEventListener("DOMContentLoaded", function (e) {
    var t;
    (t = document.getElementById("form-add-new-record")),
    setTimeout(() => {
        const e = document.querySelector(".create-new"),
            t = document.querySelector("#add-new-record");
        e &&
            e.addEventListener("click", function () {
                (offCanvasEl = new bootstrap.Offcanvas(t)),
                    (t.querySelector(".dt-user").value = ""),
                    (t.querySelector(".dt-ac_category").value = ""),
                    // (t.querySelector(".dt-account_type").value = ""),
                    (t.querySelector(".dt-transaction_type").value = ""),
                    (t.querySelector(".dt-amount").value = ""),
                    // (t.querySelector(".dt-voucher_no").value = ""),
                    offCanvasEl.show();
            });
    }, 200),
    (fv = FormValidation.formValidation(t, {
        fields: {
            user: { validators: { notEmpty: { message: "The name is required" } } },
            ac_category: { validators: { notEmpty: { message: "Account category field is required" } } },
            account_type: { validators: { notEmpty: { message: "Account type is required" } } },
            transaction_type: { validators: { notEmpty: { message: "Transaction type is required" } } },
            amount: { validators: { notEmpty: { message: "Amount is required" } } },
            // voucher_no: { validators: { notEmpty: { message: "Voucher number is required" } } },
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