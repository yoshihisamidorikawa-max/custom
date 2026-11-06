const dialog = document.querySelector('#contact-dialog');
document.querySelectorAll('[data-contact]').forEach(button => button.addEventListener('click', () => dialog.showModal()));
dialog.addEventListener('click', event => { if (event.target === dialog) { const rect = dialog.getBoundingClientRect(); if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close(); } });
