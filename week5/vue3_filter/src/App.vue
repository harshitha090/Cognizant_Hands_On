<script setup>
import { ref, computed } from 'vue'

const search = ref('')
const selectedCategory = ref('All')

const products = ref([
  { id: 1, name: 'Laptop', category: 'Electronics', price: 65000 },
  { id: 2, name: 'Smartphone', category: 'Electronics', price: 30000 },
  { id: 3, name: 'Headphones', category: 'Electronics', price: 2500 },
  { id: 4, name: 'T-Shirt', category: 'Fashion', price: 1200 },
  { id: 5, name: 'Jeans', category: 'Fashion', price: 1800 },
  { id: 6, name: 'Sneakers', category: 'Fashion', price: 3500 },
  { id: 7, name: 'Notebook', category: 'Education', price: 120 },
  { id: 8, name: 'Python Book', category: 'Education', price: 650 },
  { id: 9, name: 'Backpack', category: 'Accessories', price: 1500 },
  { id: 10, name: 'Water Bottle', category: 'Accessories', price: 450 }
])

const categories = computed(() => {
  return ['All', ...new Set(products.value.map(p => p.category))]
})

const filteredProducts = computed(() => {
  return products.value.filter(product => {
    const matchesSearch = product.name
      .toLowerCase()
      .includes(search.value.toLowerCase())

    const matchesCategory =
      selectedCategory.value === 'All' ||
      product.category === selectedCategory.value

    return matchesSearch && matchesCategory
  })
})
</script>

<template>
  <div class="container">
    <h1>Vue 3 Reactive List & Filter UI</h1>

    <div class="filters">
      <input
        v-model="search"
        type="text"
        placeholder="Search products..."
      />

      <select v-model="selectedCategory">
        <option
          v-for="category in categories"
          :key="category"
        >
          {{ category }}
        </option>
      </select>
    </div>

    <h3>Total Products: {{ filteredProducts.length }}</h3>

    <div v-if="filteredProducts.length > 0" class="cards">
      <div
        class="card"
        v-for="product in filteredProducts"
        :key="product.id"
      >
        <h2>{{ product.name }}</h2>

        <p><strong>Category:</strong> {{ product.category }}</p>

        <p><strong>Price:</strong> ₹{{ product.price }}</p>
      </div>
    </div>

    <p
      v-else
      class="no-data"
    >
      No products found.
    </p>
  </div>
</template>

<style>
*{
  margin:0;
  padding:0;
  box-sizing:border-box;
  font-family:Arial, Helvetica, sans-serif;
}

body{
  background:#f2f5f8;
}

.container{
  width:90%;
  max-width:1000px;
  margin:40px auto;
}

h1{
  text-align:center;
  margin-bottom:25px;
  color:#333;
}

.filters{
  display:flex;
  gap:20px;
  margin-bottom:20px;
}

input,
select{
  flex:1;
  padding:12px;
  border:1px solid #ccc;
  border-radius:8px;
  font-size:16px;
}

h3{
  margin-bottom:20px;
  color:#444;
}

.cards{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:20px;
}

.card{
  background:white;
  padding:20px;
  border-radius:10px;
  box-shadow:0 3px 10px rgba(0,0,0,.1);
  transition:.3s;
}

.card:hover{
  transform:translateY(-5px);
}

.card h2{
  color:#42b883;
  margin-bottom:10px;
}

.card p{
  margin:8px 0;
}

.no-data{
  text-align:center;
  color:red;
  font-size:20px;
  margin-top:30px;
}
</style>