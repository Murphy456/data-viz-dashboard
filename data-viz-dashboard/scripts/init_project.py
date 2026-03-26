#!/usr/bin/env python3
"""
Initialize a React + Vite + Recharts + Tailwind project for data visualization dashboard.
"""

import argparse
import json
import os
import sys
from pathlib import Path


def create_package_json(project_name: str) -> dict:
    return {
        "name": project_name,
        "version": "0.1.0",
        "type": "module",
        "scripts": {
            "dev": "vite",
            "build": "tsc -b && vite build",
            "lint": "eslint .",
            "preview": "vite preview",
            "test": "vitest run",
            "test:watch": "vitest",
            "test:coverage": "vitest run --coverage"
        },
        "dependencies": {
            "react": "^18.3.1",
            "react-dom": "^18.3.1",
            "recharts": "^2.15.0",
            "zustand": "^5.0.0",
            "clsx": "^2.1.0",
            "tailwind-merge": "^2.6.0"
        },
        "devDependencies": {
            "@eslint/js": "^9.0.0",
            "@testing-library/jest-dom": "^6.6.0",
            "@testing-library/react": "^16.1.0",
            "@types/react": "^18.3.0",
            "@types/react-dom": "^18.3.0",
            "@vitejs/plugin-react": "^4.3.0",
            "autoprefixer": "^10.4.0",
            "eslint": "^9.0.0",
            "eslint-plugin-react-hooks": "^5.0.0",
            "eslint-plugin-react-refresh": "^0.4.0",
            "globals": "^15.0.0",
            "jsdom": "^25.0.0",
            "postcss": "^8.4.0",
            "tailwindcss": "^3.4.0",
            "typescript": "~5.7.0",
            "typescript-eslint": "^8.0.0",
            "vite": "^6.0.0",
            "vitest": "^3.0.0",
            "@vitest/coverage-v8": "^3.0.0"
        }
    }


def create_tsconfig() -> dict:
    return {
        "compilerOptions": {
            "target": "ES2020",
            "useDefineForClassFields": True,
            "lib": ["ES2020", "DOM", "DOM.Iterable"],
            "module": "ESNext",
            "skipLibCheck": True,
            "moduleResolution": "bundler",
            "allowImportingTsExtensions": True,
            "isolatedModules": True,
            "moduleDetection": "force",
            "noEmit": True,
            "jsx": "react-jsx",
            "strict": True,
            "noUnusedLocals": True,
            "noUnusedParameters": True,
            "noFallthroughCasesInSwitch": True,
            "noUncheckedSideEffectImports": True,
            "baseUrl": ".",
            "paths": {
                "@/*": ["./src/*"]
            }
        },
        "include": ["src"]
    }


def create_vite_config() -> str:
    return '''import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
'''


def create_tailwind_config() -> str:
    return '''/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        },
      },
    },
  },
  plugins: [],
}
'''


def create_postcss_config() -> str:
    return '''export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
'''


def create_index_html(project_name: str) -> str:
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{project_name}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
'''


def create_main_tsx() -> str:
    return '''import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
'''


def create_index_css() -> str:
    return '''@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
  line-height: 1.5;
  font-weight: 400;
  color: #213547;
  background-color: #f8fafc;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body {
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
}
'''


def create_app_tsx() -> str:
    return '''import { useState } from 'react'

function App() {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <header className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900">Data Dashboard</h1>
        <p className="text-gray-600 mt-2">Your visualization will appear here</p>
      </header>

      <main className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* KPI Cards */}
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-500">Total Revenue</h3>
          <p className="text-2xl font-bold text-gray-900 mt-2">$0</p>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-500">Conversion Rate</h3>
          <p className="text-2xl font-bold text-gray-900 mt-2">0%</p>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-sm font-medium text-gray-500">Active Users</h3>
          <p className="text-2xl font-bold text-gray-900 mt-2">0</p>
        </div>

        {/* Chart Placeholder */}
        <div className="col-span-full bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-gray-900 mb-4">Chart Area</h3>
          <div className="h-64 flex items-center justify-center border-2 border-dashed border-gray-300 rounded">
            <p className="text-gray-500">Chart will be rendered here</p>
          </div>
        </div>
      </main>
    </div>
  )
}

export default App
'''


def create_vitest_config() -> str:
    return '''import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: ['./src/test/setup.ts'],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: [
        'node_modules/',
        'src/test/',
      ],
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
})
'''


def create_test_setup() -> str:
    return '''import '@testing-library/jest-dom'
'''


def create_types_template() -> str:
    return '''// Data types for the dashboard

export interface MetricData {
  name: string
  value: number
  previousValue?: number
  change?: number
  changePercent?: number
}

export interface TimeSeriesData {
  date: string
  value: number
  [key: string]: string | number
}

export interface CategoricalData {
  category: string
  value: number
  color?: string
}

export interface DashboardConfig {
  title: string
  refreshInterval?: number
  theme?: 'light' | 'dark'
}
'''


def create_readme(project_name: str) -> str:
    return f'''# {project_name}

A data visualization dashboard built with React, Vite, Recharts, and Tailwind CSS.

## Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

## Project Structure

```
src/
├── components/     # Reusable chart components
├── hooks/          # Custom React hooks
├── types/          # TypeScript type definitions
├── mock/           # Mock data generators
├── pages/          # Page components
└── App.tsx         # Main application
```

## Technologies

- React 18 + TypeScript
- Vite (build tool)
- Recharts (charts)
- Tailwind CSS (styling)
- Zustand (state management)
- Vitest (testing)
'''


def init_project(project_name: str, output_dir: str):
    """Initialize a new dashboard project."""
    project_path = Path(output_dir) / project_name

    if project_path.exists():
        print(f"Error: Directory '{project_path}' already exists")
        sys.exit(1)

    # Create directory structure
    dirs = [
        project_path,
        project_path / "src" / "components",
        project_path / "src" / "hooks",
        project_path / "src" / "types",
        project_path / "src" / "mock",
        project_path / "src" / "pages",
        project_path / "src" / "test",
        project_path / "__tests__",
        project_path / "public",
    ]

    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)

    # Create files
    files = {
        project_path / "package.json": json.dumps(create_package_json(project_name), indent=2),
        project_path / "tsconfig.json": json.dumps(create_tsconfig(), indent=2),
        project_path / "vite.config.ts": create_vite_config(),
        project_path / "tailwind.config.js": create_tailwind_config(),
        project_path / "postcss.config.js": create_postcss_config(),
        project_path / "index.html": create_index_html(project_name),
        project_path / "vitest.config.ts": create_vitest_config(),
        project_path / "README.md": create_readme(project_name),
        project_path / "src" / "main.tsx": create_main_tsx(),
        project_path / "src" / "index.css": create_index_css(),
        project_path / "src" / "App.tsx": create_app_tsx(),
        project_path / "src" / "test" / "setup.ts": create_test_setup(),
        project_path / "src" / "types" / "index.ts": create_types_template(),
    }

    for file_path, content in files.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

    print(f"Project '{project_name}' created successfully at {project_path}")
    print("\nNext steps:")
    print(f"  cd {project_name}")
    print("  npm install")
    print("  npm run dev")


def main():
    parser = argparse.ArgumentParser(description="Initialize a data visualization dashboard project")
    parser.add_argument("project_name", help="Name of the project")
    parser.add_argument("--path", default=".", help="Output directory (default: current directory)")

    args = parser.parse_args()
    init_project(args.project_name, args.path)


if __name__ == "__main__":
    main()
