// OCR Physics A topic groups: modules, badges, where each is examined and the header motif.
export type Group = { key: string; sec: string; n: number; heading: string; where: string; as: boolean; motif: string };
export const GROUPS: Group[] = [
  { key: 'Modules 1 and 2', sec: 'M1–2', n: 1, heading: 'Modules 1 and 2: Practical skills and foundations of physics (AS and A level)', where: 'Every paper: A-level Papers 1, 2 and 3; AS Papers 1 and 2', as: true, motif: 'stats' },
  { key: 'Module 3', sec: 'M3', n: 4, heading: 'Module 3: Forces and motion (AS and A level)', where: 'A-level Paper 1 and Paper 3; AS Papers 1 and 2', as: true, motif: 'mech' },
  { key: 'Module 4', sec: 'M4', n: 5, heading: 'Module 4: Electrons, waves and photons (AS and A level)', where: 'A-level Paper 2 and Paper 3; AS Papers 1 and 2', as: true, motif: 'circuit' },
  { key: 'Module 5', sec: 'M5', n: 6, heading: 'Module 5: Newtonian world and astrophysics (A level only)', where: 'A-level Paper 1 and Paper 3', as: false, motif: 'curve' },
  { key: 'Module 6', sec: 'M6', n: 7, heading: 'Module 6: Particles and medical physics (A level only)', where: 'A-level Paper 2 and Paper 3', as: false, motif: 'field' },
];
export const groupOf = (key: string): Group => GROUPS.find((g) => g.key === key) || GROUPS[0];
export const badgeText = (key: string) => groupOf(key).sec;
export const badgeClass = (key: string) => `badge badge-${groupOf(key).n}`;
export function whereExamined(t: { slug: string; group: string }): string {
  return groupOf(t.group).where;
}
export const motifFor = (t: { slug: string; group: string }) => {
  if (/photo|photons|stars|cosmology|electromagnetic-waves/.test(t.slug)) return 'spectrum';
  if (/nuclear|radioactivity|duality/.test(t.slug)) return 'orbital';
  if (/work-energy|thermal|ideal-gases|electrical-power/.test(t.slug)) return 'energy';
  if (/gravitational|planetary|electric-fields|magnetic|induction/.test(t.slug)) return 'field';
  if (/wave-motion|superposition|stationary|harmonic|medical/.test(t.slug)) return 'trig';
  if (/materials|springs|measurements|practical|quantities/.test(t.slug)) return 'stats';
  return groupOf(t.group).motif;
};
