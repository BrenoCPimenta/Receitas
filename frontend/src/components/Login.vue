<template>
  <div>
    <v-card
      class="elevation-5"
      width="400"
    >
      <v-img
        height="200px"
        src="../assets/titulo.png"
      />
      <v-toolbar
        dark
        color="mycolor"
      >
        <v-toolbar-title>
          {{ isRegister ? stateObj.register.name : stateObj.login.name }}
        </v-toolbar-title>
      </v-toolbar>
      <v-card-text>
        <form
          ref="form"
          @submit.prevent="isRegister ? register() : login()"
        >
          <v-text-field
            v-model="username"
            name="username"
            label="Usuário"
            type="text"
            required
            color="mycolor"
          />

          <v-text-field
            v-if="isRegister"
            v-model="email"
            name="email"
            label="E-mail"
            type="text"
            required
            color="mycolor"
          />

          <v-text-field
            v-model="password"
            name="password"
            label="Senha"
            type="password"
            required
            color="mycolor"
          />

          <v-text-field
            v-if="isRegister"
            v-model="confirmPassword"
            name="confirmPassword"
            label="Confirme a senha"
            type="password"
            required
            color="mycolor"
          />
          <div class="red--text">
            {{ errorMessage }}
          </div>
          <v-btn
            id="submit_form_login"
            type="submit"
            class="white--text mt-4"
            color="mycolor"
            value="log in"
          >
            {{ isRegister ? stateObj.register.btn : stateObj.login.btn }}
          </v-btn>
          <div
            id="login_register_message"
            class="grey--text mt-4"
            @click="isRegister = !isRegister;"
          >
            {{ toggleMessage }}
          </div>
        </form>
      </v-card-text>
    </v-card>
    <br>

    <div class="text-center">
      <v-btn
        color="mycolor"
        dark
        outlined
        @click="clickEntrarSemConta"
      >
        Entrar sem conta
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: `Login`,
  data() {
    return {
      username: ``,
      email: ``,
      password: ``,
      confirmPassword: ``,
      isRegister: false,
      errorMessage: ``,
      stateObj: {
        register: {
          name: `Crie uma conta`,
          btn: `Criar`,
          message: `Já possui uma conta? Faça login aqui.`,
        },
        login: {
          name: `Acesse sua conta`,
          btn: `Entrar`,
          message: `Primeira vez? Crie uma conta aqui.`,
        },
      },
    };
  },
  computed: {
    toggleMessage() {
      return this.isRegister ? this.stateObj.register.message : this.stateObj.login.message;
    },
  },
  methods: {
    login() {
      const { username } = this;
      this.$router.replace({ name: `home`, params: { username } });
    },
    register() {
      if (this.password === this.confirmPassword) {
        this.isRegister = false;
        this.errorMessage = ``;
        this.$refs.form.reset();
      } else {
        this.errorMessage = `Senhas não coincidem`;
      }
    },
    clickEntrarSemConta() {
      this.$router.replace({ name: `home` });
    },
  },
};
</script>
