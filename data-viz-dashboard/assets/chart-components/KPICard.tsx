import React from 'react'
import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export interface KPICardProps {
  title: string
  value: string | number
  previousValue?: string | number
  change?: number
  changePercent?: number
  unit?: string
  trend?: 'up' | 'down' | 'neutral'
  size?: 'sm' | 'md' | 'lg'
  className?: ClassValue
}

const sizeStyles = {
  sm: {
    container: 'p-4',
    title: 'text-xs',
    value: 'text-xl',
    change: 'text-xs',
  },
  md: {
    container: 'p-6',
    title: 'text-sm',
    value: 'text-2xl',
    change: 'text-sm',
  },
  lg: {
    container: 'p-8',
    title: 'text-base',
    value: 'text-3xl',
    change: 'text-base',
  },
}

const trendColors = {
  up: 'text-green-600 bg-green-50',
  down: 'text-red-600 bg-red-50',
  neutral: 'text-gray-600 bg-gray-50',
}

const trendIcons = {
  up: (
    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 10l7-7m0 0l7 7m-7-7v18" />
    </svg>
  ),
  down: (
    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
    </svg>
  ),
  neutral: (
    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 12H4" />
    </svg>
  ),
}

export function KPICard({
  title,
  value,
  previousValue,
  change,
  changePercent,
  unit,
  trend = 'neutral',
  size = 'md',
  className,
}: KPICardProps) {
  const styles = sizeStyles[size]
  const displayTrend = changePercent !== undefined
    ? changePercent > 0 ? 'up' : changePercent < 0 ? 'down' : 'neutral'
    : trend

  return (
    <div className={twMerge(clsx(
      'bg-white rounded-lg shadow-sm border border-gray-100',
      styles.container,
      className
    ))}>
      <h3 className={clsx('font-medium text-gray-500', styles.title)}>
        {title}
      </h3>

      <div className="mt-2 flex items-baseline gap-2">
        <span className={clsx('font-bold text-gray-900', styles.value)}>
          {typeof value === 'number' ? value.toLocaleString() : value}
        </span>
        {unit && <span className="text-gray-500 text-sm">{unit}</span>}
      </div>

      {changePercent !== undefined && (
        <div className="mt-2 flex items-center gap-2">
          <span className={clsx(
            'inline-flex items-center gap-1 px-2 py-0.5 rounded-full',
            styles.change,
            trendColors[displayTrend]
          )}>
            {trendIcons[displayTrend]}
            <span>{Math.abs(changePercent).toFixed(1)}%</span>
          </span>
          <span className="text-gray-400 text-xs">vs last period</span>
        </div>
      )}
    </div>
  )
}

export default KPICard
