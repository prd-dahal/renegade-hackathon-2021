
// const successCallback = (position)=>{
//     console.log(position)
// }
// const errorCallback =(error)=>{
//     console.error(error)
// }
// navigator.geolocation.getCurrentPosition(successCallback, errorCallback)

function getLocation(){
   
    const successCallback = (position)=>{
        
        url = "http://api.positionstack.com/v1/reverse?access_key=4d6e55aa54dbe32d7e0fcbc33b8b5c29&query="+position.coords.latitude+"," +position.coords.longitude
        const fetchData = async()=>{
            const response = await fetch(url)

            const data = await response.json()
            return data
        }
        fetchData().then((res)=>{

            
            document.getElementById("country").value = res.data[0].country
            document.getElementById("city").value = res.data[0].county
        })
    }
    const errorCallback = (error)=>{
        console.error(error)
    }
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback)
}