import { useState, FormEvent } from 'react';
import { useRecipes } from '@/hooks/useRecipes';

export const RecipeForm = () => {
  const [inputIngredient, setInputIngredient] = useState('');
  const [ingredients, setIngredients] = useState<string[]>([]);
  const [equipment, setEquipment] = useState<string[]>(['JULGUI']);
  const { recipe, isLoading, error, generateRecipe } = useRecipes();

  const handleAddIngredient = () => {
    if (inputIngredient.trim() && !ingredients.includes(inputIngredient.trim())) {
      setIngredients([...ingredients, inputIngredient.trim()]);
      setInputIngredient('');
    }
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    generateRecipe(ingredients, equipment);
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">Създаване на рецепта</h2>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div className="flex gap-2">
          <input
            type="text"
            value={inputIngredient}
            onChange={(e) => setInputIngredient(e.target.value)}
            placeholder="Добави съставка"
            className="flex-1 p-2 border rounded"
          />
          <button
            type="button"
            onClick={handleAddIngredient}
            className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
          >
            Добави
          </button>
        </div>

        <div className="mt-4">
          <h3 className="font-semibold">Добавени съставки:</h3>
          <ul className="list-disc pl-5 mt-2">
            {ingredients.map((ing, index) => (
              <li key={index}>{ing}</li>
            ))}
          </ul>
        </div>

        <button
          type="submit"
          disabled={isLoading}
          className="w-full bg-green-500 text-white py-2 rounded hover:bg-green-600 disabled:bg-gray-400"
        >
          {isLoading ? 'Генерира се...' : 'Генерирай рецепта'}
        </button>

        {error && <p className="text-red-500">{error}</p>}
        {recipe && (
          <div className="mt-4 p-4 bg-gray-100 rounded">
            <h3 className="font-bold">Рецепта:</h3>
            <pre className="whitespace-pre-wrap">{recipe}</pre>
          </div>
        )}
      </form>
    </div>
  );
};