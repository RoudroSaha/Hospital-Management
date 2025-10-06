// Registration and login specific functionality

document.addEventListener('DOMContentLoaded', function() {
    initAuthForms();
});

function initAuthForms() {
    // Toggle between login and register forms
    const showRegister = document.getElementById('showRegister');
    const showLogin = document.getElementById('showLogin');
    const loginForm = document.getElementById('loginForm').parentElement;
    const registerForm = document.getElementById('registerForm');
    
    if (showRegister && showLogin) {
        showRegister.addEventListener('click', function(e) {
            e.preventDefault();
            loginForm.style.display = 'none';
            registerForm.style.display = 'block';
        });
        
        showLogin.addEventListener('click', function(e) {
            e.preventDefault();
            registerForm.style.display = 'none';
            loginForm.style.display = 'block';
        });
    }
    
    // Enhanced form validation for registration
    const registrationForm = document.getElementById('registrationForm');
    if (registrationForm) {
        registrationForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const userName = document.getElementById('userName').value;
            const phoneNumber = document.getElementById('phoneNumber').value;
            const password = document.getElementById('regPassword').value;
            
            // Enhanced validation
            let isValid = true;
            
            // Username validation
            if (userName.length < 3) {
                showInputError(document.getElementById('userName'), 'Username must be at least 3 characters long');
                isValid = false;
            }
            
            // Phone number validation
            const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
            if (!phoneRegex.test(phoneNumber.replace(/\D/g, ''))) {
                showInputError(document.getElementById('phoneNumber'), 'Please enter a valid phone number');
                isValid = false;
            }
            
            // Password validation
            if (password.length < 6) {
                showInputError(document.getElementById('regPassword'), 'Password must be at least 6 characters long');
                isValid = false;
            }
            
            if (isValid) {
                // Simulate registration
                HealthApp.simulateApiCall({
                    userId: Math.random().toString(36).substr(2, 9),
                    userName: userName,
                    phoneNumber: phoneNumber
                }).then(response => {
                    HealthApp.showNotification('Registration successful! Please login.', 'success');
                    registerForm.style.display = 'none';
                    loginForm.style.display = 'block';
                    registrationForm.reset();
                });
            }
        });
    }
    
    // Enhanced login form validation
    const loginFormElement = document.getElementById('loginForm');
    if (loginFormElement) {
        loginFormElement.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            // Basic validation
            if (!username || !password) {
                HealthApp.showNotification('Please fill in all fields', 'danger');
                return;
            }
            
            // Simulate login
            HealthApp.simulateApiCall({
                token: 'mock-jwt-token',
                user: {
                    id: 1,
                    username: username,
                    role: 'user'
                }
            }).then(response => {
                HealthApp.showNotification('Login successful!', 'success');
                // Redirect to dashboard (in real app, this would be handled by your auth system)
                setTimeout(() => {
                    window.location.href = '../core/dashboard.html';
                }, 1000);
            });
        });
    }
}