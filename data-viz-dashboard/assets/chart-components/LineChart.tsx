import React from 'react'
import {
  LineChart as RechartsLineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts'
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export interface LineChartProps {
  data: Array<Record<string, string | number>>
  xKey: string
  yKeys: string[]
  height?: number
  colors?: string[]
  showGrid?: boolean
  showLegend?: boolean
  showDots?: boolean
  smooth?: boolean
  className?: ClassValue
}

const defaultColors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6']

export function LineChart({
  data,
  xKey,
  yKeys,
  height = 300,
  colors = defaultColors,
  showGrid = true,
  showLegend = true,
  showDots = true,
  smooth = false,
  className,
}: LineChartProps) {
  return (
    <div className={twMerge(clsx('w-full', className))} style={{ height }}>
      <ResponsiveContainer width="100%" height="100%">
        <RechartsLineChart
          data={data}
          margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
        >
          {showGrid && <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />}
          <XAxis
            dataKey={xKey}
            tick={{ fill: '#6B7280', fontSize: 12 }}
          />
          <YAxis tick={{ fill: '#6B7280', fontSize: 12 }} />
          <Tooltip
            contentStyle={{
              backgroundColor: '#fff',
              border: '1px solid #E5E7EB',
              borderRadius: '8px',
              boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)',
            }}
          />
          {showLegend && <Legend />}
          {yKeys.map((key, index) => (
            <Line
              key={key}
              type={smooth ? 'monotone' : 'linear'}
              dataKey={key}
              stroke={colors[index % colors.length]}
              strokeWidth={2}
              dot={showDots ? { fill: colors[index % colors.length], r: 4 } : false}
              activeDot={{ r: 6 }}
            />
          ))}
        </RechartsLineChart>
      </ResponsiveContainer>
    </div>
  )
}

export default LineChart
