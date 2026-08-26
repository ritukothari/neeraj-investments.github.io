document.addEventListener('DOMContentLoaded', function () {
  const footer = document.querySelector('.foot');
  if (!footer || footer.querySelector('.grievance-officer')) return;

  const grievance = document.createElement('div');
  grievance.className = 'grievance-officer';
  grievance.innerHTML = '<strong>Grievance Officer</strong><span>Neeraj Jain</span><span>Mobile: 9412206425</span><span>Email: <a href="mailto:neerajjainmeerut@outlook.com">neerajjainmeerut@outlook.com</a></span>';
  footer.appendChild(grievance);
});
