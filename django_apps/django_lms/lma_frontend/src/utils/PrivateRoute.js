import { useContext } from "react";
import { Route, Routes,useNavigate ,Navigate, Outlet} from "react-router-dom";
import AuthContext from "../context/AuthContext";

const PrivateRoute = () =>{
    // const authenticated = false
    let {user} = useContext(AuthContext)
     return(
        // <Routes>
        //      <Route {...rest}>{!authenticated? Navigate('/login'):children}</Route>
        // </Routes>
        user&&user.is_superuser?<Outlet/>:<Navigate replace to='/'></Navigate>
     )
}

export default PrivateRoute;
