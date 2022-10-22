import React from 'react'
import { Link } from 
"react-router-dom";
import TeacherSidebar from '../Teacher/TeacherSidebar'
function TeacherAddCourses() {
  return (
    <div className='container mt-4'>
        <div className='row'>
            <aside className='col-md-3'>
                <TeacherSidebar/>
            </aside>
            <section className='col-md-9'>
            <div className='card'>
                    <h5 className='card-header'>Add courses</h5>
                    <div className='card-body'>
                    <div className="mb-3 row">
                            <label for="inputPassword" className="col-sm-2 col-form-label">Title</label>
                            <div className="col-sm-10">
                            <input type="text" className="form-control" id="inputPassword"/>
                            </div>
                        </div>
                        <div className="mb-3 row">
                            <label for="inputPassword" className="col-sm-2 col-form-label">Description</label>
                            <div className="col-sm-10">
                            <input type="email" className="form-control" id="inputPassword"/>
                            </div>
                        </div>
                        <div className="mb-3 row">
                            <label for="inputPassword" className="col-sm-2 col-form-label">Course vedio</label>
                            <div className="col-sm-10">
                            <input type="file" className="form-control" id="inputPassword"/>
                            </div>
                        </div>
                        <div className="mb-3 row">
                            <label for="inputPassword" className="col-sm-2 col-form-label">Technologies</label>
                            <div className="col-sm-10">
                            <input type="text" className="form-control" id="inputPassword"/>
                            </div>
                        </div>
                        
                        <hr/>
                        <button className='btn btn-primary'>update</button>
                    </div>
                </div>
            </section>
        </div>
    </div>
  )
}

export default TeacherAddCourses