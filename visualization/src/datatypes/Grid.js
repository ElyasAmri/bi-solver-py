class Grid {
  constructor(w, h, l = 0, t = false) {
    this.w = w
    this.h = h
    this.l = l
    this.t = t

    this.data = []

    this.initTable()
  }

  initTable() {
    for (let i = 0; i < this.w; i++) {
      const row = []
      for (let j = 0; j < this.h; j++) {
        row.push((i ^ j) - this.l)
      }
      this.data.push(row)
    }
  }

  sum() {
    let ret = 0
    const {h, data, t, w} = this;
    for (let i = 0; i < w; i++) {
      for (let j = 0; j < h; j++) {
        ret += data[i][j]
      }
    }
    if (!t) {
      return ret % t
    }
    return ret
  }
}

export default Grid