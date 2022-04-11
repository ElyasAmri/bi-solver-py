class Frame {
  constructor(bit, grid) {
    const bitValue = Math.pow(2, bit)
    this.data = []
    this.binData = []

    for (let i = 0; i < grid.w; i++) {
      const row = []
      const binRow = []
      for (let j = 0; j < grid.h; j++) {
        const v = parseInt(grid.binaryForm[i][j][grid.mx - bit - 1])
        row.push(v * bitValue)
        binRow.push(v)
      }
      this.data.push(row)
      this.binData.push(binRow)
    }
  }
}

export default Frame