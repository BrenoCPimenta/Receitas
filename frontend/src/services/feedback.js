import feedbacks from './feedbacksMock';

const parsedFeedbacks = feedbacks.map(el => ({
  ...el,
  date: new Date(el.date),
}));

const mapFeedback = (selectedFeedbacks) => {
  const result = [0, 0, 0, 0, 0];
  selectedFeedbacks.forEach((el) => {
    result[el.feedback - 1] += 1;
  });
  return result;
};

function get({ filter = {} } = {}) {
  return new Promise((resolve) => {
    setTimeout(() => {
      let result = parsedFeedbacks;
      if (filter.startDate) {
        const startDate = new Date(filter.startDate);
        result = result.filter(x => x.date.getTime() >= startDate.getTime());
      }

      if (filter.endDate) {
        const endDate = new Date(filter.endDate);
        result = result.filter(x => x.date.getTime() <= endDate.getTime());
      }
      resolve({
        data: mapFeedback(result),
      });
    }, 500);
  });
}

export {
  get,
};
