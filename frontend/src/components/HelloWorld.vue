<template>
  <v-container>
    <div class="text-center">
      <v-dialog v-model="dialog" width="500">
        <v-card>
          <v-card-title class="text-h5 grey lighten-2">
            Our suggestion
          </v-card-title>

          <v-card-text> {{ message }} </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click="dialog = false"> I see </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">Welcome to XXX系统</h1>

        <p class="subheading font-weight-regular">
          你可以怎么怎么怎么样
          <br />
          <a href="https://community.vuetifyjs.com" target="_blank"
            >这是我们的链接</a
          >
        </p>
      </v-col>

      <v-col class="mb-5" cols="12">
        <v-row justify="center">
          <div>
            <v-text-field
              label="告诉我们你的信息吧"
              hide-details="auto"
              v-model="text"
            ></v-text-field></div
        ></v-row>
      </v-col>

      <v-col class="mb-5" cols="12">
        <v-row justify="center">
          <v-btn @click="submit" color="info" outlined> Okay </v-btn>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({ dialog: false, text: "", message: "Connection ERR" }),

  methods: {
    submit() {
      this.axios
        .post("/foo", {
          submit: this.text,
        })
        .then((res) => {
          this.message = res.data;
          this.dialog = true;
        })
        .catch(function (err) {
          console.log(err);
          this.message = err;
          this.dialog = true;
        });
    },
  },
};
</script>
