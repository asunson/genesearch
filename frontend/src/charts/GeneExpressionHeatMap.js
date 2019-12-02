import React from 'react';
import { ResponsiveHeatMap } from '@nivo/heatmap';

export const GeneExpressionHeatMap = ({ data, chartSettings }) => (
    <ResponsiveHeatMap
        data={data}
        {...chartSettings}
    />
)