status: seeded
type: herb_growth
parent: softsage
region: forest_of_illusions

[summary]
A calm, shade-friendly herb that grows in gentle stages.
Slow enough to feel “earned,” quick enough to be reliable.

[grow_time]
- Typical: 9–14 days to mature (forest conditions)
- Faster if: steady mist + cool shade
- Slower if: dry air or too much sun

[growth_stages]
- sprout (days 1–3)
  - Tiny twin leaves, pale green.
  - Needs soft moisture; hates harsh wind.
- youngleaf (days 4–7)
  - Fuzz begins to form; scent becomes noticeable.
  - Prefers dappled shade near quiet paths.
- mature (days 8–14)
  - Leaves turn velvety with a faint silver cast.
  - Scent settles into “dry-calm” clarity.

[harvest_window]
- Best harvest: early mature (first 2–3 days of maturity)
- After that: still usable, but the calming note fades slightly.

[propagation]
- Re-seeds lightly if left unharvested after maturity.
- Likes mossy soil; does well near study-clearings and sheltered benches.

[notes]
If you want a “focused scene” plant that doesn’t feel magical-overpowered,
softsage is meant to be dependable and gentle.
EOF

# 3) add a tiny launcher link to the existing softsage.md
cat >> "hollowverse/forest_of_illusions/vegetation/forest_floor/herbs/softsage.md" <<'EOF'

[deep_dive]
- growth stages: softsage/growth.md
EOF
