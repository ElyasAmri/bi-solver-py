import type {BitRank, Bit, Table} from "../types";
import {getBitValue} from "../utils/helpers";
import Grid from "./Grid";

class Frame {
  public data: Table<number>;
  public binData: Table<Bit>;

  constructor(bit: BitRank, grid: Grid) {
    const bitValue = getBitValue(bit)
    this.data = []
    this.binData = []

    for (let i = 0; i < grid.w; i++) {
      const row = []
      const binRow: Bit[] = []
      for (let j = 0; j < grid.h; j++) {
        const v = parseInt(grid.binaryForm[i][j][grid.mx - bit - 1]) as Bit
        row.push(v * bitValue)
        binRow.push(v)
      }
      this.data.push(row)
      this.binData.push(binRow)
    }
  }
}

export default Frame