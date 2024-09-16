<template>
    <div class="container pt-5">
        <h1>Регистрация: {{ literalTarget }}</h1>
        
        <div class="alert alert-primary my-3">
            Введите данные о себе и нажмите кнопку "Регистрация"
        </div>

<form method="post">
    <div class="mb-3">
  <label for="email" class="form-label">Электронная почта:</label>
  <div class="input-group">
    <span class="input-group-text" id="email-addon">@</span>
    <input type="mail" class="form-control" id="email" aria-describedby="email-help email-addon" aria-label="Email" placeholder="@ex.ru" required>
  </div>
  <div class="form-text" id="email-help">Например: example@example.com</div>
</div>

<div class="mb-3">
  <label for="surname-addon" class="form-label">Фамилия:</label>
  <div class="input-group">
    <span class="input-group-text" id="surname-addon"><i class="bi bi-file-earmark-person"></i></span>
    <input type="mail" class="form-control" id="surname" aria-describedby="surname-addon" placeholder="Иванов" required>
  </div>
</div>

<div class="mb-3">
  <label for="basic-url" class="form-label">Имя:</label>
  <div class="input-group">
    <span class="input-group-text" id="basic-addon3"><i class="bi bi-file-earmark-person"></i></span>
    <input type="mail" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4" placeholder="Иван" required>
  </div>
</div>

<div class="mb-3">
  <label for="basic-url" class="form-label">Отчество:</label>
  <div class="input-group">
    <span class="input-group-text" id="basic-addon3"><i class="bi bi-file-earmark-person"></i></span>
    <input type="mail" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4" placeholder="Иванович" required>
  </div>
</div>

<div class="mb-3">
  <label for="basic-url" class="form-label">Номер телефона:</label>
  <div class="input-group">
    <span class="input-group-text" id="basic-addon3"><i class="bi bi-telephone"></i></span>
    <input type="tel" class="form-control" id="basic-url" aria-describedby="basic-addon3 basic-addon4" placeholder="8-888-888-88-88" required>
  </div>
</div>

<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" required>
  <label class="form-check-label" for="flexCheckDefault">
    Данным действием подтверждаю "Согласие об обработке персональных данных"
  </label>
</div>

<button type="submit" class="btn btn-lg btn-primary mt-3">Регистрация</button>
</form>

    </div>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()

const target = route.params.target;

const literalTarget = target == 'student' ? 'Ученик' : 'Учитель'
</script>