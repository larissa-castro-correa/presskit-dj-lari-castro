import re

with open("/Users/lari/Desktop/presskit/presskitoficial.html", "r") as f:
    c = f.read()

# 1. Font size of Lari Castro and Tribal House
c = c.replace('font-size:clamp(1.6rem,3vw,2.4rem);', 'font-size:clamp(2.4rem, 6vw, 4.5rem);')
c = c.replace('font-size:0.65rem;', 'font-size:1.1rem;')

# 2. Brighten image
c = c.replace('filter:brightness(0.72) saturate(1.1);', 'filter:brightness(0.95) saturate(1.1);')
c = c.replace('rgba(9,9,9,0.55)', 'rgba(9,9,9,0.25)')
c = c.replace('rgba(9,9,9,0.40)', 'rgba(9,9,9,0.15)')

# 3. Remove watermark LC
c = re.sub(r'<div class="hero__ghost" aria-hidden="true">LC</div>\s*', '', c)

# 4. Nav brand Logo_png.png
c = re.sub(r'<a href="#hero" class="nav__brand">LC</a>',
           r'<a href="#hero" class="nav__brand" style="display:flex;align-items:center;"><img src="Logo_png.png" alt="Logo Lari Castro" style="height:36px;"></a>', c)

# 5. Tribal House replacements
c = c.replace('Tribal House &middot; Afro House &middot; Melodic Techno', 'Tribal House')
c = c.replace('Tribal House · Afro House · Melodic Techno', 'Tribal House')
c = c.replace('— que passeiam entre <strong>Tribal House</strong>, <strong>Afro House</strong> e <strong>Melodic Techno</strong> —', '— com foco no <strong>Tribal House</strong> —')

with open("/Users/lari/Desktop/presskit/presskitoficial.html", "w") as f:
    f.write(c)
