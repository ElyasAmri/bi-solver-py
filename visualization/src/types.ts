// BitValue is 2 to the power of the BitRank
export type BitValue = number

// BitRank is the rank of bit, starting from 0
export type BitRank = number

export type Bit = One | Zero
export type One = 1
export type Zero = 0

export type Table<T> = T[][]
export type ValueTable = Table<BitValue>
export type BitTable = Table<Bit>

export type Explict<T> = T
