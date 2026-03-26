import React from 'react'
import {
  ScatterChart as RechartsScatterChart,
  Scatter,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  ZAxis,
} from 'recharts'
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export interface ScatterChartProps {
  data: Array<{ x: number; y: number; z?: number; name?: string }>
  height?: number
  color?: string
  showGrid?: boolean
  bubble?: boolean
  className?: ClassValue
}

export function ScatterChart({
  data,
  height = 300,
  color = '#3B82F6',
  showGrid = true,
  bubble = false,
  className,
}: ScatterChartProps) {
  return (
    <div className={twMerge(clsx('w-full', className))} style={{ height }}>
      <ResponsiveContainer width="100%" height="100%">
        <RechartsScatterChart margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
          {showGrid && <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />}
          <XAxis
            type="number"
            dataKey="x"
            name="x"
            tick={{ fill: '#6B7280', fontSize: 12 }}
          />
          <YAxis
            type="number"
            dataKey="y"
            name="y"
            tick={{ fill: '#6B7280', fontSize: 12 }}
          />
          {bubble && <ZAxis type="number" dataKey="z" range={[50, 400]} />}
          <Tooltip
            cursor={{ strokeDasharray: '3 3' }}
            contentStyle={{
              backgroundColor: '#fff',
              border: '1px solid #E5E7EB',
              borderRadius: '8px',
              boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
            }}
          />
          <Scatter
            name="Data"
            data={data}
            fill={color}
          />
        </RechartsScatterChart>
      </ResponsiveContainer>
    </div>
  )
}

export default ScatterChart
