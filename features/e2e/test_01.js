const { When } = require("@badeball/cypress-cucumber-preprocessor");

When("я ya.ru", () => {
  cy.visit("https://ya.ru/");
});

When("я смотрю на картику", () => {
  assert.deepEqual({}, {});
});
