# Multi-Agent Model

## Agent schema

```json
{
  "id": "a17",
  "state": 0.62,
  "susceptibility": 0.8,
  "bias": 0.1
}
```

## Edge schema

```json
{
  "source": "a17",
  "target": "a21",
  "weight": 0.4
}
```

## Reference update

For weighted-neighbor averaging:

`x_i(t+1) = (1-alpha_i)*x_i(t) + alpha_i*weighted_neighbor_mean`

Optional noise may be added.

## Collective outputs

- mean state
- dispersion
- coherence
- cluster count
- convergence rate
- topology sensitivity

## Emergence comparison

Compare against an ablated independent-agent baseline in which neighbor effects are removed.

## Perturbation test

Inject a bounded change into one agent and measure downstream collective shift.
