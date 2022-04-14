<template>
  <div id="carouselExampleControls" class="carousel slide d-flex" data-bs-ride="carousel">

      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>

      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvWNS1Z5xxNF1B49a-fCvIcqgxpWf0FO90nw&usqp=CAU" class="d-block">
        </div>

        <div class="carousel-item">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg/1200px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png" class="d-block">
        </div>

      </div>

      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>

    </div>
</template>

<script>
export default {

}
</script>

<style>
  img {
    height: 50rem;
    margin-left: auto;
    margin-right: auto;
  }
</style>