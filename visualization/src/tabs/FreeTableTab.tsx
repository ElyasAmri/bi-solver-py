import Table from '../components/Table'
import {useState} from 'react'
import {table} from '../utils/helpers'

type Props = {
  width: number
  height: number
}

const FreeTableTab = ({width, height}: Props) => {
  const [inputs, setInputs] = useState(table(width, height, 0))

  const changeInput = (x: number, y: number) => (v: number) => {
    const copy = [...inputs]
    copy[x][y] = v
    setInputs(copy)
  }

  return (
    <div className="flex flex-row justify-evenly">
      <div className="flex flex-row">
        {inputs && inputs.length && Array.from({length: width}, (_, i) =>
          <div key={i} className="flex flex-col justify-evenly">
            {Array.from({length: height}, (_, j) =>
              <input className="block border w-10" key={j} value={inputs[i][j]} type="number"
                     min={0} onChange={({target}) => changeInput(i, j)(parseInt(target.value))}/>,
            )}
          </div>
        )}
      </div>
      <div>
        <Table data={inputs}/>
      </div>
    </div>
  )
}

export default FreeTableTab