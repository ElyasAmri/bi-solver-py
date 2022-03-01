function Table({data}) {

  return (
    <div className="max-w-min flex flex-row leading-none divide-x-2 divide-gray-300 border-2 border-gray-300">
      {data.map((row, x) =>
        <div key={x} className="divide-y-2 divide-gray-300 flex flex-col">
          {row.map((item, y) =>
            <span key={y}>
              {item}
            </span>)}
        </div>)}
    </div>
  )
}

export default Table