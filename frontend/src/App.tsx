import { RecipeForm } from '@/components/RecipeForm'

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-gray-100 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-3xl mx-auto">
        <div className="text-center mb-10">
          <h1 className="text-4xl font-extrabold text-gray-900 sm:text-5xl mb-3">
            Cooking AI
          </h1>
          <p className="text-xl text-gray-600">
            Генерирай перфектни рецепти с изкуствен интелект
          </p>
        </div>
        <RecipeForm />
      </div>
    </div>
  )
}

export default App