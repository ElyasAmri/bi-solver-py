import Table from "../components/Table";
import Frame from "../datatypes/Frame";
import SubtractionCounter from "../datatypes/SubtractionCounter";

type Props = {
  frames: Frame[]
  rawFrames: Frame[]
  counter: SubtractionCounter
  subtraction: Frame[]
  useBinary: boolean
}

const SubtractionTab = ({frames, rawFrames, counter, subtraction, useBinary}: Props) => {
  return (
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
        <p className="text-center mb-4">Raw</p>
        <div className="space-y-2">
          {frames.map((e, i) =>
            <Table key={i} data={useBinary ? e.binData : e.data}/>)}
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
    </div>
  );
};

export default SubtractionTab;