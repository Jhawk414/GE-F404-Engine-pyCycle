# GE-F404-Engine-pyCycle
## Purpose:
Models/Matches performance of GE's F404-GE-402 engine to publicly available data at both On-Design & Off-Design (OD) conditions using pyCycle.

## Status:
In-progress as of 15 July '25 (started June '25). I'm currently working to balance the bypass duct- and LPT- exit pressures (extraction ratio "ER").

### Strategy:
Adjust the design point cycle parameters to achieve the desired OD estimated thrust. Unclassified data is used merely to _estimate_ the design parameters $(OPR,\ BPR, \pi_{\text{Fan}},\ \pi_{HPT/LPT})$, which are then tweaked to achieve the desired OD thrust.

While the cruise condition ("CRZ") is typically chosen as a turbofan's design point, this project initially choses the sea-level static (SLS) as the design point since for simplicity since most unclassified data exists exists at SLS conditions (makes performance matching easier). The OD condition is thus assumed to be CRZ.

The primary OD performance metric, thrust, is estimated using the thrust lapse equations (_Mattingly, 2018_):

if $$\ \theta_0 \leq \theta_{0\text{break}} \quad \Longrightarrow \quad \alpha = 0.6\delta_0 $$

if $$\ \theta_0 > \theta_{0\text{break}} \quad \Longrightarrow \quad \alpha = 0.6\delta_0 \left(1 - 2.5 \frac{\theta_0 - \theta_{0\text{break}}}{\theta_0} \right)$$

where:

$$\alpha = \frac{T_{OD}}{T_{SL}} = \frac{\text{Installed Thrust}}{\text{Thrust}_{SLS}}$$

$$\delta_0 = \frac{P_{t0}}{P_{\text{std}}}$$

$$\theta_0 = \frac{T_{t0}}{T_{\text{std}}}$$

$$\text{Thrust}_{SLS} = 17700\ \text{lbf}$$

## References

Mattingly, Jack D., William H. Heiser, Keith M. Boyer, Brenda A. Haven, and David T. Pratt. _Aircraft Engine Design_. 3rd Edition. Reston, VA: American Institute of Aeronautics and Astronautics, Inc., 2018. 
