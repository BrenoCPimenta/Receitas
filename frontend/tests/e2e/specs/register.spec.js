describe(`Register form test`, () => {
  it(`Validate all required fields`, () => {
    cy.visit(`/login`);
    cy.get('#login_register_message').click();
    cy.get('#submit_form_login').click();
    cy.wait(10);
    cy.matchImageSnapshot('Required field: username');

    cy.get('input[name="username"]').type('Novo Usuario'); 
    cy.get('#submit_form_login').click();
    cy.wait(10);
    cy.matchImageSnapshot('Required field: email');

    cy.get('input[name="email"]').type('test@mail.com'); 
    cy.get('#submit_form_login').click();
    cy.wait(10);
    cy.matchImageSnapshot('Required field: password');

    cy.get('input[name="password"]').type('Senha123456'); 
    cy.get('#submit_form_login').click();
    cy.wait(10);
    cy.matchImageSnapshot('Required field: confirmPassword');

    cy.get('input[name="confirmPassword"]').type('Senha'); 
    cy.get('#submit_form_login').click();
    cy.wait(10);
    cy.matchImageSnapshot('Fields must match: [password, confirmPassword]');

    cy.get('input[name="confirmPassword"]').type('123456'); 
    cy.get('#submit_form_login').click();
    cy.wait(10);
    cy.matchImageSnapshot('Register: success');
  });
});
