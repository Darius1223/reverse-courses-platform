<template>
  <div class="container pt-5">
    <h1>Регистрация: {{ literalTarget }}</h1>

    <div class="alert alert-primary my-3">
      Введите данные о себе и нажмите кнопку "Регистрация"
    </div>

    <!-- Почта -->
    <form method="post" @submit.prevent="onSubmit" v-if="status === null">
      <div class="mb-3">
        <label for="email" class="form-label">Электронная почта:</label>
        <div class="input-group">
          <span class="input-group-text" id="email-addon">@</span>
          <input
            type="email"
            class="form-control"
            id="email"
            aria-describedby="email-help email-addon"
            aria-label="Email"
            placeholder="@ex.ru"
            required
            v-model="user.email"
          />
        </div>
        <div class="form-text" id="email-help">
          Например: example@example.com
        </div>
      </div>

      <!-- Фамилия -->
      <div class="mb-3">
        <label for="surname-addon" class="form-label">Фамилия:</label>
        <div class="input-group">
          <span class="input-group-text" id="surname-addon"
            ><i class="bi bi-file-earmark-person"></i
          ></span>
          <input
            type="text"
            class="form-control"
            id="surname"
            aria-describedby="surname-addon"
            aria-label="LastName"
            placeholder="Иванов"
            v-model="user.lastname"
            required
          />
        </div>
      </div>
      <!-- Имя -->
      <div class="mb-3">
        <label for="firstname" class="form-label">Имя:</label>
        <div class="input-group">
          <span class="input-group-text" id="basic-addon3"
            ><i class="bi bi-file-earmark-person"></i
          ></span>
          <input
            type="text"
            class="form-control"
            id="firstname"
            aria-describedby="basic-addon3 basic-addon4"
            aria-label="FirstName"
            placeholder="Иван"
            v-model="user.firstname"
            required
          />
        </div>
      </div>
      <!-- Отчество -->
      <div class="mb-3">
        <label for="surname" class="form-label">Отчество:</label>
        <div class="input-group">
          <span class="input-group-text" id="basic-addon3"
            ><i class="bi bi-file-earmark-person"></i
          ></span>
          <input
            type="text"
            class="form-control"
            id="surname"
            aria-describedby="basic-addon3 basic-addon4"
            placeholder="Иванович"
            v-model="user.surname"
            required
          />
        </div>
      </div>

      <div class="mb-3">
        <label for="basic-url" class="form-label">Номер телефона:</label>
        <div class="input-group">
          <span class="input-group-text" id="basic-addon3"
            ><i class="bi bi-telephone"></i
          ></span>
          <input
            type="tel"
            class="form-control"
            id="telephone"
            aria-describedby="basic-addon3 basic-addon4"
            placeholder="8-888-888-88-88"
            v-model="user.telephone"
            required
          />
        </div>
      </div>

      <div class="form-check">
        <input
          class="form-check-input"
          type="checkbox"
          value=""
          id="flexCheckDefault"
          required
        />
        <label class="form-check-label" for="flexCheckDefault">
          Данным действием подтверждаю "Согласие об обработке персональных
          данных"
        </label>
      </div>

      <button type="submit" class="btn btn-lg btn-primary mt-3">
        Регистрация
      </button>
    </form>

    <div v-else>
      <div class="alert alert-success" v-if="status === 'success'">
        Регистрация прошла успешно
      </div>
      <div class="alert alert-danger" v-else>Регистрация не прошла, ОШибка</div>
    </div>
  </div>
</template>

<script setup>
import apiClient from "@/api/utils";
import { ref } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();

const target = route.params.target;

const literalTarget = target == "student" ? "Ученик" : "Учитель";

let user = ref({
  email: null,
  firstname: null,
  lastname: null,
  surname: null,
  telephone: null,
  role: target,
});
const status = ref(null);

const onSubmit = () => {
  console.log("Start registration", (user = user.value));

  apiClient
    .registration(user)
    .then(() => {
      console.log("Success registrations");
      status.value = "success";
    })
    .catch((err) => {
      console.error(err);
      status.value = "error";
    });
};
</script>
