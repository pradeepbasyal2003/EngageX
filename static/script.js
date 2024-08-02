document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault();
  alert('Login form submitted');
  // Add your login logic here
});

document.getElementById('signupForm').addEventListener('submit', function(event) {
  event.preventDefault();
  alert('Signup form submitted');
  // Add your signup logic here
});

function signupAs(role) {
  const username = document.getElementById('signupUsername').value;
  const password = document.getElementById('signupPassword').value;
  const email = document.getElementById('signupEmail').value;

  if (!username || !password || !email) {
      alert('Please enter all required fields');
      return;
  }

  alert(`Signed up as ${role} with username: ${username}`);
  // You can add your signup logic here based on the role
}

function showSignupForm() {
  document.getElementById('loginContainer').style.display = 'none';
  document.getElementById('signupContainer').style.display = 'block';
}

function showLoginForm() {
  document.getElementById('signupContainer').style.display = 'none';
  document.getElementById('loginContainer').style.display = 'block';
}
