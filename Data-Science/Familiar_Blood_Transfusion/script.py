from familiar import *
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# Get data from 'familiar' library
vein_pack_lifespans = lifespans(package='vein')
# print(vein_pack_lifespans)

# Use ttest to see if the data is significantly different from the expected
# null hypothesis: the vein pack does not have any affect on living 71 years
tstat, vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(vein_pack_test)

# true: reject null hypothesis
if vein_pack_test < 0.05:
  print("\nThe Vein Pack is Proven to Make You Live Longer!")
else:
  print("\nThe Vein Pack is Probably Good For You Somehow!")
  
# Get data from artery pack in 'familiar' library
artery_pack_lifespans = lifespans(package='artery')
#print(artery_pack_lifespans)

# Can we prove that the artery pack makes a significant impact on lifespan in comparison to vein?
# null hypothesis: the artery pack has no significant impact on lifespan compared to that of the vein pack
tstats, package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(package_comparison_results)

# false: artery package doesn't increase lifespan
if package_comparison_results < 0.05:
  print("the Artery Package guarantees even stronger results!")
else:
  print("The Artery Package is good too... Please clap...")

# So it doesn't increase lifespan, but what about some other health benefits?
# Get the iron contingency table from the familiar function
# Then we use the chi squared test
iron_contingency_table = iron_counts_for_package()
tstat, iron_pvalue, dof, freq = chi2_contingency(iron_contingency_table)
print(iron_pvalue)

if iron_pvalue < 0.05:
  print("Artery Package is proven to change your iron count, and studies show that it is healhier!")
else:
  print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
