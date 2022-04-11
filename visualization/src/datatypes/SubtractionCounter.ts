import _ from 'lodash'

class SubtractionCounter {
  constructor({w, h, l, mx}) {
    this.w = w
    this.h = h
    this.mx = mx
    this.counter = {}

    for (let i = 0; i < mx; i++) {
      const val = mx - i - 1
      const bv = Math.pow(2, val)
      // noinspection JSBitwiseOperatorUsage
      const fill = bv & l ? Math.pow(2, val) : 0
      this.counter[val] = Array(w)
        .fill(0)
        .map(() => Array(h).fill(fill))
    }
  }

  subtractFrame(frame) {
    const frameCopy = _.cloneDeep(frame)
    const {data} = frameCopy
    const {counter, w, h} = this;
    for (let f in counter) {
      f = parseInt(f)
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

    for (const f in counter) {
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
          for (const k in counter) {
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