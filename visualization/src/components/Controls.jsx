import {useDispatch, useSelector} from "react-redux";
import {
  changeSubtract,
  changeUseSubtract,
  changeUseModulus,
  changeHeight,
  changeModulus,
  changeWidth,
} from "../store";

function Controls() {
  const dispatch = useDispatch()
  const {width, height, subtract, useSubtract, modulus, useModulus} = useSelector(state => state.table)

  return (
    <div className="flex flex-row mt-4 border border-black rounded-md max-w-max px-6 py-2 bg-blue-400">
      <div className="flex flex-col space-y-2">
        <label className="h-6" htmlFor="width">Width</label>
        <label className="h-6" htmlFor="height">Height</label>
        <label className="h-6" htmlFor="use-subtract">Use Subtract</label>
        {useSubtract &&
          <label className="h-6" htmlFor="subtract">Subtract</label>
        }
        <label className="h-6" htmlFor="use-modulus">Use Modulus</label>
        {useModulus &&
          <label className="h-6" htmlFor="modulus">Modulus</label>
        }
      </div>

      <div className="ml-4 flex flex-col space-y-2">
        <input className="h-6" id="width" type="number" value={width}
               onChange={e => dispatch(changeWidth(e.target.value))}/>
        <input className="h-6" id="height" type="number" value={height}
               onChange={e => dispatch(changeHeight(e.target.value))}/>
        <input className="h-6" id="use-subtract" type="checkbox" checked={useSubtract}
               onChange={() => dispatch(changeUseSubtract(!useSubtract))}/>
        {useSubtract &&
          <input className="h-6" id="subtract" type="number" value={subtract}
                 onChange={e => dispatch(changeSubtract(e.target.value))}/>
        }
        <input className="h-6" id="use-modulus" type="checkbox" checked={useModulus}
               onChange={() => dispatch(changeUseModulus(!useModulus))}/>
        {useModulus &&
          <input className="h-6" id="modulus" type="number" value={modulus}
                 onChange={e => dispatch(changeModulus(e.target.value))}/>
        }
      </div>
    </div>
  )
}

export default Controls