import {useState} from "react";
import {useSelector} from "react-redux";
import Table from "./components/Table";
import Controls from "./components/Controls";
import Grid from './datatypes/Grid'
import SubtractionCounter from "./datatypes/SubtractionCounter";

// noinspection JSUnusedGlobalSymbols
function App() {
  const {width, height, subtract, modulus, useBinary} = useSelector(state => state.table)
  const [tab, setTab] = useState('table')

  const grid = new Grid(width, height, subtract, modulus)

  const isGridSimple = subtract === 0 && modulus === 0

  const rawGrid = isGridSimple ? grid : new Grid(width, height, 0, 0)

  const frames = grid.getFrames()
  const rawFrames = isGridSimple ? frames : rawGrid.getFrames()

  const counter = new SubtractionCounter(grid)
  const subtraction = rawFrames.map(e => counter.subtractFrame(e))

  const changeTab = (t) => () => setTab(t)

  return (
    <div className="bg-gray-100 min-w-screen min-h-screen pb-72 pt-4">
      <div className="mx-10">
        <ul className="w-full h-10 flex flex-row justify-evenly text-white font-bold">
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={changeTab('table')}>Table</li>
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={changeTab('frame')}>Frames</li>
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={changeTab('sub')}>Subtraction Forms</li>
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
                {rawFrames.map((e, i) =>
                  <Table key={i} data={useBinary ? e.binData : e.data}/>)}
              </div>
            </div>
            <div>
              <p className="text-center mb-4">Real</p>
              <div className="space-y-2">
                {frames.map((e, i) =>
                  <Table key={i} data={useBinary ? e.binData : e.data}/>)}
              </div>
            </div>
          </div>
        }
        {tab === 'sub' &&
          <div className="flex flex-row justify-evenly">
            <div>
              <p className="text-center mb-4">Raw</p>
              <div className="space-y-2">
                {rawFrames.map((e, i) =>
                  <Table key={i} data={useBinary ? e.binData : e.data}/>)}
              </div>
            </div>
            <div>
              <p className="text-center mb-4">Subtraction</p>
              <div className="space-y-2">
                {subtraction.map((e, i) =>
                  <Table key={i} data={e.data}/>)}
              </div>
            </div>
            <div>
              <p className="text-center mb-4">Remainder</p>
              <div className="space-y-2">
                <div className="flex flex-row space-x-2">
                  {counter.counterFrames().map((e, i) =>
                    <Table key={i} data={e}/>)}
                </div>
              </div>
            </div>
          </div>}
        <div className="fixed bottom-4 left-4">
          <Controls/>
          <p className="px-4">Sum: {grid.sum()}</p>
        </div>
      </div>
    </div>
  )
}

export default App
