import {configureStore, createSlice} from '@reduxjs/toolkit'

const tableSlice = createSlice({
  name: 'table-settings',
  initialState: {
    width: 10,
    height: 10,
    useSubtract: false,
    subtract: 0,
    useModulus: false,
    modulus: 0,
  },
  reducers: {
    changeWidth: (state, action) => {
      state.width = action.payload
    },
    changeHeight: (state, action) => {
      state.height = action.payload
    },
    changeUseSubtract: (state, action) => {
      state.useSubtract = action.payload
    },
    changeSubtract: (state, action) => {
      state.subtract = action.payload
    },
    changeUseModulus: (state, action) => {
      state.useModulus = action.payload
    },
    changeModulus: (state, action) => {
      state.modulus = action.payload
    }
  }
})


export const store = configureStore({
  reducer: {
    table: tableSlice.reducer
  },
})

export const {
  changeWidth,
  changeHeight,
  changeUseSubtract,
  changeSubtract,
  changeUseModulus,
  changeModulus,
} = tableSlice.actions