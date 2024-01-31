import { createApp } from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import shell from 'vue-shell'

import App from './App.vue'


import vueJsonEditor from 'vue-json-editor'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faInfoCircle } from '@fortawesome/free-solid-svg-icons'
import { faChevronDown } from '@fortawesome/free-solid-svg-icons'
import { faChevronRight, faExpand, faCompress, faBookOpen, faBook } from '@fortawesome/free-solid-svg-icons'
import { faCopy, faEnvelope, faPaperPlane } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'



library.add(faInfoCircle, faChevronDown, faChevronRight, faCopy,faEnvelope, faExpand, faCompress, faBook, faPaperPlane, faBookOpen)


const app = createApp(App)

app.use(VueAxios, axios)
app.use(shell)

app.component('vue-json-editor', vueJsonEditor)
app.component('font-awesome-icon', FontAwesomeIcon)

app.config.productionTip = false

app.mount('#app')
