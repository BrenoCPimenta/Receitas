describe(`Homepage test`, () => {
  it(`Check initial homepage and text search`, () => {
    cy.visit(`/home`);
    cy.matchImageSnapshot(`Homepage: initial`);

    cy.get(`#search_input`).type(`morango`);
    cy.get(`#search_button`).click();
    cy.wait(10);
    cy.matchImageSnapshot(`Homepage: text search`);
  });

  it.only(`Check ingredient search`, () => {
    cy.visit(`/home`);
    cy.get(`#tab_busca_ingrediente`).click();
    cy.wait(10);
    cy.get(`.v-select__slot`).type(`ovo`).type(`{enter}`);
    cy.get(`.v-select__slot`).type(`morango`).type(`{enter}`);
    cy.matchImageSnapshot(`Temporary`);
    cy.get(`#search_ingredient_button`).click();
    cy.wait(20);
    cy.matchImageSnapshot(`Temporary2`);
    cy.get(`.UiGrid__item`).should(`have.length`, 1);
    cy.matchImageSnapshot(`Homepage: ingredient search`);
  });
});
