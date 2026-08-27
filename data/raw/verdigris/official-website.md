# Verdigris - Official Website

Source: https://www.verdigris.co/
Fetched: 2026-08-27

Electrical Ground Truth for AI Data Centers.

Standard monitoring samples once a second. Failures move in milliseconds. Verdigris reads 8,000 samples a second (8 kHz vs 1 Hz), catching them before alarms fire and freeing the 15 to 25 percent of capacity that slow data leaves stranded.

Stats:
- 2+ GW peak demand monitored
- 20M+ sq ft global deployments
- 10K+ power equipment monitored

## Technology: 8 kHz waveform analysis

A 200 ms harmonic spike from a degrading rectifier looks like a normal reading at 1 Hz. At 8 kHz, the same event produces 1,600 data points - enough to identify the failure signature.

Continuous waveform analysis catches degradation that threshold-based alarms structurally cannot. A degrading rectifier shifts the ratio of its 5th and 7th harmonics weeks before any threshold trips.

## Case study: T-Mobile

T-Mobile deployed Verdigris across 800+ UPS rectifiers. 4% showed active electrical degradation; standard BMS alarms had fired on zero of them. Continuous waveform analysis caught the harmonic shifts that precede equipment failure, giving 21 days of runway to schedule replacement before any breaker opened, and a 5-month payback. $1.3M to $3M projected 3-year value, 6:1 ROI. Caught 21 days before failure.

## Capacity optimization

Per-circuit data reveals capacity that aggregate metering hides. A Fortune 50 NYC data center cut chiller energy 19% once it could act on validated operating limits instead of conservative nameplate derating. Verdigris validates a measured-safe operating envelope from physics that reaches 92% of nameplate, recovering 15 to 25% more capacity per circuit while holding an 8% safety margin.

Full power chain measured: 13 nodes from main switchgear through every sub-panel and circuit, all measured continuously. A fault stays visible at every node above it.
