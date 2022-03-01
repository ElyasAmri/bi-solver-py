import Table from "./components/Table";
import Controls from "./components/Controls";
import Grid from './datatypes/Grid'
import {useSelector} from "react-redux";

// noinspection JSUnusedGlobalSymbols
function App() {
  const {width, height, subtract, modulus} = useSelector(state => state.table)
  const grid = new Grid(width, height, subtract, modulus)

  return (
    <div className="bg-gray-100 min-w-screen min-h-screen pb-72 pt-4">
      <div className="max-w-sm md:max-w-3xl mx-auto xl:max-w-6xl xl:mx-2">
        <Table data={grid.data}/>
        <div className="fixed bottom-4 left-4">
          <Controls/>
          <p className="px-4">Sum: {grid.sum()}</p>
        </div>
      </div>
    </div>
  )
}

export default App
