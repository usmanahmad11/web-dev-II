<script >
export default {
  name:"App",
  data() {
    return {
      name:"Usman Ahmad",
      channel:"Careernest",
      Phone:"<h3>New Mobile Number</h3>",
      headingID:"HEADING",
      isDisabled:true,
      isSoldout:false,
      highlight:'orange',
      headerSize:100
    };
  },
};
</script>


<template>
 <div>Hello {{ name }}</div> 
 
 <div v-text="channel"></div>

 <div v-html="Phone"></div>

 <h2 v-bind:id="headingID">Heading</h2>
 <button v-bind:disabled="isDisabled">Bind</button>

 <h2 class="underline">Underlined Text</h2>

 <h3 v-bind:class="isSoldout ? 'sold-out':'new'">Soldout Movie </h3>

 <h2 v-bind:style="{
    color:highlight,
    'font-size': headerSize + 'px'
 }"> Inline Styles</h2>


</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
  .underline {
    text-decoration: underline;
  }

  .new{
    color:olive;
  }
  .sold-out{
    
    background-color: aqua;

  }

  
}
</style>


