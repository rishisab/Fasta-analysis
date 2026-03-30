import sys
import csv


#Input file
Input=sys.argv[1]

sequence={}
seq_id=""
seq=""


#reading csv
with open (Input,"r")as f:
        for line in f:
                line=line.strip()
                if line.startswith(">"):
                        if seq_id:
                                sequence[seq_id]=seq
                        seq_id=line[1:]
                        seq=""
                else:
                        seq +=line.upper()

#reading last seq

        if seq_id:
                sequence[seq_id]=seq

#output save as csv

with open("output.csv","w",newline="") as out:
        writer=csv.writer(out)
        writer.writerow(["ID", "Length", "GC_count", "GC%","Status"])

        for id, sequence in sequence.items():
                length=len(sequence)
                GC_count=sequence.count("G") + sequence.count("C")
                GC_percent= (GC_count / length)*100 if length > 0 else 0
# filter condition (if any)

                if length>35 and GC_percent>40:
                        status="SELECTED"
                else:
                        status="REJECTED"
                writer.writerow([id, length, GC_count, round(GC_percent,2),status])
print("Analysis complete ! output save as csv")
