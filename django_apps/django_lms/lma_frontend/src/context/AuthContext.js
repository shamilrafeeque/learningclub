import jwt_decode from  'jwt-decode';
import {createContext,useState} from 'react'
import { useNavigate } from 'react-router-dom';
import axios from '../utils/axios';
// import { applyAuthTokenInterceptor } from 'axios-jwt';


const AuthContext=createContext()

export default AuthContext;

export const AuthProvider =({children})=>{
    let [user,setUser] = useState(()=>localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null)
    let [authTokens,setAuthTokens] = useState(()=>localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
    let navigate = useNavigate();
    let [resData,setResData] = useState()
    let [signupResError,setSignupResError] = useState()
    let [signupResSuccess,setSignupResSuccess]= useState()
    let [loading,setLoading] = useState()

const BASE_URL='http://127.0.0.1:8000/'
const axiosInstance = axios.create({ baseURL: BASE_URL })
console.log(BASE_URL)
// const requestRefresh = async (refresh) => {
//     return axios.post(`${BASE_URL}api/acounts/token/refresh/b`, { refresh })
//     .then((response) => 
//     localStorage.setItem('authTokens',JSON.stringify(response.data.access_token)))
// };

// applyAuthTokenInterceptor(axiosInstance, { requestRefresh });  // Notice that this uses the axiosInstance instance.  <-- important


let SignupUser=async(username,email,password,bio,mobile,interests)=>{
    await axios.post('http://127.0.0.1:8000/api/acounts/register/',{username:username,
        email:email,
        password:password,
        bio:bio,
        mobile:mobile,
        interests:interests}).then((response)=>{
        console.log("innser signup user")
        console.log(username)
        console.log(response.status)
        console.log(response.data)
        
        if (response.status===201){
            console.log('authcontecy')
            setSignupResSuccess('User registered successfully, Please verify with OTP')
            navigate('/user-login')
    }else{
        setSignupResError(response.data)
        console.log("not register erro")
    }
    })
}
let loginUser = async (email,password) =>{
    setLoading(true)
    let response = await fetch('http://127.0.0.1:8000/api/acounts/token/',{
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'email':email,'password':password})
    })
    let data = await response.json()
    if (response.status === 200){
        setLoading(false)
        setAuthTokens(data)
        const a=setUser(jwt_decode(data.access))
        console.log(a)
        console.log(data.access)
        console.log(user)
        console.log(user.user_id)
        if (user.user_id==1){
            navigate('/admins')
        }else{
            navigate('/')
        }
        localStorage.setItem('authTokens',JSON.stringify(data))
        // console.log(response.user_id)
        // if (response.user_id==1){
        //     navigate('/admins')
        // } else{
        //     navigate('/')
        // }
           
       

       
    }else{
        setLoading(false)
        setResData('Invalid password or There is no account existing for this email.')
        
    }
}


let logoutUser=()=>{
    setAuthTokens(null)
    setUser(null)
    localStorage.removeItem('authTokens')
    setUser(null)
    console.log('logouuuuuuuuuuuutttttttttt')
    navigate('/register')
}







let contextData = {
    SignupUser:SignupUser,
    // authTokens:authTokens,
    signupResSuccess:signupResSuccess,
    signupResError:signupResError,
    loginUser:loginUser,
    user:user,
    logoutUser:logoutUser,
}
return (
    <AuthContext.Provider value={contextData}>
        {children}
    </AuthContext.Provider>
)
}