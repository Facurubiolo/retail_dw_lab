import pandas as pd

# Cambiá las rutas a donde tengas los archivos en tu PC
categories = pd.read_csv("raw/categories.csv")
products = pd.read_csv("raw/products.csv")

# 1. Join productos con categorías para traer el nombre de la categoría
merged = products.merge(
    categories[['category_id', 'category_name', 'parent_category_id']],
    on="category_id", how="left"
)

# 2. Join para traer el nombre de la categoría padre
merged = merged.merge(
    categories[['category_id', 'category_name']].rename(
        columns={'category_id': 'parent_category_id', 'category_name': 'parent_category_name'}
    ),
    on="parent_category_id", how="left"
)

# 3. Eliminamos el ID de la categoría padre si ya no lo queremos
merged = merged.drop(columns=['parent_category_id', "category_id"])

# Guardar el nuevo CSV
merged.to_csv("raw/products_denormalized.csv", index=False)

print("Archivo 'products_denormalized.csv' creado con éxito con nombres de categorías y categorías padre.")
