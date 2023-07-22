# Calculate the future value of
# $100,000 invested
# at 8% per year for 10 years
import numpy_financial as npf

fv = npf.fv(rate=0.08, nper=10, pmt=0, pv=-100000)

print('${:,.2f}'.format(fv))
