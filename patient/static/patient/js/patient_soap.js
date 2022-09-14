$(document).ready(function() {
    let total_soap = $('#id_related_patient-TOTAL_FORMS').val();
    $('#id_related_patient-FORMS').each(
        function (index) {
            let input = $(this);
            //console.log(input);
            for(let i=0; i<total_soap; i++) {
                let child_id = '#inline_child_related_patient-' + i;
                let child_element = input.find(child_id);
                child_element.find('.w-field__input').find('option:not(:selected)').remove();
            }
        });
});
