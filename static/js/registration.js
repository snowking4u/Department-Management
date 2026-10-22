const registrationForm = document.querySelector('.registration-form');
const password = document.querySelector('#password');
const confirmPassword = document.querySelector('#confirm_password');
const passwordMessage = document.querySelector('#password-message');

function validatePasswords() {
    if (!password || !confirmPassword) return true;

    const hasValue = confirmPassword.value.length > 0;
    const matches = password.value === confirmPassword.value;

    confirmPassword.setCustomValidity(matches ? '' : 'Passwords do not match.');
    confirmPassword.classList.toggle('invalid', hasValue && !matches);
    passwordMessage.textContent = hasValue && !matches ? 'Passwords do not match.' : '';

    return matches;
}

password?.addEventListener('input', validatePasswords);
confirmPassword?.addEventListener('input', validatePasswords);

registrationForm?.addEventListener('submit', (event) => {
    validatePasswords();

    if (!registrationForm.checkValidity()) {
        event.preventDefault();
        registrationForm.classList.add('was-validated');
        registrationForm.querySelector(':invalid')?.focus();
    }
});

document.querySelectorAll('[data-password-toggle]').forEach((button) => {
    button.addEventListener('click', () => {
        const input = document.getElementById(button.dataset.passwordToggle);
        const isHidden = input.type === 'password';

        input.type = isHidden ? 'text' : 'password';
        button.textContent = isHidden ? 'Hide' : 'Show';
        button.setAttribute('aria-label', `${isHidden ? 'Hide' : 'Show'} ${input.labels?.[0]?.textContent || 'password'}`);
    });
});
