import React, { useEffect, useState } from 'react'
import './App.css'
import mockdata from './mockdata.json'

function App() {

  const [data, setData] = useState({})

  useEffect(() => {
    fetch('/api').then(
      response => response.json()
    ).then(resdata => {
      setData(resdata)
      console.log(resdata)
    })
  })

  return (
    <>
      <div>
        <img className='h-10' src={mockdata.account.avatar} alt="User Avatar" />
        <div dangerouslySetInnerHTML={{ __html: mockdata.content }} />
      </div>
    </>
  )
}

export default App
