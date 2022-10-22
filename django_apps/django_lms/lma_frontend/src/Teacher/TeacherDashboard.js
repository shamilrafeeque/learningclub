import React from 'react'
import {Link} from 'react-router-dom'
import TeacherSidebar from '../Teacher/TeacherSidebar'
import {Routes,Route} from 'react-router-dom'
function TeacherDashboard() {
  return (
    <div className='container mt-4'>
        <div className='row'>
            <aside className='col-md-3'>
                <TeacherSidebar/>
            </aside>
            <section className='col-md-9'>
                dashboard
            </section>
        </div>
    </div>
  )
}

export default TeacherDashboard