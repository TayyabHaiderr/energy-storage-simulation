# Energy Storage Performance Simulation
# Based on a linear degradation model from independent research

# -----------------------
# Input parameters
# -----------------------

eta_0 = 0.85            # Initial round-trip efficiency
d_eta = 0.015           # Annual efficiency degradation (per year)
lifetime = 15           # System lifetime (years)
capacity_kwh = 1000     # Rated energy capacity (kWh)
cycles_per_year = 300   # Annual charge-discharge cycles
depth_of_discharge = 1.0

# -----------------------
# Simulation
# -----------------------

print("Year | Efficiency | Energy Delivered (kWh/year)")
print("-----------------------------------------------")

for year in range(lifetime + 1):
    eta_t = max(0, eta_0 - d_eta * year)
    energy_delivered = (
        cycles_per_year *
        capacity_kwh *
        depth_of_discharge *
        eta_t
    )
    print(
        f"{year:>4} | "
        f"{eta_t:.3f}      | "
        f"{energy_delivered:,.0f}"
    )
