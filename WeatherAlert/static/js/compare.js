handleKeyPress = (e) => {
    if (e.key === "Enter") {
      const locationinput = document.querySelector(".input__first").value;
      const locationinputtwo = document.querySelector(".input__second").value;
  
      fetch(
        `http://api.weatherapi.com/v1/current.json?key=8d86a57d9053408f9a0190650211812&q=${locationinput}`
      )
        .then((response) => response.json())
        .then((res) => {
          const current = res.current;
          const temp = current.temp_c;
          const windspeed = current.wind_kph;
          const gust = current.gust_kph;
  
          document.getElementById("first_temp").innerHTML = temp + " degree celcius";
          document.getElementById("first_wind_speed").innerHTML = windspeed +" km/hr";
          document.getElementById("first_wind_gust").innerHTML = gust + " km/hr";
        })
        .catch((err) => {
          console.error(err);
        });
  
      if (locationinputtwo.length > 0) {
        fetch(
          `http://api.weatherapi.com/v1/current.json?key=8d86a57d9053408f9a0190650211812&q=${locationinputtwo}`
        )
          .then((response) => response.json())
          .then((res) => {
            const current = res.current;
            const temp = current.temp_c;
            const windspeed = current.wind_kph;
            const gust = current.gust_kph;
  
            document.getElementById("second_temp").innerHTML = temp + " degree celcius";
            document.getElementById("second_wind_speed").innerHTML = windspeed+" km/hr";
            document.getElementById("second_wind_gust").innerHTML = gust+ " km/hr";
          })
          .catch((err) => {
            console.error(err);
            alert("Error could not fetch");
          });
      }
    }
  };
  
  window.addEventListener("keypress", handleKeyPress);