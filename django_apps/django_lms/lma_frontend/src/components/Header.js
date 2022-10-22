import React,{useContext} from 'react'
import {Link} from 'react-router-dom'
import AuthContext from '../context/AuthContext'
// import { useContext } from 'react'

function Header() {
  const teacherLoginStatus=localStorage.getItem('teacherLoginStatus')
  const userLoginStatus=localStorage.getItem('authTokens')
  const{user,logoutUser}=useContext(AuthContext)
  return (
    <nav className="navbar navbar-expand-lg bg-dark navbar-dark">
  <div className="container">
    <Link className="navbar-brand" to="/">LearnOn</Link>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div className="navbar-nav ms-auto">
        <Link className="nav-link active" aria-current="page" to="/">Home</Link>
        <a className="nav-link" href="#">Courses</a>
        {/*  ssName="nav-link" to="/admins">Admin</Link> */}

        {/* <a className="nav-link" href="#">Teachers</a> */}
        <li className="nav-item dropdown">
          <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Teacher
          </a>
          
          <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
            {teacherLoginStatus!='true'&&
            <>
                  <li><Link className="dropdown-item" to="/teacher-login">login</Link></li>
                  <li><Link className="dropdown-item" to="/teacher-register">
                    Register</Link></li></>
              }
            
            <li><hr className="dropdown-divider"/></li>
            <li><Link className="dropdown-item" to="/teacher-dashboard">
                          Dashboard</Link></li>
        
            <li><Link className="dropdown-item" >Logout</Link></li>
          </ul>
        </li>
        <li className="nav-item dropdown">
          <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            User
          </a>
          <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
              {userLoginStatus==null && 
              <>
              <li><Link className="dropdown-item" to="/user-login">login</Link></li>
              <li><Link className="dropdown-item" to="/user-register">
              Register</Link></li></>}
          <>
            <li><hr className="dropdown-divider"/></li>
            <li><Link className="dropdown-item" to="/user-dashboard">
                 Dashboard</Link></li>
            <li><a className="dropdown-item" onClick={logoutUser}>Logout</a></li></>
          </ul>
        </li>
        
        
        {/* <a className="nav-link disabled">Disabled</a> */}
      </div>
    </div>
  </div>
</nav>
  );
}

export default Header;