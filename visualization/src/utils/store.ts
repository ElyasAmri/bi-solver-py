import {configureStore, createSlice} from '@reduxjs/toolkit'

const tableSlice = createSlice({
  name: 'table-settings',
  initialState: {
    width: 10,
    height: 10,
    useSubtract: true,
    subtract: 3,
    useModulus: false,
    modulus: 0,
    useBinary: false,
  },
  reducers: {
    changeWidth: (state, action) => {
      state.width = parseInt(action.payload)
    },
    changeHeight: (state, action) => {
      state.height = parseInt(action.payload)
    },
    changeUseSubtract: (state, action) => {
      state.useSubtract = action.payload
    },
    changeSubtract: (state, action) => {
      state.subtract = parseInt(action.payload)
    },
    changeUseModulus: (state, action) => {
      state.useModulus = action.payload
    },
    changeModulus: (state, action) => {
      state.modulus = parseInt(action.payload)
    },
    changeUseBinary: (state, action) => {
      state.useBinary = action.payload
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
  changeUseBinary,
} = tableSlice.actions

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch