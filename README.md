# GE-F404-Engine-pyCycle
# Purpose: Models/Matches performance of GE's F404-GE-402 engine to publicly available data at both On-Design & Off-Design conditions using pyCycle.

# Status: In-progress as of 15 July '25 (started June '25). I'm currently working to balance the bypass duct- and LPT- exit pressures (extraction ratio).

## Strategy:
Adjust the design point (SLS) cycle parameters to achieve the desired off-design point (cruise; "CRZ") estimated thrust. Unclassified data is used merely to _estimate_ the design parameters $(OPR, \pi_F, BPR, \pi_{HPT/LPT})$, which are then tweaked to achieve the desired CRZ thrust.

The CRZ thrust is estimated using the thrust lapse equations (_Mattingly, 2018_);
$$\theta_0 \leq \theta_{0\text{break}} \quad \alpha = 0.6\delta_0 $$

$$\theta_0 > \theta_{0\text{break}} \quad \alpha = 0.6\delta_0 \left(1 - 2.5 \frac{\theta_0 - \theta_{0\text{break}}}{\theta_0} \right)$$

where:

$$\alpha = \frac{T}{T_{SL}} = \frac{\text{Installed Thrust}}{\text{Thrust}_{SLS}}$$
