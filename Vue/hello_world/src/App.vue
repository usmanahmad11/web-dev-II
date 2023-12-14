<template>
  <div>
    <header class="bg-light p-3">
      <div class="container">
        <div class="logo">{{ name }}</div>
        <div :id="headingid">Heading</div>
        <div>{{ Channel }}</div>
      </div>
    </header>

    <main class="container mt-4">
      <section>
        <h1>{{ greetUser() }}</h1>
        <p>This is a simple web page using Vue.js!</p>
        <button @click="changeChannel" class="btn btn-primary">Change Channel</button>
      </section>

      <section class="mt-4">
        <h2>Graphical Content</h2>
        <div class="row">
          <div class="col-md-4">
            <div class="card">
              <img src="https://via.placeholder.com/150" class="card-img-top" alt="Placeholder Image">
              <div class="card-body">
                <h5 class="card-title">Card Title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              </div>
            </div>
          </div>

          <div class="col-md-4">
            <div class="card">
              <img src="https://via.placeholder.com/150" class="card-img-top" alt="Placeholder Image">
              <div class="card-body">
                <h5 class="card-title">Card Title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              </div>
            </div>
          </div>

          <div class="col-md-4">
            <div class="card">
              <img src="https://via.placeholder.com/150" class="card-img-top" alt="Placeholder Image">
              <div class="card-body">
                <h5 class="card-title">Card Title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      name: "Usman Ahmad",
      Channel: "Careernest",
      headingid: "Heading"
    };
  },
  methods: {
    greetUser() {
      return `Hello, ${this.name}!`;
    },
    changeChannel() {
      this.Channel = "New Channel";
    }
  }
};
</script>

<style scoped>
.header {
  line-height: 1.5;
  background-color: #f0f0f0;
  padding: 1rem;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
}

main {
  margin: 2rem;
}

button {
  padding: 0.5rem 1rem;
  cursor: pointer;
}

.card {
  margin-bottom: 1rem;
}
</style>
