# TERMITE Theory

## 1. Problem

Large collectives can exhibit behaviors not obvious from any individual member.

Examples include:
- consensus,
- polarization,
- clustering,
- distributed search,
- resource concentration,
- oscillation,
- cascading failure,
- collective deadlock.

TERMITE treats topology and local interaction rules as first-class variables.

## 2. Agent state

For agents:

`A = {a_1, ..., a_n}`

each agent has local state:

`x_i(t)`

and neighborhood:

`N_i(t)`.

## 3. Local update

A generic interaction rule:

`x_i(t+1) = F(x_i(t), {x_j(t): j in N_i}, u_i(t))`

Global behavior is:

`X_t = Aggregate({x_i(t)})`

## 4. Emergence score

Let `B_global` be observed collective behavior.

Let `B_individual` be the behavior predicted by independent-agent composition.

Candidate emergence:

`E = dist(B_global, B_individual)`

Higher `E` means the collective cannot be explained well by independent-agent behavior alone.

## 5. Collective coherence

For scalar agent states:

`C = 1 - normalized_dispersion({x_i})`

Higher `C` means stronger agreement or coordinated organization.

## 6. Fragmentation

Partition the interaction graph into connected or behaviorally distinct clusters.

A simple fragmentation index:

`F = number_of_clusters / number_of_agents`

or a modularity-based equivalent.

## 7. Topology sensitivity

Compare outcomes under:
- ring,
- lattice,
- random graph,
- hub-and-spoke,
- clustered networks.

`T = Var(outcome | topology)`

High `T` means the collective behavior depends strongly on network structure.

## 8. Local-to-global amplification

If a local perturbation magnitude is `p0` and collective change is `P_T`:

`A = P_T / (p0 + eps)`

## 9. Attractor stability

Run multiple seeds from nearby initial conditions.

If trajectories converge to similar collective states, the attractor is more stable.

## 10. EFMW interpretation

The EFMW-inspired element is recursive relational structure across agents, neighborhoods, topology, and time.

The target is not one agent's output.

It is the **emergent field formed by repeated local interactions**.

## 11. Falsifiable prediction

TERMITE should add value when:
- topology matters,
- local rules interact,
- collective modes emerge,
- simple agent averaging fails.

If standard network science and multi-agent metrics capture the same behavior, TERMITE's extra formulation is unnecessary.
