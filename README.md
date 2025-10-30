<h1 align="center">🌌 Cosmic-Redshift-Distance-Tracker</h1>
<p align="center">
  <em>Python-based tool for calculating cosmic redshift and astronomical distances</em>
</p>

<hr>

<h2>🎯 Purpose & Scope</h2>
<p>
  <strong>Cosmic-Redshift-Distance-Tracker</strong> is a Python project that calculates and visualizes the relationship between <strong>cosmic redshift (z)</strong> and astronomical distances.  
  This tool is intended for students, researchers, and enthusiasts in cosmology to understand universe expansion and estimate distances to distant celestial objects.
</p>
<ul>
  <li>Calculate redshift (z) from observed spectral data using relativistic Doppler formula.</li>
  <li>Compute various cosmological distances: comoving distance, luminosity distance, and light travel distance.</li>
  <li>Visualize redshift-distance relationships.</li>
  <li>Optional bilingual graph outputs (Turkish / English).</li>
</ul>

<hr>

<h2>🧩 Project Structure</h2>

<pre>
📁 Cosmic-Redshift-Distance-Tracker/
│
├── tracker.py          → English script: calculates redshift and distances, produces graphs
├── tracker.py          → Turkish script: calculates redshift and distances, produces graphs
└── README.md           → This file
</pre>

<hr>

<h2>⚙️ Installation & Usage</h2>
<ol>
  <li>Make sure you have <strong>Python 3.x</strong> installed.</li>
  <li>Install dependencies:
    <pre><code>pip install numpy matplotlib</code></pre>
  </li>
  <li>Run the tracker:
    <pre><code>python tracker.py</code></pre>
  </li>
  <li>Graphs are saved as <code>.png</code> files and displayed automatically.</li>
</ol>

<hr>

<h2>🧮 Scientific Background</h2>

<h3>• Redshift Calculation</h3>
<p>
  Redshift is computed using the standard relativistic Doppler formula:
</p>
<pre>
z = (λ_observed - λ_emitted) / λ_emitted
</pre>
<p>
where:
  <ul>
    <li><code>λ_observed</code>: wavelength measured at Earth</li>
    <li><code>λ_emitted</code>: wavelength emitted by the source</li>
  </ul>
</p>

<h3>• Cosmological Distance Calculations</h3>
<p>
  Distances are computed based on standard cosmology:
</p>
<ul>
  <li><strong>Comoving Distance</strong>:
    <pre>D_C = c ∫(0 → z) dz' / H(z')</pre>
  </li>
  <li><strong>Luminosity Distance</strong>:
    <pre>D_L = (1 + z) · D_C</pre>
  </li>
  <li><strong>Light Travel Distance</strong>:
    <pre>D_T = ∫(0 → z) c dz' / H(z')</pre>
  </li>
</ul>

<p>
  where <code>H(z)</code> is the Hubble parameter at redshift z, and <code>c</code> is the speed of light.
</p>

<hr>

<h2>📊 Visualization</h2>
<p>
  The script generates plots of redshift vs. distance. Users can easily compare different cosmological models and visualize how the universe’s expansion affects observed distances.
</p>

<hr>

<h2>🌐 Resources</h2>
<ul>
  <li>Python Documentation: <a href="https://www.python.org/doc/">https://www.python.org/doc/</a></li>
  <li>Matplotlib Documentation: <a href="https://matplotlib.org/stable/users/index.html">https://matplotlib.org</a></li>
  <li>Cosmology Reference: Hogg, D. W. (1999). Distance measures in cosmology. arXiv:astro-ph/9905116</li>
</ul>




