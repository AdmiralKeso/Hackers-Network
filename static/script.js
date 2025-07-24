const loginBtn = document.getElementById('loginBtn');
const loginSound = document.getElementById('login-sound');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const loadingBar = document.getElementById('loading-bar');
const loadingBarContainer = document.getElementById('loading-bar-container');
const message = document.getElementById('message');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function fakeLoadingBar(duration = 8600, flashes = 3, flashDelay = 250) {
  loadingBar.style.width = '0%';
  loadingBarContainer.style.display = 'block';
  message.textContent = 'Loading...';
  
  const steps = 100;
  for (let i = 0; i <= steps; i++) {
    loadingBar.style.width = i + '%';
    await sleep(duration / steps);
  }

  for (let i = 0; i < flashes; i++) {
    loadingBar.style.backgroundColor = '#00ff00';
    await sleep(flashDelay);
    loadingBar.style.backgroundColor = '#007700';
    await sleep(flashDelay);
  }
}

loginBtn.addEventListener('click', async () => {
  const username = usernameInput.value.trim();
  const password = passwordInput.value;

  if (!username) {
    message.style.color = '#f00';
    message.textContent = 'Please enter a username.';
    return;
  }

  loginBtn.disabled = true;
  usernameInput.disabled = true;
  passwordInput.disabled = true;
  message.style.color = '#0f0';
  message.textContent = 'Verifying credentials...';

  try {
    const response = await fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const result = await response.json();

    if (result.success) {
      loginSound.play();
      await fakeLoadingBar();
      message.textContent = result.message + '\n>>> Proceeding to Network Scan Stage...';
    } else {
      message.style.color = '#f00';
      message.textContent = result.message;
      loginBtn.disabled = false;
      usernameInput.disabled = false;
      passwordInput.disabled = false;
    }
  } catch (error) {
    message.style.color = '#f00';
    message.textContent = 'Error contacting server.';
  }
});