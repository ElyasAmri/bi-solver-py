import Table from "../components/Table";
import Frame from "../datatypes/Frame";

type Props = {
  frames: Frame[]
  rawFrames: Frame[]
  useBinary: boolean
}

const FramesTab = ({frames, rawFrames, useBinary}: Props) => {
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
        <p className="text-center mb-4">Real</p>
        <div className="space-y-2">
          {frames.map((e, i) =>
            <Table key={i} data={useBinary ? e.binData : e.data}/>)}
        </div>
      </div>
    </div>
  );
};

export default FramesTab;