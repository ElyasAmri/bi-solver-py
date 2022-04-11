import Frame from './Frame'

const pos = x => x > 0 ? x : 0
const limit2 = x => Math.floor(Math.log2(x)) + 1

class Grid {
  constructor(w, h, l = 0, t = 0) {
    this.w = w
    this.h = h
    this.l = l
    this.t = t
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
    const {data, mx} = this;

    for (let i = 0; i < this.w; i++) {
      const row = []
      for (let j = 0; j < this.h; j++) {

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