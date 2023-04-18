const { When, Then } = require("@badeball/cypress-cucumber-preprocessor");

When("я ya.ru", () => {
  cy.visit("https://ya.ru/");
});

Then("я смотрю на картику", () => {
  assert.deepEqual({}, {});
});
