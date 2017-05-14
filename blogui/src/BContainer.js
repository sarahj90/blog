import {Container} from 'flux/utils';

import Store from './BStore';
import actions from './BActions';

import App from "./App";

function getStores() {
  return [Store];
}

function getState() {
  return Store.getState().merge(actions).toObject();
}

export default Container.createFunctional(App, getStores, getState);
