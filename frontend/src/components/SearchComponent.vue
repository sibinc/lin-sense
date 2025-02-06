<template>
  <div>
    <input v-model="query" placeholder="Search..." @keyup.enter="onSearch"/>
    <button @click="onSearch">Search</button>
    <div v-if="result">
      <h3>Search Result:</h3>
      <p>ID: {{ result.id }}</p>
      <p>Description: {{ result.description }}</p>
      <p>Alias: {{ result.alias }}</p>
      <p>Department: {{ result.department }}</p>
    </div>
  </div>
</template>

<script>
import { searchMenu } from '@/api';

export default {
  data() {
    return {
      query: '',
      result: null,
    };
  },
  methods: {
    async onSearch() {
      try {
        this.result = await searchMenu(this.query);
      } catch (error) {
        console.error("Search failed:", error);
      }
    },
  },
};
</script>

<style scoped>
input {
  margin-right: 10px;
}
</style>