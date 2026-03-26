import React from 'react'
import {
  FunnelChart as RechartsFunnelChart,
  Funnel,
  LabelList,
  ResponsiveContainer,
  Cell,
} from 'recharts'
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export interface FunnelData {
  name: string
  value: number
  fill?: string
}

export interface FunnelChartProps {
  data: FunnelData[]
  height?: number
  colors?: string[]
  className?: ClassValue
}

const defaultColors = ['#3B82F6', '#60A5FA', '#93C5FD', '#BFDBFE', '#DBEAFE']

export function FunnelChart({
  data,
  height = 300,
  colors = defaultColors,
  className,
}: FunnelChartProps) {
  return (
    <div className={twMerge(clsx('w-full', className))} style={{ height }}>
      <ResponsiveContainer width="100%" height="100%">
        <RechartsFunnelChart>
          <Funnel
            dataKey="value"
            data={data}
            isAnimationActive
          >
            <LabelList
              position="right"
              fill="#374151"
              stroke="none"
              dataKey="name"
            />
            {data.map((entry, index) => (
              <Cell
                key={`cell-${index}`}
                fill={entry.fill || colors[index % colors.length]}
              />
            ))}
          </Funnel>
        </RechartsFunnelChart>
      </ResponsiveContainer>
    </div>
  )
}

export default FunnelChart
