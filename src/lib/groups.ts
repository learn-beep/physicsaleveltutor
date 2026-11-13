// AQA Physics topic groups: section code, short badge, where each is examined and the header motif.
export type Group = { key: string; sec: string; n: number; heading: string; where: string; as: boolean; motif: string };
export const GROUPS: Group[] = [
  { key: 'Measurements', sec: '3.1', n: 1, heading: '3.1 Measurements and their errors (AS and A level)', where: 'A-level Paper 1 and Paper 3 Section A; AS Papers 1 and 2', as: true, motif: 'stats' },
  { key: 'Particles and radiation', sec: '3.2', n: 2, heading: '3.2 Particles and radiation (AS and A level)', where: 'A-level Paper 1; AS Papers 1 and 2', as: true, motif: 'orbital' },
  { key: 'Waves', sec: '3.3', n: 3, heading: '3.3 Waves (AS and A level)', where: 'A-level Paper 1; AS Papers 1 and 2', as: true, motif: 'trig' },
  { key: 'Mechanics and materials', sec: '3.4', n: 4, heading: '3.4 Mechanics and materials (AS and A level)', where: 'A-level Paper 1; AS Papers 1 and 2', as: true, motif: 'mech' },
  { key: 'Electricity', sec: '3.5', n: 5, heading: '3.5 Electricity (AS and A level)', where: 'A-level Paper 1; AS Papers 1 and 2', as: true, motif: 'circuit' },
  { key: 'Further mechanics and thermal physics', sec: '3.6', n: 6, heading: '3.6 Further mechanics and thermal physics (A level only)', where: 'A-level Paper 1 (periodic motion) or Paper 2 (thermal physics)', as: false, motif: 'curve' },
  { key: 'Fields and their consequences', sec: '3.7', n: 7, heading: '3.7 Fields and their consequences (A level only)', where: 'A-level Paper 2', as: false, motif: 'field' },
  { key: 'Nuclear physics', sec: '3.8', n: 8, heading: '3.8 Nuclear physics (A level only)', where: 'A-level Paper 2', as: false, motif: 'orbital' },
  { key: 'Option: Astrophysics', sec: '3.9', n: 9, heading: 'Option 3.9 Astrophysics (Paper 3 Section B)', where: 'A-level Paper 3 Section B, if you take the Astrophysics option', as: false, motif: 'spectrum' },
  { key: 'Option: Medical physics', sec: '3.10', n: 9, heading: 'Option 3.10 Medical physics (Paper 3 Section B)', where: 'A-level Paper 3 Section B, if you take the Medical physics option', as: false, motif: 'curve' },
  { key: 'Option: Engineering physics', sec: '3.11', n: 9, heading: 'Option 3.11 Engineering physics (Paper 3 Section B)', where: 'A-level Paper 3 Section B, if you take the Engineering physics option', as: false, motif: 'energy' },
  { key: 'Option: Turning points in physics', sec: '3.12', n: 9, heading: 'Option 3.12 Turning points in physics (Paper 3 Section B)', where: 'A-level Paper 3 Section B, if you take the Turning points option', as: false, motif: 'orbital' },
  { key: 'Option: Electronics', sec: '3.13', n: 9, heading: 'Option 3.13 Electronics (Paper 3 Section B)', where: 'A-level Paper 3 Section B, if you take the Electronics option', as: false, motif: 'circuit' },
];
export const groupOf = (key: string): Group => GROUPS.find((g) => g.key === key) || GROUPS[0];
export const badgeText = (key: string) => groupOf(key).sec;
export const badgeClass = (key: string) => `badge badge-${groupOf(key).n}`;
// Topic-level override: periodic motion is Paper 1, thermal physics Paper 2.
export function whereExamined(t: { slug: string; group: string }): string {
  if (['circular-motion', 'simple-harmonic-motion'].includes(t.slug)) return 'A-level Paper 1 (and Paper 3 Section A for practical work)';
  if (['thermal-energy-and-ideal-gases', 'kinetic-theory'].includes(t.slug)) return 'A-level Paper 2 (and Paper 3 Section A for practical work)';
  return groupOf(t.group).where;
}
export const motifFor = (t: { slug: string; group: string }) => {
  if (t.slug.includes('photoelectric') || t.slug.includes('energy-levels')) return 'spectrum';
  if (t.slug.includes('materials')) return 'stats';
  if (t.slug.includes('work-energy') || t.slug.includes('thermal') || t.slug.includes('kinetic')) return 'energy';
  if (t.slug.includes('gravitational') || t.slug.includes('electric-fields') || t.slug.includes('magnetic')) return 'field';
  return groupOf(t.group).motif;
};
