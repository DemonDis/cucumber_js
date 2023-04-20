const { defineConfig } = require("cypress");
const webpack = require("@cypress/webpack-preprocessor");
const preprocessor = require("@badeball/cypress-cucumber-preprocessor");

async function setupNodeEvents(on, config) {
  await preprocessor.addCucumberPreprocessorPlugin(on, config);

  on(
    "file:preprocessor",
    webpack({
      webpackOptions: {
        resolve: {
          extensions: [".ts", ".js", "jsx", "tsx"],
        },
        module: {
          rules: [
            {
              test: /\.feature$/,
              use: [
                {
                  loader: "@badeball/cypress-cucumber-preprocessor/webpack",
                  options: config,
                },
              ],
            },
          ],
        },
      },
    })
  );

  return config;
}

module.exports = defineConfig({
  e2e: {
    specPattern: "**/*.feature",
    setupNodeEvents,
    // specPattern: "tests/e2e",
    fileServerFolder: "features/e2e",
    // fixturesFolder: "tests/e2e/fixtures",
    // integrationFolder: "tests/e2e/integration",
    // pluginsFile: "tests/e2e/plugins/index.js",
    // screenshotsFolder: "tests/e2e/screenshots",
    supportFile: "features/support/e2e.js",
    // videosFolder: "tests/e2e/videos"
  },
});