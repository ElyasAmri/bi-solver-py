import {StrictMode} from 'react'
import {createRoot} from "react-dom/client";
import './index.css'
import App from './App'
import {Provider} from 'react-redux';
import {store} from './utils/store';

const container = document.getElementById('root') as HTMLElement
const root = createRoot(container)
const app = (
    <StrictMode>
        <Provider store={store}>
            <App/>
        </Provider>
    </StrictMode>
)

root.render(app)