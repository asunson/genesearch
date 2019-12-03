import React from 'react';
import '../styles/App.scss';
import { GeneExpressionHeatMap } from '../charts/GeneExpressionHeatMap';
import groupBy from 'lodash.groupby';
import { Paper } from '@material-ui/core';

export const ResultsPage = ({ geneResults, samples }) => {
    console.log(geneResults)
    const sampleNames = samples.filter(sample => sample.status === "Vivo" && sample.species === "Human").map(sample => sample.name)

    const aggregatedGenes = groupBy(geneResults.filter(geneResult => sampleNames.includes(geneResult.sample_name)), 'symbol');

    const expressionData = Object.keys(aggregatedGenes).map(
        (geneName) => {
            let geneExpressionData = { "Gene": geneName }
            aggregatedGenes[geneName].forEach(
                (gene) => {
                    geneExpressionData[gene.sample_name] = parseFloat(Math.log2(gene.fpkm).toFixed(2))
                }
            )
            return geneExpressionData
        }
    )

    const chartSettings = {
        keys: [
            "BC3t parental-1",
            "BC3t parental-2",
            "BC3t parental-3",
            "BC3t shCCL2-1",
            "BC3t shCCL2-2",
            "BC3t shCCL2-3",
            "BC3t GFP-1",
            "BC3t GFP-2",
            "BC3t GFP-3"
        ],
        indexBy: "Gene",
        margin: { top: 100, right: 80, bottom: 60, left: 80 },
        axisTop: {
            orient: 'top',
            tickSize: 5,
            tickPadding: 5,
            tickRotation: -45,
            legend: 'Sample',
            legendOffset: -75,
            legendPosition: 'middle'
        },
        axisRight: null,
        axisBottom: null,
        axisLeft: {
            orient: 'left',
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: 'Gene',
            legendPosition: 'middle',
            legendOffset: -75
        },
        tooltipFormat: (value) => `${Math.pow(2, value).toFixed(2)} FPKM`
    }
    const height = `${200 + Object.keys(aggregatedGenes).length * 40}px`

    return (
        <Paper className="paper-results" elevation={3}>
            <div style={{ height: height }}>
                <GeneExpressionHeatMap
                    data={expressionData}
                    chartSettings={chartSettings}
                />
            </div>
        </Paper>
    )
};