#!/bin/bash

# Проверка дали директорията frontend съществува
if [ -d "frontend" ]; then
  echo "⚠️ Директория 'frontend' вече съществува. Изтрийте я или преименувайте преди да продължите."
  exit 1
fi

# Създаване на базова структура
mkdir -p frontend && cd frontend

# Инициализиране на Vite проект
echo "🛠️ Създаване на Vite + React + TypeScript проект..."
npm create vite@latest . -- --template react-ts

# Инсталиране на основни зависимости
echo "📦 Инсталиране на зависимости..."
npm install
npm install axios tailwindcss postcss autoprefixer @types/node --save
npm install -D @vitejs/plugin-react eslint vite-tsconfig-paths

# Инициализиране на Tailwind CSS
echo "🎨 Конфигуриране на Tailwind CSS..."
npx tailwindcss init -p

# Създаване на директории
echo "📂 Създаване на файлова структура..."
mkdir -p src/{components,hooks,pages,styles,assets}

# Създаване на конфигурационни файлове
echo "⚙️ Генериране на конфигурационни файлове..."

# Vite config
cat > vite.config.ts <<EOL
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})
EOL

# Tailwind config
cat > tailwind.config.js <<EOL
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
EOL

# Основен CSS файл
cat > src/styles/main.css <<EOL
@tailwind base;
@tailwind components;
@tailwind utilities;
EOL

# App компонент
cat > src/App.tsx <<EOL
import { useState } from 'react'
import { useRecipes } from '@/hooks/useRecipes'

function App() {
  const [ingredients, setIngredients] = useState<string[]>([])

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold text-center mb-8">AI Готвач</h1>
      {/* Добавете вашия интерфейс тук */}
    </div>
  )
}

export default App
EOL

# useRecipes hook
cat > src/hooks/useRecipes.ts <<EOL
import axios from 'axios'
import { useState } from 'react'

export const useRecipes = () => {
  const [recipes, setRecipes] = useState<string[]>([])

  const generateRecipes = async (ingredients: string[]) => {
    try {
      const response = await axios.post('/api/generate', {
        ingredients
      })
      setRecipes(response.data.recipes)
    } catch (error) {
      console.error('Грешка:', error)
    }
  }

  return { recipes, generateRecipes }
}
EOL

# TypeScript декларации
cat > src/vite-env.d.ts <<EOL
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_BASE_URL: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
EOL

# Инсталиране и стартиране
echo "🚀 Стартиране на разработен сървър..."
npm run dev

echo "✅ Готово! Vite проектът е създаден успешно."
echo "➡️ Доступен на: http://localhost:5173"