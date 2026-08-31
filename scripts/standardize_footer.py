from pathlib import Path
import re

ROOT = Path('.')

FOOTER = '''<footer>
  <div class="container foot">
    <div>
      <strong>Quick Links</strong>
      <a href="index.html#about">About</a>
      <a href="index.html#products">Products</a>
      <a href="calculators.html">All Calculators</a>
      <a href="insurance.html">Insurance</a>
      <a href="learn.html">Learn</a>
      <a href="downloads.html">Downloads</a>
      <a href="contact.html">Contact</a>
      <a href="others.html">Others</a>
    </div>
    <div>
      <strong>Contact</strong>
      <span>Neeraj Jain</span>
      <span>D-347 Shastri Nagar, Meerut</span>
      <span>Uttar Pradesh 250004, India</span>
      <span>AMFI Registered Mutual Fund Distributor- ARN:8522 EUIN: E034983</span>
      <span>ARN &amp; EUIN validity 02.10.2024 to 01.10.2027. Registered with AMFI since 20.03.2003</span>
      <span><a href="tel:+919412206425">+91 94122 06425</a></span>
      <a href="mailto:neerajjainmeerut@outlook.com">neerajjainmeerut@outlook.com</a>
      <a href="mailto:njain17jun@gmail.com">njain17@gmail.com</a>
    </div>
    <div class="grievance-officer">
      <strong>Grievance Officer</strong>
      <span>Neeraj Jain</span>
      <span>Mobile: 9412206425</span>
      <span>Email: <a href="mailto:neerajjainmeerut@outlook.com">neerajjainmeerut@outlook.com</a></span>
    </div>
  </div>
  {amc}
  <div class="container legal">
    <div class="important-links">
      <span class="important-title">Important Links</span>
      <a href="disclaimer.html">Disclaimer</a>
      <a href="privacy-policy.html">Privacy Policy</a>
      <a href="disclosure.html">Disclosure</a>
      <a href="documents.html">SID/SAI/KIM</a>
      <a href="code-of-conduct.html">Code of Conduct</a>
      <a href="regulatory-links.html">SEBI Circulars</a>
      <a href="regulatory-links.html#amfi">AMFI Risk Factors</a>
      <a href="regulatory-disclosure.html">Regulatory Disclosure</a>
    </div>
    <div class="risk-note">Mutual fund investments are subject to market risks. Please read all scheme related documents carefully before investing.</div>
  </div>
</footer>'''

for path in ROOT.glob('*.html'):
    text = path.read_text(encoding='utf-8')
    match = re.search(r'<footer[\s\S]*?</footer>', text, re.I)
    if not match:
        continue
    old = match.group(0)
    amc_match = re.search(r'<div class=["\']container amc-section["\'][\s\S]*?</div>\s*</div>', old, re.I)
    amc = amc_match.group(0) if amc_match else ''
    new_footer = FOOTER.format(amc=amc)
    if old != new_footer:
        path.write_text(text[:match.start()] + new_footer + text[match.end():], encoding='utf-8')
