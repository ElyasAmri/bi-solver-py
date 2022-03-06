import _ from 'lodash'

class SubtractionCounter {
  constructor({w, h, l, mx}) {
    this.l = l
    this.mx = mx
    this.counter = []

    const binL = (parseInt(l)).toString(2).padStart(mx, '0')
    for (let i = 0; i < mx; i++) {
      if (binL[i] === '0')
        continue

      const val = mx - i - 1

      this.counter[val] = Array(w)
        .fill(0)
        .map(() => Array(h)
          .fill(0)
          .map(() => Math.pow(2, val))
        )
    }
  }

  subtractFrame(frame, w, h) {
    const frameCopy = _.cloneDeep(frame)
    const {data} = frameCopy
    const {counter} = this;
    for (const ce in counter) {
      for (let i = 0; i < w; i++) {
        for (let j = 0; j < h; j++) {
          let item = data[i][j]

          if (item === 0) continue
          let subtract = counter[ce][i][j]

          if (subtract <= item) {
            const tempItem = item
            item -= subtract
            subtract -= tempItem - item
          } else {
            subtract -= item
            item = 0
          }
          data[i][j] = item
          counter[ce][i][j] = subtract
        }
      }
    }

    return {
      action: frameCopy,
    }
  }
}

export default SubtractionCounter