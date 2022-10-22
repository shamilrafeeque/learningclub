import React from 'react'
import {Link} from 'react-router-dom'
import TeacherSidebar from './TeacherSidebar'
function TeacherUsers() {
  return (
    <div className='container mt-4'>
        <div className='row'>
            <aside className='col-md-3'>
                <TeacherSidebar/>
            </aside>
            <section className='col-md-9'>
            <div className='card'>
    <h5 className='card-header'>Users List</h5>
    <div className='card-body'>
        <table className='table table-bordered'>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Enrolled Cousre</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <td>John</td>
                <td><Link to="/">React</Link></td>
                <td>
                    <button className='btn btn-primary btn-danger active btn-sm'>Delete</button>
                </td>
            </tbody>
        </table>
        
    </div>
</div>
            </section>
        </div>
    </div>
  )
}

export default TeacherUsers