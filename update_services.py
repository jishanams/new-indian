import re

file_path = r"d:\DO tech works\new-indian-service-center\core\templates\core\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

css_replacement = """    /* services */
    .svc-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      margin-top: 44px
    }
    @media (max-width: 1024px) {
      .svc-grid { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 768px) {
      .svc-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 480px) {
      .svc-grid { grid-template-columns: 1fr; }
    }

    .svc {
      background: var(--white);
      border-radius: 16px;
      padding: 30px 24px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
      transition: .25s;
      border: 1px solid transparent;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }

    .svc:hover {
      transform: translateY(-4px);
      box-shadow: 0 14px 30px rgba(13, 47, 107, .12);
      border-color: #E3E7EE;
    }

    .svc img.ic {
      height: 42px;
      width: auto;
      margin-bottom: 20px;
    }

    .svc h3 {
      font-size: 16px;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 12px;
      color: var(--nexa-black);
      position: relative;
      padding-bottom: 12px;
    }

    .svc h3::after {
      content: "";
      position: absolute;
      left: 0;
      bottom: 0;
      width: 24px;
      height: 3px;
      background: var(--ms-blue);
      border-radius: 2px;
    }

    .svc p {
      font-size: 14.5px;
      color: var(--steel);
      line-height: 1.6;
    }

    /* why */"""

html_replacement = """<div class="svc-grid">
        <div class="svc">
          <img class="ic" src="{% static 'gift.png' %}" alt="Free Service">
          <h3>Free Service</h3>
          <p>Scheduled free services for new Maruti Suzuki vehicles, as per the company service schedule.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'paid.png' %}" alt="Paid Service">
          <h3>Paid Service</h3>
          <p>Periodic maintenance with genuine parts — oil, filters, brakes, full checkup.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'tick.png' %}" alt="Warranty Service">
          <h3>Warranty Service</h3>
          <p>Warranty repairs and replacements handled directly, with full documentation.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'car.png' %}" alt="Nexa Service">
          <h3>Nexa Service</h3>
          <p>Authorized servicing for Nexa range — Baleno, Fronx, Grand Vitara, Ciaz, Jimny, Invicto and more.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'arena.png' %}" alt="Arena Service">
          <h3>Arena Service</h3>
          <p>Complete care for Arena models — Swift, Alto, WagonR, Brezza, Dzire, Ertiga and more.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'door.png' %}" alt="Body Repairing Works">
          <h3>Body Repairing Works</h3>
          <p>Dent removal, panel work and accident body repairs restored to factory finish.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'claim.png' %}" alt="Claim Works">
          <h3>Claim Works</h3>
          <p>Accident insurance claims processed end to end — survey, estimate, repair, settlement.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'spray.png' %}" alt="Painting">
          <h3>Painting</h3>
          <p>Full-body and panel painting with exact factory color matching.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'wheel.png' %}" alt="Wheel Alignment">
          <h3>Wheel Alignment</h3>
          <p>Computerized alignment and balancing — essential for Wayanad's hill roads.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'rain drop.png' %}" alt="Water Service">
          <h3>Water Service</h3>
          <p>Exterior wash, underbody cleaning and interior vacuuming.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'snow.png' %}" alt="A/C Works">
          <h3>A/C Works</h3>
          <p>A/C gas refilling, cooling coil service and compressor repairs.</p>
        </div>
        <div class="svc">
          <img class="ic" src="{% static 'scanning copy.png' %}" alt="Scanning Works">
          <h3>Scanning Works</h3>
          <p>Computerized diagnostics to detect engine, sensor and ECU faults accurately.</p>
        </div>
      </div>"""

# Replace CSS
css_pattern = re.compile(r'/\*\s*services\s*\*/.*?(?=\/\*\s*why\s*\*\/)', re.DOTALL)
content = css_pattern.sub(css_replacement + "\n", content)

# Replace HTML
html_pattern = re.compile(r'<div class="svc-grid">.*?(?=</div>\s*</div>\s*</section>)', re.DOTALL)
content = html_pattern.sub(html_replacement + "\n", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully.")
