$(document).ready(function() {
    let total_invoice = $('#id_related_invoice_patient-TOTAL_FORMS').val();
    $('#id_related_invoice_patient-FORMS').each(
        function (index) {
            let input = $(this);
            //console.log(input);
            for(let i=0; i<total_invoice; i++) {
                let child_id = '#inline_child_related_invoice_patient-' + i;
                let child_element = input.find(child_id);
                let id_is_final = '#id_related_invoice_patient-' + i + '-is_final';
                if (child_element.find(id_is_final).is(":checked")) {
                    // ReadOnly all input
                    child_element.find('.w-field__input').find('input').prop('readonly', true);

                    // ReadOnly all Selected
                    child_element.find('.w-field__input').find('option:not(:selected)').remove();

                    // is_final
                    let elem = child_element.find('div [data-contentpath="is_final"]');
                    let id_is_final = 'id_related_invoice_patient-' + i + '-is_final';
                    let name_is_final = 'related_invoice_patient-' + i + '-is_final';
                    child_element.find('input[id="' + id_is_final + '"').prop('disabled', true).prop('name', '');
                    elem.append('<input id="' + id_is_final + '" type="hidden" name="' + name_is_final + '" value="true">');

                    // datetime
                    let elem_datetime = child_element.find('div[data-contentpath="datetime"]');
                    let id_datetime = 'id_related_invoice_patient-' + i + '-datetime';
                    let name_datetime = 'related_invoice_patient-' + i + '-datetime';
                    let datetime_value = child_element.find('input[id="' + id_datetime + '"').val();

                    child_element.find('input[id="' + id_datetime + '"').prop('disabled', true).prop('name', '');
                    elem_datetime.append('<input id="' + id_datetime + '" type="hidden" name="' + name_datetime + '" value="' + datetime_value +'">');

                    let id_is_cancel = '#id_related_invoice_patient-' + i + '-is_cancel';
                    if (child_element.find(id_is_cancel).is(":checked")) {
                        let id_is_cancel = 'id_related_invoice_patient-' + i + '-is_cancel';
                        let elem_is_cancel = child_element.find('div[data-contentpath="is_cancel"]');
                        let name_is_cancel = 'related_invoice_patient-' + i + '-is_cancel';
                        child_element.find('input[id="' + id_is_cancel + '"').prop('disabled', true).prop('name', '');
                        elem_is_cancel.append('<input id="' + id_is_cancel + '" type="hidden" name="' + name_is_cancel + '" value="true">');
                    }

                    // Button Add Detail Item
                    let id_button = '#id_related_invoice_patient-' + i + '-related_invoice-ADD';
                    $(id_button).hide();

                } else {
                    let id_is_cancel = '#id_related_invoice_patient-' + i + '-is_cancel';
                    child_element.find(id_is_cancel).prop('disabled', true);
                }
            }
        });
});
