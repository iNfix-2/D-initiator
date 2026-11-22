const clock = document.querySelector('[data-clock]');
if (clock) {
  const format = new Intl.DateTimeFormat('en-GB', {timeZone:'Africa/Lagos', hour:'2-digit',minute:'2-digit',hour12:false});
  const update = () => { clock.textContent = format.format(new Date()) + ' WAT'; };
  update();
  setInterval(update, 30000);
}
