# parasite_count_converter
Python script run through command line to convert between different P. falciparum parasitaemia units

## Background
Intended to convert between parasitaemia measurements commonly used in the field for the malaria parasite Plasmodium falciparum.
Converts between three possible units: parasites per 200 white blood cells (WBC), parasites per ul blood, or proportion of red blood cells (RBCs) infected.
The user defines the input unit type (options: "WBC200", "parasites_ul", or "pcnt_RBC", for the above units, respectively) and the parasitaemia value for that unit. The script will print in the terminal the conversion to the other two parasitaemia unit types.

Default assumptions are 10E+9 WBC/L and 3E+12 RBC/L. These can be changed.
Note: while 8x10^9 WBC/L is commonly used for this conversion, I have used 10x10^9/L by default based on this paper: https://malariajournal.biomedcentral.com/articles/10.1186/1475-2875-11-238. The authors find that 10x10^9/L more accurately reflects children under 5 in Ghana. 
For greater accuracy, actual WBC counts for the patient would be required. This is only an approximation.

## Mandatory inputs:
 -i or --input. The starting unit [options: "WBC200", "parasites_ul", or "pcnt_RBC"]
 -c or --count. The parasitaemia value (numeric)
 
## Optional inputs:
 -w or --WBC_per_L. The WBC/L value. Defaults to 10000000000
 -r or --RBC_per_L. The RBC/L value. Defaults to 3E+12

## Example command line:
python3 PATH/pf_parasite_converter.py -i "WBC200" -c 1000

Expected output from above command would be:
Parasite count converter v1.0
Starting input: 1000.0 parasites per 200 WBC
Assumptions: WBC/L: 10000000000.0 | RBC/L: 3000000000000.0
Calculated outputs:
Parasites per 200 WBC: 1000.0
Parasites per ul blood: 50000.0
Proportion of RBCs infected: 0.0167

Note the proportion of infected RBCs would need to be multiplied by 100 for percentage of RBCs infected.
