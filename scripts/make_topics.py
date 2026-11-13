import json
T=[("measurements-and-uncertainties","Measurements, units and uncertainties","Measurements",["3.1"]),
("atomic-structure-and-stable-nuclei","Atomic structure and stable nuclei","Particles and radiation",["3.2.1.1","3.2.1.2"]),
("particles-antiparticles-and-interactions","Particles, antiparticles and particle interactions","Particles and radiation",["3.2.1.3","3.2.1.4"]),
("classification-of-particles-and-quarks","Classification of particles, quarks and conservation laws","Particles and radiation",["3.2.1.5","3.2.1.6","3.2.1.7"]),
("photoelectric-effect","The photoelectric effect","Particles and radiation",["3.2.2.1"]),
("energy-levels-and-wave-particle-duality","Excitation, energy levels and wave-particle duality","Particles and radiation",["3.2.2.2","3.2.2.3","3.2.2.4"]),
("progressive-waves-and-polarisation","Progressive waves, longitudinal and transverse waves","Waves",["3.3.1.1","3.3.1.2"]),
("stationary-waves","Superposition and stationary waves","Waves",["3.3.1.3"]),
("interference-and-diffraction","Interference, diffraction and the diffraction grating","Waves",["3.3.2.1","3.3.2.2"]),
("refraction-and-optical-fibres","Refraction, total internal reflection and optical fibres","Waves",["3.3.2.3"]),
("vectors-and-moments","Scalars, vectors and moments","Mechanics and materials",["3.4.1.1","3.4.1.2"]),
("motion-and-projectiles","Motion along a straight line and projectile motion","Mechanics and materials",["3.4.1.3","3.4.1.4"]),
("newtons-laws-and-momentum","Newton's laws of motion and momentum","Mechanics and materials",["3.4.1.5","3.4.1.6"]),
("work-energy-and-power","Work, energy, power and conservation of energy","Mechanics and materials",["3.4.1.7","3.4.1.8"]),
("materials-and-young-modulus","Materials, stress, strain and the Young modulus","Mechanics and materials",["3.4.2"]),
("current-voltage-and-resistivity","Current, potential difference, I-V characteristics and resistivity","Electricity",["3.5.1.1","3.5.1.2","3.5.1.3"]),
("circuits-and-potential-dividers","Circuits and potential dividers","Electricity",["3.5.1.4","3.5.1.5"]),
("emf-and-internal-resistance","Electromotive force and internal resistance","Electricity",["3.5.1.6"]),
("circular-motion","Circular motion","Further mechanics and thermal physics",["3.6.1.1"]),
("simple-harmonic-motion","Simple harmonic motion, forced vibrations and resonance","Further mechanics and thermal physics",["3.6.1.2","3.6.1.3","3.6.1.4"]),
("thermal-energy-and-ideal-gases","Thermal energy transfer and ideal gases","Further mechanics and thermal physics",["3.6.2.1","3.6.2.2"]),
("kinetic-theory","Molecular kinetic theory","Further mechanics and thermal physics",["3.6.2.3"]),
("gravitational-fields","Gravitational fields and orbits","Fields and their consequences",["3.7.1","3.7.2"]),
("electric-fields","Electric fields and electric potential","Fields and their consequences",["3.7.3"]),
("capacitors","Capacitance and capacitor charge and discharge","Fields and their consequences",["3.7.4"]),
("magnetic-fields","Magnetic flux density and moving charges in a magnetic field","Fields and their consequences",["3.7.5.1","3.7.5.2"]),
("electromagnetic-induction","Electromagnetic induction, alternating currents and transformers","Fields and their consequences",["3.7.5.3","3.7.5.4","3.7.5.5","3.7.5.6"]),
("rutherford-scattering-and-radiation","Rutherford scattering, alpha, beta and gamma radiation","Nuclear physics",["3.8.1.1","3.8.1.2"]),
("radioactive-decay","Radioactive decay, half-life and nuclear instability","Nuclear physics",["3.8.1.3","3.8.1.4"]),
("nuclear-radius","Nuclear radius","Nuclear physics",["3.8.1.5"]),
("mass-energy-and-fission","Mass and energy, binding energy, fission and safety","Nuclear physics",["3.8.1.6","3.8.1.7","3.8.1.8"]),
("telescopes","Telescopes","Option: Astrophysics",["3.9.1"]),
("classification-of-stars","Classification of stars and the HR diagram","Option: Astrophysics",["3.9.2"]),
("cosmology","Cosmology: Doppler effect, Hubble's law, quasars and exoplanets","Option: Astrophysics",["3.9.3"]),
("eye-ear-and-ecg","Physics of the eye, the ear and the ECG","Option: Medical physics",["3.10.1","3.10.2","3.10.3"]),
("medical-imaging","Medical imaging: ultrasound, X-rays, CT, MRI and radionuclides","Option: Medical physics",["3.10.4","3.10.5","3.10.6"]),
("rotational-dynamics","Rotational dynamics","Option: Engineering physics",["3.11.1"]),
("thermodynamics-and-engines","Thermodynamics and engines","Option: Engineering physics",["3.11.2"]),
("discovery-of-the-electron","The discovery of the electron","Option: Turning points in physics",["3.12.1"]),
("wave-particle-duality-history","Wave-particle duality: from Newton to electron microscopes","Option: Turning points in physics",["3.12.2"]),
("special-relativity","Special relativity","Option: Turning points in physics",["3.12.3"]),
("semiconductor-devices-and-signals","Semiconductor devices, analogue and digital signals","Option: Electronics",["3.13.1","3.13.2"]),
("operational-amplifiers","Filters and operational amplifiers","Option: Electronics",["3.13.3","3.13.4"]),
("digital-electronics","Digital signal processing: logic, sequential circuits and astables","Option: Electronics",["3.13.5"]),
("data-communication","Data communication systems and modulation","Option: Electronics",["3.13.6"])]
OPT={"3.9":"Astrophysics","3.10":"Medical physics","3.11":"Engineering physics","3.12":"Turning points in physics","3.13":"Electronics"}
t=open('/home/claude/phys/work/app/data/index.js').read(); QB=json.loads(t[len('window.QB='):-1])
ids=[st['id'] for s in QB['spec'] for st in s['st']]
out=[];used=set()
for slug,name,grp,pre in T:
    st=[i for i in ids if any(i.split('-')[0]==p or i.split('-')[0].startswith(p+'.') for p in pre)]
    used|=set(st)
    sec='.'.join(pre[0].split('.')[:2])
    out.append({"slug":slug,"name":name,"group":grp,"code":", ".join(pre),"option":OPT.get(sec),"statements":st})
miss=[i for i in ids if i not in used]
print(len(out),'topics; unmapped statements',miss)
for o in out:
    if not o['statements']: print('EMPTY',o['slug'])
json.dump(out,open('topics.json','w'),indent=1,ensure_ascii=False)
