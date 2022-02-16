describe(`Register form test`, () => {
  it(`Validate all required fields`, () => {
    cy.visit(`/`);
    cy.get(`#login_register_message`).click();
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Required field: username`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });

    cy.get(`input[name="username"]`).type(`Novo Usuario`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Required field: email`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });

    cy.get(`input[name="email"]`).type(`test@mail.com`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Required field: password`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });

    cy.get(`input[name="password"]`).type(`Senha123456`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Required field: confirmPassword`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });

    cy.get(`input[name="confirmPassword"]`).type(`Senha`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Fields must match: [password, confirmPassword]`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });

    cy.get(`input[name="confirmPassword"]`).type(`123456`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Register: success`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });
  });
});
