const productDb = [
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/016/663/84433/84433_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Patê de tomate seco",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/126/503/51982/51982_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Pizza Light com tomate seco e rúcula",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/106/023/37570/37570_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Patê de tomate seco",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/035/234/121407/121407_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Risoto com tomate seco, mussarela e rúcula da Tam",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/096/704/31596/31596_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Ravioli com recheio de ricota, rúcula e tomate seco regado ao molho Alfredo",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/166/270/218243/218243_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Salmão com tomate seco e alcaparras",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/198/374/303672/303672_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Arroz carreteiro do Borba",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/093/319/198296/198296_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Arroz carreteiro e feijão tropeiro segundo Polinari",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/112/462/281831/281831_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Arroz carreteiro de churrasco",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/064/685/116832/116832_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Carreteiro de linguiça",
  },
  {
    img: "https://img.itdg.com.br/tdg/assets/default/recipe_original.png?mode=crop&amp;width=300&amp;height=200",
    name: "Arroz carreteiro do Mato Grosso do Sul",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/001/624/321428/321428_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Macarrão à carbonara",
  },
  {
    img: "https://img.itdg.com.br/tdg/assets/default/recipe_original.png?mode=crop&amp;width=300&amp;height=200",
    name: "Pizza marguerita de macarrão",
  },
  {
    img: "https://img.itdg.com.br/tdg/images/recipes/000/065/498/12160/12160_original.jpg?mode=crop&amp;width=300&amp;height=200",
    name: "Penne à bolonhesa ao molho marguerita e queijo",
  },
  {
    img: "https://img.itdg.com.br/tdg/assets/default/recipe_original.png?mode=crop&amp;width=300&amp;height=200",
    name: "Macarrão marguerita",
  },
];

// eslint-disable-next-line import/prefer-default-export
export function get({ filter = {}, limit, page = 1 }) {
  const pageInt = parseInt(page, 10);

  return new Promise((resolve) => {
    setTimeout(() => {
      let result = productDb;
      let filteredResultCount = result.length;

      // if (filter.category) {
      //   result = result.filter(x => x.categories.includes(filter.category));
      //   filteredResultCount = result.length;
      // }

      if (limit) {
        const start = (pageInt - 1) * limit;
        const end = start + limit;
        result = result.slice(start, end);
      }

      resolve({
        data: result,
        meta: {
          pageCount: Math.ceil(filteredResultCount / limit),
        },
      });
    }, 500);
  });
}
