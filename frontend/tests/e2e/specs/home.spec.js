describe(`Homepage test`, () => {
  it(`Check initial homepage and text search`, () => {
    cy.visit(`/`);
    cy.get('#anonymous_login_button').click();
    cy.wait(10);
    cy.matchImageSnapshot(`Homepage: initial`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });

    cy.get(`#search_input`).type(`morango`);
    cy.get(`#search_button`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Homepage: text search`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });
  });

  it(`Check ingredient search`, () => {
    cy.visit(`/`);
    cy.get('#anonymous_login_button').click();
    cy.wait(10);
    cy.get(`#tab_busca_ingrediente`).click();
    cy.wait(10);
    cy.get(`.v-select__slot`).type(`ovo`).type(`{enter}`);
    cy.get(`.v-select__slot`).type(`morango`).type(`{enter}`);
    cy.get(`#search_ingredient_button`).click();
    cy.wait(20);
    cy.matchImageSnapshot(`Homepage: ingredient search`, {
      customDiffConfig: {threshold: 5.0}, // threshold for each pixel
      failureThreshold: 5.0, // threshold for entire image
      failureThresholdType: 'percent', // percent of image or number of pixels
    });
  });
});
