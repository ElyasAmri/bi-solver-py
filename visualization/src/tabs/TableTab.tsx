import Table from "../components/Table";
import Grid from "../datatypes/Grid";

type Props = {
  grid: Grid
  rawGrid: Grid
}

const TableTab = ({grid, rawGrid}: Props) => {
  return (
    <div className="flex flex-row justify-evenly">
      <div>
        <Table data={rawGrid.data}/>
      </div>
      <div>
        <Table data={grid.data}/>
      </div>
    </div>
  );
};

export default TableTab;