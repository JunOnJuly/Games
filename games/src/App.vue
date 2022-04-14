<template>
  <div id="app">
    <nav class="bg-dark fs-3 text-center pt-2">
      <router-link :to="{ name: 'HomeView' }" class="text-white fs-1 fw-bold text-decoration-none">Home</router-link>
      <div class="d-flex justify-content-center py-2">
        <router-link :to="{ name: 'SudokuView' }" class="text-decoration-none text-white align-self-center mx-2">Sudoku</router-link>
        <router-link :to="{ name: 'OthelloView' }" class="text-decoration-none text-white align-self-center mx-2">Othello</router-link>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<style>
  body {
    background-color: grey;
  }
</style>
