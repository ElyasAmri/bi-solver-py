import {Bit, BitRank, BitValue} from "../types"

const {pow, log2, floor} = Math

const containsBit = (x: number, b: BitRank) => {
  return (x & getBitValue(b)) as Bit
}

export const getBitValue = (x: BitRank) => {
  return pow(2, x) as BitValue

}

const bitRank = (x: BitValue) => {
  return log2(x) as BitRank
}

export const table = (w: number, h: number, v: any) => {
  return Array.from({length: w}, () =>
    Array.from({length: h}, () => v
    ))
}

export const array2d = (w: number, h: number, fn: (w: number, h: number) => any) => {
  return Array.from({length: w}, () =>
    Array.from({length: h}, fn))
}

const bits = (x: number) => {
  const max = floor(log2(x))
  return Array.from({length: max}, (_, i: number) => containsBit(x, i))
}