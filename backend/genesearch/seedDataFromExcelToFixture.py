import json
import pandas as pd

df_h = pd.read_excel('./fixtures/Fall 2019 BC3 RNASeq FPKM inVitro and inVivo HUMAN.xlsx', sheet_name = [0, 1, 2])
df_m = pd.read_excel('./fixtures/Fall 2019 BC3 RNASeq FPKM inVitro and inVivo MOUSE.xlsx', sheet_name = [0, 1, 2])

df_h_vivo = df_h[2]
df_h_vitro = df_h[1]

df_m_vivo = df_m[2]
df_m_vitro = df_m[1]

print("converting samples...")

# convert samples
samples = []

pk = 1
for name in df_h_vivo.columns[0:5]:
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
for name in df_h_vitro.columns[0:3]:
    samples.append(
        {
            "model": "genesearch.Sample",
            "pk": pk,
            "fields": {
                "name": name[:-6],
                "species": "Human",
                "status": "Vitro"
            }
        }
    )
    pk = pk + 1
for name in df_m_vivo.columns[0:5]:
    samples.append(
        {
            "model": "genesearch.Sample",
            "pk": pk,
            "fields": {
                "name": name[:-6],
                "species": "Mouse",
                "status": "Vivo"
            }
        }
    )
    pk = pk + 1
for name in df_m_vitro.columns[0:3]:
    samples.append(
        {
            "model": "genesearch.Sample",
            "pk": pk,
            "fields": {
                "name": name[:-6],
                "species": "Mouse",
                "status": "Vitro"
            }
        }
    )
    pk = pk + 1
    
with open('./fixtures/samples.json', 'w') as fp:
    json.dump(samples, fp)

print("converting samples... DONE")

genes_h_vivo = []
genes_h_vitro = []
genes_m_vivo = []
genes_m_vitro = []

pk_s = 1
pk_g = 1

# convert genes

print("converting human in vivo genes...")

# convert human in vivo
for name in df_h_vivo.columns[0:5]:
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
print("converting human in vitro genes...")

# convert human in vitro
for name in df_h_vitro.columns[0:3]:
    for gene, row in df_h_vitro[[name]].iterrows():
        genes_h_vitro.append(
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
with open('./fixtures/genes_h_vitro.json', 'w') as fp:
    json.dump(genes_h_vitro, fp)

print("converting human in vitro genes... DONE")
print("converting mouse in vivo genes...")

# convert mouse in vivo
for name in df_m_vivo.columns[0:5]:
    for gene, row in df_m_vivo[[name]].iterrows():
        genes_m_vivo.append(
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
with open('./fixtures/genes_m_vivo.json', 'w') as fp:
    json.dump(genes_m_vivo, fp)

print("converting mouse in vivo genes... DONE")
print("converting mouse in vitro genes...")

# convert mouse in vitro
for name in df_m_vitro.columns[0:3]:
    for gene, row in df_m_vitro[[name]].iterrows():
        genes_m_vitro.append(
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
with open('./fixtures/genes_m_vitro.json', 'w') as fp:
    json.dump(genes_m_vitro, fp)

print("converting mouse in vitro genes... DONE")

print("Seeding Complete!!")
