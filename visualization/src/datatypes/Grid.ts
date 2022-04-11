import Frame from './Frame'
import {Bit, Table} from "../types";

const pos = (x: number) => x > 0 ? x : 0
const limit2 = (x: number) => Math.floor(Math.log2(x)) + 1

class Grid {
  public mx: number
  public data: Table<number>
  public binaryForm: Table<string>

  constructor(public w: number, public h: number, public l: number = 0, public t: number = 0) {
    this.mx = limit2(Math.max(w, h) - 1) + 1

    this.data = []

    this.initTable()
    this.binaryForm = this.toBinary()
  }

  initTable() {
    const {data, w, h, l} = this;
    for (let i = 0; i < w; i++) {
      const row = []
      for (let j = 0; j < h; j++) {
        row.push(pos((i ^ j) - l))
      }
      data.push(row)
    }
  }

  sum() {
    let ret = 0
    const {w, h, t, data} = this;
    for (let i = 0; i < w; i++) {
      for (let j = 0; j < h; j++) {
        ret += data[i][j]
      }
    }
    if (t === 0) {
      return ret
    }
    return ret % t
  }

  toBinary() {
    const ret = []
    const {data, mx, w, h} = this;

    for (let i = 0; i < w; i++) {
      const row = []
      for (let j = 0; j < h; j++) {

        row.push(data[i][j].toString(2).padStart(mx, '0'))
      }
      ret.push(row)
    }
    return ret
  }

  getFrames() {
    const {w, h, mx} = this
    if (w < 1 || h < 1) return []

    return Array(mx - 1)
      .fill(0)
      .map((_, i) => new Frame(i, this))
  }
}

export default Grid