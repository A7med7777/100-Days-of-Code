<template>
  <div :class="`alert alert-${type}`" role="alert">
    {{ message }}
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true,
    },
    type: {
      type: String,
      default: "success", // success, error, etc.
    },
  },
};
</script>
