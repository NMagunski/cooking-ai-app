import axios from 'axios'
import { useState } from 'react'

interface RecipeResponse {
  success: boolean
  recipe: string
}

export const useRecipes = () => {
  const [recipe, setRecipe] = useState<string>('')
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [error, setError] = useState<string>('')

  const generateRecipe = async (ingredients: string[], equipment: string[]) => {
    setIsLoading(true)
    setError('')
    setRecipe('')

    try {
      const response = await axios.post<RecipeResponse>(
        '/api/generate',
        {
          ingredients,
          equipment,
          diet: 'none',
          max_time: 30
        }
      )
      
      if (response.data.success) {
        setRecipe(response.data.recipe)
      } else {
        setError('Неуспешно генериране на рецепта')
      }
    } catch (err) {
      setError('Грешка при връзка със сървъра')
      console.error('API Error:', err)
    } finally {
      setIsLoading(false)
    }
  }

  return { recipe, isLoading, error, generateRecipe }
}