import _ from 'lodash'
import Grid from "./Grid";
import Frame from "./Frame";

class SubtractionCounter {
  public counter: {[deg: number]: any[]};

  constructor(public w: number, public h: number, public l: number, public mx: number) {
    this.counter = {}

    for (let i = 0; i < mx; i++) {
      const val = mx - i - 1
      const bv = Math.pow(2, val)
      const fill = bv & l ? Math.pow(2, val) : 0
      this.counter[val] = Array(w)
        .fill(0)
        .map(() => Array(h).fill(fill))
    }
  }

  static createFromGrid(grid: Grid) {
    return new SubtractionCounter(grid.w, grid.h, grid.l, grid.mx)
  }

  subtractFrame(frame: Frame) {
    const frameCopy = _.cloneDeep(frame)
    const {data} = frameCopy
    const {counter, w, h} = this;
    for (let cf in counter) {
      let f = parseInt(cf)
      for (let i = 0; i < w; i++) {
        for (let j = 0; j < h; j++) {
          let item = data[i][j]

          if (item === 0)
            continue

          let subtract = counter[f][i][j]
          if (subtract <= item) {
            const tempItem = item
            item -= subtract
            subtract -= tempItem - item
          } else {
            subtract -= item
            item = 0
          }
          data[i][j] = item
          counter[f][i][j] = subtract
        }
      }
    }

    return frameCopy
  }

  counterFrames() {
    const {counter, w, h} = this
    const newCounter = []

    for (const cf in counter) {
      let f = parseInt(cf)
      const newCounterFrame = []
      const bv = Math.pow(2, f)
      for (let i = 0; i < w; i++) {
        const newCounterFrameRow = []
        for (let j = 0; j < h; j++) {
          const item = counter[f][i][j]
          if (item === bv || item === 0) {
            newCounterFrameRow.push(item)
            continue
          }
          newCounterFrameRow.push(0)
          for (const ck in counter) {
            let k = parseInt(ck)
            if (k < f)
              break
            const sbv = Math.pow(2, k)
            // noinspection JSBitwiseOperatorUsage
            if (sbv & item)
              newCounter[k][i][j] = sbv
          }
        }
        newCounterFrame.push(newCounterFrameRow)
      }
      newCounter.push(newCounterFrame)
    }
    return newCounter
  }
}

export default SubtractionCounter