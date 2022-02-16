describe(`Login form test`, () => {
  it(`Validate login required fields`, () => {
    cy.visit(`/login`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Required field: username`);

    cy.get(`input[name="username"]`).type(`userTest`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Required field: password`);

    cy.get(`input[name="password"]`).type(`123456`);
    cy.get(`#submit_form_login`).click();
    cy.wait(10);

    cy.matchImageSnapshot(`Login: success`);
  });
});
