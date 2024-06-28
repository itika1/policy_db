document.addEventListener('DOMContentLoaded', function() {
    const policyTypeSelect = document.querySelector('#id_policy_type');
    const medicalTypeField = document.querySelector('.form-row.field-medical_type');
    const medicalStatusField = document.querySelector('.form-row.field-medical_status');
    const remarksField = document.querySelector('.form-row.field-remarks');

    function toggleFields() {
        const policyType = policyTypeSelect.value;

        if (policyType === 'ICICI') {
            medicalTypeField.style.display = 'none';
            medicalStatusField.style.display = 'none';
            remarksField.style.display = '';
        } else if (policyType === 'MAX') {
            medicalTypeField.style.display = '';
            medicalStatusField.style.display = '';
            remarksField.style.display = 'none';
        } else {
            medicalTypeField.style.display = '';
            medicalStatusField.style.display = '';
            remarksField.style.display = '';
        }
    }

    if (policyTypeSelect) {
        toggleFields();
        policyTypeSelect.addEventListener('change', toggleFields);
    }
});
