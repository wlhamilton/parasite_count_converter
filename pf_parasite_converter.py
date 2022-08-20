########## Parasite count converter v1.0
## Will Hamilton
#
# Script to convert between different measurements of parasitaemia
# Intended for the malaria parasite Plasmodium falciparum
# Optional units: parasites per 200 white blood cells (WBC), parasites per ul blood, or proportion infected RBCs
# The user defines the input unit type (options: "WBC200", "parasites_ul", or "pcnt_RBC") and the value
# Default assumptions are 10000000000 WBC/L and 3E+12 RBC/L. These can be changed.
#
# Mandatory inputs:
#   -i or --input. The starting unit [options: "WBC200", "parasites_ul", or "pcnt_RBC"]
#   -c or --count. The parasitaemia value (numeric)
# Optional inputs:
#   -w or --WBC_per_L. The WBC/L value. Defaults to 10000000000
#   -r or --RBC_per_L. The RBC/L value. Defaults to 3E+12
#
# Example command line:
# python3 PATH/pf_parasite_converter.py -i "WBC200" -c 1000
#
#
#
# Import packages
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import warnings
warnings.simplefilter("ignore")

# Parse command line arguments
parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-i", "--input", default="WBC200", help="Options: WBC200, parasites_ul, or pcnt_RBC")
parser.add_argument("-c", "--count", help="Parasitaemia value")
parser.add_argument("-w", "--WBC_per_L", default=10000000000, help="Numeric, WBC/L")
parser.add_argument("-r", "--RBC_per_L", default=3E+12, help="Numeric, RBC/L")
args = vars(parser.parse_args())

# Set up parameters
input = args["input"]
count = float(args["count"])
WBC_per_L = float(args["WBC_per_L"])
RBC_per_L = float(args["RBC_per_L"])

# Calculate conversions starting from parasites per 200 WBC
if input == "WBC200":
   Input = "parasites per 200 WBC"
   Parasites_per_200WBC = round(count,0)
   Parasites_per_ul_blood = round((count/200)*WBC_per_L/1000000,-2)
   Parasitaemia_pcnt_RBCs = round(Parasites_per_ul_blood/(RBC_per_L/1000000),4)
   print("Parasite count converter v1.0")
   print("Starting input:",count,Input)
   print("Assumptions:","WBC/L:",WBC_per_L,"| RBC/L:",RBC_per_L)
   print("Calculated outputs:")
   print("Parasites per 200 WBC:",Parasites_per_200WBC)
   print("Parasites per ul blood:",Parasites_per_ul_blood)
   print("Proportion of RBCs infected:",Parasitaemia_pcnt_RBCs)

# Calculate conversions starting from parasites per ul blood
elif input == "parasites_ul":
   Input = "parasites per ul blood"
   Parasites_per_ul_blood = round(count,-2)
   Parasites_per_200WBC = round(count/(WBC_per_L/1000000)*200,0)
   Parasitaemia_pcnt_RBCs = round(count/(RBC_per_L/1000000),4)
   print("Parasite count converter v1.0")
   print("Starting input:",count,Input)
   print("Assumptions:","WBC/L:",WBC_per_L,"| RBC/L:",RBC_per_L)
   print("Calculated outputs:")
   print("Parasites per 200 WBC:",Parasites_per_200WBC)
   print("Parasites per ul blood:",Parasites_per_ul_blood)
   print("Proportion of RBCs infected:",Parasitaemia_pcnt_RBCs)

# Calculate conversions starting from proportion of RBCs infected
elif input == "pcnt_RBC":
   Input = "proportion of RBCs infected"
   Parasitaemia_pcnt_RBCs = round(count,4)
   Parasites_per_ul_blood = round(count*(RBC_per_L/1000000),-2)
   Parasites_per_200WBC = round(Parasites_per_ul_blood/(WBC_per_L/1000000)*200,0)
   print("Parasite count converter v1.0")
   print("Starting input:",count,Input)
   print("Assumptions:","WBC/L:",WBC_per_L,"| RBC/L:",RBC_per_L)
   print("Calculated outputs:")
   print("Parasites per 200 WBC:",Parasites_per_200WBC)
   print("Parasites per ul blood:",Parasites_per_ul_blood)
   print("Proportion of RBCs infected:",Parasitaemia_pcnt_RBCs)

else:
   print("Oops. Input format not recognised, check help")

##### End #####