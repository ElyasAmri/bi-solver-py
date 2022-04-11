import {FC, useState} from "react";
import Controls from "./components/Controls";
import Grid from './datatypes/Grid'
import SubtractionCounter from "./datatypes/SubtractionCounter";
import {useAppSelector} from "./utils/hooks";
import TableTab from "./tabs/TableTab";
import FramesTab from './tabs/FramesTab'
import SubtractionTab from './tabs/SubtractionTab'
import FreeTableTab from './tabs/FreeTableTab'


type Tab = 'table' | 'frame' | 'sub' | 'extra'

// noinspection JSUnusedGlobalSymbols
function App() {
  const {width, height, subtract, modulus, useBinary} = useAppSelector(state => state.table)
  const [tab, setTab] = useState<Tab>('table')

  const grid = new Grid(width, height, subtract, modulus)

  const isGridSimple = subtract === 0 && modulus === 0

  const rawGrid = isGridSimple ? grid : new Grid(width, height, 0, 0)

  const frames = grid.getFrames()
  const rawFrames = isGridSimple ? frames : rawGrid.getFrames()

  const counter = SubtractionCounter.createFromGrid(grid)
  const subtraction = rawFrames.map(e => counter.subtractFrame(e))

  const changeTab = (t: Tab) => () => setTab(t)

  const tabContainer = {
    'table': <TableTab grid={grid} rawGrid={rawGrid}/>,
    'frame': <FramesTab frames={frames} rawFrames={rawFrames} useBinary={useBinary}/>,
    'sub': <SubtractionTab frames={frames} rawFrames={rawFrames} useBinary={useBinary} counter={counter} subtraction={subtraction}/>,
    'extra': <FreeTableTab width={width} height={height}/>,
  }

  return (
    <div className="bg-gray-100 min-w-screen min-h-screen pb-72 pt-4">
      <div className="mx-10">
        <ul className="w-full h-10 flex flex-row justify-evenly text-white font-bold">
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={changeTab('table')}>Table</li>
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={changeTab('frame')}>Frames</li>
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={changeTab('sub')}>Subtraction Forms</li>
          <li className="bg-purple-600 rounded-md h-6 px-2" onClick={changeTab('extra')}>Free Table</li>
        </ul>
        <hr className="mb-4"/>
        {tabContainer[tab]}
        <div className="fixed bottom-4 left-4">
          <Controls/>
          <p className="px-4">Sum: {grid.sum()}</p>
        </div>
      </div>
    </div>
  )
}

export default App
