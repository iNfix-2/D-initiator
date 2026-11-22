const clock = document.querySelector('[data-clock]');
if (clock) {
  const format = new Intl.DateTimeFormat('en-GB', {
    timeZone: 'Africa/Lagos',
    hour: '2-digit',
    minute: '2-digit',
    hourCycle: 'h23',
  });
  const update = () => { clock.textContent = format.format(new Date()) + ' WAT'; };
  update();
  setInterval(update, 30000);
}

const menuToggle = document.querySelector('.nav-toggle');
const menu = document.getElementById('main-nav');
const mobileMenu = matchMedia('(max-width: 880px)');
function setMenu(open) {
  menu.hidden = mobileMenu.matches && !open;
  menuToggle.setAttribute('aria-expanded', String(open));
}
function updateMenu() {
  menuToggle.hidden = !mobileMenu.matches;
  setMenu(false);
}
updateMenu();
mobileMenu.addEventListener('change', updateMenu);
menuToggle.addEventListener('click', () => setMenu(menu.hidden));
menu.addEventListener('click', (event) => {
  if (event.target.closest('a') && mobileMenu.matches) {
    setMenu(false);
    menuToggle.focus();
  }
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && mobileMenu.matches && !menu.hidden) {
    setMenu(false);
    menuToggle.focus();
  }
});

const projectDetails = document.querySelectorAll('.project-details');
const stackedProjects = matchMedia('(max-width: 655px)');
function updateDetails() {
  projectDetails.forEach((details) => { details.open = !stackedProjects.matches; });
}
updateDetails();
stackedProjects.addEventListener('change', updateDetails);

const dialog = document.querySelector('.image-dialog');
if (dialog && typeof dialog.showModal === 'function') {
  const enlarged = dialog.querySelector('img');
  const caption = dialog.querySelector('p');
  document.querySelectorAll('[data-gallery]').forEach((link) => {
    link.addEventListener('click', (event) => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      caption.textContent = link.querySelector('img').alt;
      enlarged.src = link.href;
      dialog.showModal();
    });
  });
  dialog.addEventListener('close', () => enlarged.removeAttribute('src'));
}
