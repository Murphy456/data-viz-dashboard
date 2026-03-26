import React from 'react'
import {
  BarChart as RechartsBarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts'
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export interface BarChartProps {
  data: Array<Record<string, string | number>>
  xKey: string
  yKeys: string[]
  height?: number
  colors?: string[]
  showGrid?: boolean
  showLegend?: boolean
  variant?: 'vertical' | 'horizontal' | 'stacked' | 'grouped'
  className?: ClassValue
}

const defaultColors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6']

export function BarChart({
  data,
  xKey,
  yKeys,
  height = 300,
  colors = defaultColors,
  showGrid = true,
  showLegend = true,
  variant = 'vertical',
  className,
}: BarChartProps) {
  const isHorizontal = variant === 'horizontal'
  const isStacked = variant === 'stacked'

  return (
    <div className={twMerge(clsx('w-full', className))} style={{ height }}>
      <ResponsiveContainer width="100%" height="100%">
        <RechartsBarChart
          data={data}
          layout={isHorizontal ? 'vertical' : 'horizontal'}
          margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
        >
          {showGrid && <CartesianGrid strokeDasharray="3 3" stroke="#E5E7EB" />}
          {isHorizontal ? (
            <>
              <XAxis type="number" tick={{ fill: '#6B7280', fontSize: 12 }} />
              <YAxis
                dataKey={xKey}
                type="category"
                tick={{ fill: '#6B7280', fontSize: 12 }}
                width={80}
              />
            </>
          ) : (
            <>
              <XAxis
                dataKey={xKey}
                tick={{ fill: '#6B7280', fontSize: 12 }}
              />
              <YAxis tick={{ fill: '#6B7280', fontSize: 12 }} />
            </>
          )}
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
            <Bar
              key={key}
              dataKey={key}
              fill={colors[index % colors.length]}
              stackId={isStacked ? 'stack' : undefined}
              radius={[4, 4, 0, 0]}
            />
          ))}
        </RechartsBarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default BarChart
