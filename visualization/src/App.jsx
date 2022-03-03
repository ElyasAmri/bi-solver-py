import Table from "./components/Table";
import Controls from "./components/Controls";
import Grid from './datatypes/Grid'
import {useSelector} from "react-redux";
import {useState} from "react";

// noinspection JSUnusedGlobalSymbols
function App() {
  const {width, height, subtract, modulus, useBinary} = useSelector(state => state.table)
  const grid = new Grid(width, height, subtract, modulus)

  const isGridSimple = subtract === 0 && modulus === 0

  const rawGrid = isGridSimple ? grid : new Grid(width, height, 0, 0)

  const frames = grid.getFrames()
  const rawFrames = isGridSimple ? frames : rawGrid.getFrames()

  const [tab, setTab] = useState('table')

  return (
    <div className="bg-gray-100 min-w-screen min-h-screen pb-72 pt-4">
      <div className="max-w-sm md:max-w-3xl mx-auto xl:max-w-6xl xl:mx-2">
        <ul className="w-full h-10 flex flex-row justify-evenly text-white font-bold">
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={() => setTab('table')}>Table</li>
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={() => setTab('frame')}>Frames</li>
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={() => setTab('sub')}>Subtraction Forms</li>
        </ul>
        <hr className="mb-4"/>
        {tab === 'table' &&
          <Table data={grid.data}/>
        }
        {tab === 'frame' &&
          <div className="flex flex-row justify-evenly">
            <div>
              <p className="text-center mb-4">Raw</p>
              <div className="space-y-2">
                {rawFrames.map((e, i) => <Table key={i}
                                                data={useBinary ? e.binData : e.data}/>)}
              </div>
            </div>
            <div>
              <p className="text-center mb-4">Real</p>
              <div className="space-y-2">
                {frames.map((e, i) => <Table key={i}
                                             data={useBinary ? e.binData : e.data}/>)}
              </div>
            </div>
          </div>
        }
        {tab === 'sub' &&
          'subtraction form'
        }
        <div className="fixed bottom-4 left-4">
          <Controls/>
          <p className="px-4">Sum: {grid.sum()}</p>
        </div>
      </div>
    </div>
  )
}

export default App
