import json
import pandas as pd

df_h = pd.read_excel('./fixtures/humanInVivo.xlsx')

df_h_vivo = df_h

print("converting samples...")

# convert samples
samples = []

pk = 1
for name in df_h_vivo.columns[0:9]:
    samples.append(
        {
            "model": "genesearch.Sample",
            "pk": pk,
            "fields": {
                "name": name[:-6],
                "species": "Human",
                "status": "Vivo"
            }
        }
    )
    pk = pk + 1

with open('./fixtures/samples.json', 'w') as fp:
    json.dump(samples, fp)

print("converting samples... DONE")

genes_h_vivo = []
genes_m_vivo = []

pk_s = 1
pk_g = 1

# convert genes

print("converting human in vivo genes...")

# convert human in vivo
for name in df_h_vivo.columns[0:9]:
    for gene, row in df_h_vivo[[name]].iterrows():
        genes_h_vivo.append(
            {
                "model": "genesearch.Gene",
                "pk": pk_g,
                "fields": {
                    "symbol": gene,
                    "fpkm": row[name],
                    "sample": pk_s
                }
            }
        )
        pk_g += 1
    pk_s += 1
with open('./fixtures/genes_h_vivo.json', 'w') as fp:
    json.dump(genes_h_vivo, fp)

print("converting human in vivo genes... DONE")

print("Seeding Complete!!")
