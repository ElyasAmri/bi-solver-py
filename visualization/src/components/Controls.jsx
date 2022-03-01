import {useState} from "react";

function Controls() {
  const [width, setWidth] = useState(10)
  const [height, setHeight] = useState(10)
  const [subtract, setSubtract] = useState(0)
  const [useSubtract, setUseSubtract] = useState(false)
  const [modulus, setModulus] = useState(0)
  const [useModulus, setUseModulus] = useState(false)

  return (
    <div className="flex flex-row mt-4 border border-black rounded-md max-w-max px-6 py-2">
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
        <input className="h-6" id="width" type="number" value={width} onChange={e => setWidth(e.target.value)}/>
        <input className="h-6" id="height" type="number" value={height} onChange={e => setHeight(e.target.value)}/>
        <input className="h-6" id="use-subtract" type="checkbox" checked={useSubtract}
               onClick={() => setUseSubtract(!useSubtract)}/>
        {useSubtract &&
          <input className="h-6" id="subtract" type="number" value={subtract} onChange={e => setSubtract(e.target.value)}/>
        }
        <input className="h-6" id="use-modulus" type="checkbox" checked={useModulus}
               onClick={() => setUseModulus(!useModulus)}/>
        {useModulus &&
          <input className="h-6" id="modulus" type="number" value={modulus} onChange={e => setModulus(e.target.value)}/>
        }
      </div>
    </div>
  )
}

export default Controls