import React from 'react';
import ReactDOM from 'react-dom';
import BContainer from './BContainer';
import './index.css';
import actions from "./BActions"

ReactDOM.render(
  <BContainer />,
  document.getElementById('root')
);

actions.fetchArticles();
