<template>
  <div class="">
    <div class="text-center grad pt-5">
      <div class="">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="256"
          height="256"
          fill="white"
          class="bi bi-backpack2"
          viewBox="-2 -2 20 20"
          stroke-opacity="0.8"
          stroke-width="0.2"
          stroke="#16045f"
        >
          <path
            d="M4.04 7.43a4 4 0 0 1 7.92 0 .5.5 0 1 1-.99.14 3 3 0 0 0-5.94 0 .5.5 0 1 1-.99-.14"
          />
          <path
            fill-rule="evenodd"
            d="M4 9.5a.5.5 0 0 1 .5-.5h7a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5h-7a.5.5 0 0 1-.5-.5zm1 .5v3h6v-3h-1v.5a.5.5 0 0 1-1 0V10z"
          />
          <path
            d="M6 2.341V2a2 2 0 1 1 4 0v.341c2.33.824 4 3.047 4 5.659v1.191l1.17.585a1.5 1.5 0 0 1 .83 1.342V13.5a1.5 1.5 0 0 1-1.5 1.5h-1c-.456.607-1.182 1-2 1h-7a2.5 2.5 0 0 1-2-1h-1A1.5 1.5 0 0 1 0 13.5v-2.382a1.5 1.5 0 0 1 .83-1.342L2 9.191V8a6 6 0 0 1 4-5.659M7 2v.083a6 6 0 0 1 2 0V2a1 1 0 0 0-2 0M3 13.5A1.5 1.5 0 0 0 4.5 15h7a1.5 1.5 0 0 0 1.5-1.5V8A5 5 0 0 0 3 8zm-1-3.19-.724.362a.5.5 0 0 0-.276.447V13.5a.5.5 0 0 0 .5.5H2zm12 0V14h.5a.5.5 0 0 0 .5-.5v-2.382a.5.5 0 0 0-.276-.447L14 10.309Z"
          />
        </svg>
      </div>
      <div class="text-white mt-1 contur-text">
        <h1 class="display-3">Педагогическая мастерская</h1>
      </div>
    </div>
    <div id="content" class="container text-light">
      <div class="lead mt-5">
        <div class="row">
          <div class="col">
            <h3 class="bi bi-highlighter"></h3>
            <h3>Возможность</h3>
            <p>
              Мы рады видеть вас на нашем сайте, посвященном созданию
              вдохновляющей и эффективной образовательной среды. Наша мастерская
              — это пространство для педагогов, родителей и всех, кто
              интересуется развитием образования. Здесь вы найдете полезные
              ресурсы, инновационные методики, идеи для уроков и практические
              советы по работе с детьми.
            </p>
            <router-link
              class="btn btn-primary btn-lg w-100"
              :to="{ name: 'registration', params: { target: 'student' } }"
            >
              Я ученик
            </router-link>
          </div>

          <div class="col">
            <h3 class="bi bi-marker-tip"></h3>
            <h3>Цель</h3>
            <p>
              Мы верим, что каждый педагог — это творец, способный изменить
              жизнь своих учеников. Наша цель — поддерживать вас в этом важном
              деле, предоставляя актуальную информацию и возможности для
              профессионального роста. Присоединяйтесь к нашему сообществу,
              делитесь опытом и находите единомышленников! Давайте вместе
              строить будущее образования!
            </p>

            <router-link
              class="btn btn-primary btn-lg w-100"
              :to="{ name: 'registration', params: { target: 'teacher' } }"
            >
              Я учитель
            </router-link>
          </div>
          <button class="btn btn-lg btn-outline-light w-10 mt-3">
            Уже зарегистрирован
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
@import "../styles/main.scss";

.grad {
  // background-image: linear-gradient(180deg, $primary, $dark);
  // background: rgb(2,0,36);
  background: linear-gradient(180deg, $primary 0%, $dark 100%);
}
</style>
