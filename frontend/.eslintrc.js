module.exports = {
  root: true,
  env: {
    'cypress/globals': true,
  },
  extends: [
    `plugin:vue/recommended`,
    `@avalanche/eslint-config`,
  ],
  rules: {
    'no-console': process.env.NODE_ENV === `production` ? `error` : `warn`,
    'no-debugger': process.env.NODE_ENV === `production` ? `error` : `warn`,
    'vue/component-name-in-template-casing': [`error`,
      `PascalCase`,
    ],
    'vue/no-v-html': 0,
    'vue/html-closing-bracket-spacing': [`error`, {
      startTag: `never`,
      endTag: `never`,
      selfClosingTag: `never`,
    }],
  },
  parserOptions: {
    parser: `@babel/eslint-parser`,
  },
  plugins: [
    `cypress`,
    `@babel`,
  ],
};
