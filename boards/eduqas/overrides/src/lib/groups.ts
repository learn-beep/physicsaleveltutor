// Eduqas Physics topic groups: components, badges, where each topic is examined and the header motif.
export type Group = { key: string; sec: string; n: number; heading: string; where: string; as: boolean; motif: string };
export const GROUPS: Group[] = [
  { key: 'Component 1', sec: 'C1', n: 1, heading: 'Component 1: Newtonian physics (topics 1.1 to 1.8)', where: 'A-level Component 1', as: true, motif: 'mech' },
  { key: 'Component 2', sec: 'C2', n: 2, heading: 'Component 2: Electricity and the universe (topics 2.1 to 2.8)', where: 'A-level Component 2', as: true, motif: 'circuit' },
  { key: 'Component 3', sec: 'C3', n: 3, heading: 'Component 3: Light, nuclei and options (topics 3.1 to 3.10)', where: 'A-level Component 3 Section A', as: true, motif: 'trig' },
  { key: 'Options', sec: 'Opt', n: 9, heading: 'Component 3 Section B: the four options (you answer one)', where: 'A-level Component 3 Section B, if you take this option', as: false, motif: 'spectrum' },
];
export const groupOf = (key: string): Group => GROUPS.find((g) => g.key === key) || GROUPS[0];
export const badgeText = (key: string) => groupOf(key).sec;
export const badgeClass = (key: string) => `badge badge-${groupOf(key).n}`;
// AS content (spec v3): AS Component 1 = 1.1-1.4, 2.5, 2.7, 3.7; AS Component 2 = 2.1-2.3, 3.1-3.5.
const AS1 = ['1.1', '1.2', '1.3', '1.4', '2.5', '2.7', '3.7'];
const AS2 = ['2.1', '2.2', '2.3', '3.1', '3.2', '3.3', '3.4', '3.5'];
export function whereExamined(t: { slug: string; group: string; code?: string }): string {
  const g = groupOf(t.group).where;
  if (t.slug === 'comprehension') return 'A-level Component 1 Section B (20 marks on a printed article)';
  const c = t.code || '';
  if (AS1.includes(c)) return `${g}; AS Component 1${c === '3.7' ? ' (part of the topic)' : ''}`;
  if (AS2.includes(c)) return `${g}; AS Component 2`;
  return `${g} (A level only)`;
}
export const motifFor = (t: { slug: string; group: string }) => {
  if (/photon|laser|radiation-and-stars|refraction/.test(t.slug)) return 'spectrum';
  if (/nuclear|particles/.test(t.slug)) return 'orbital';
  if (/thermal|kinetic|energy/.test(t.slug)) return 'energy';
  if (/fields|magnetic|orbits|induction/.test(t.slug)) return 'field';
  if (/vibrations|waves|wave-properties|alternating/.test(t.slug)) return 'trig';
  if (/solids|comprehension/.test(t.slug)) return 'stats';
  return groupOf(t.group).motif;
};
