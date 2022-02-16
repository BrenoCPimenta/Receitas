describe(`Login form test`, () => {
  it(`Validate login required fields`, () => {
    cy.visit(`/`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Required field: username`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });

    cy.get(`input[name="username"]`).type(`userTest`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Required field: password`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });

    cy.get(`input[name="password"]`).type(`123456`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);

    cy.matchImageSnapshot(`Login: success`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });
  });
});
