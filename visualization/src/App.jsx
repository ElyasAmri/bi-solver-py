import Table from "./components/Table";
import Controls from "./components/Controls";
import Grid from './datatypes/Grid'

// noinspection JSUnusedGlobalSymbols
function App() {
  const grid = new Grid(11, 11)

  return (
    <div className="bg-gray-100 w-full h-full">
      <div className="max-w-sm md:max-w-3xl mx-auto py-4">
        <Table data={grid.data}/>
        <Controls/>
      </div>
    </div>
  )
}

export default App
