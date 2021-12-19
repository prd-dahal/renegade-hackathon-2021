function geoLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(success, error);
  } else {
    alert("Geolocation not supported by browser");
  }
}

async function success(pos) {
  const lat = pos.coords.latitude;
  const long = pos.coords.longitude;

  let params = { lat, long };

  fetch(
    `http://api.weatherapi.com/v1/current.json?key=8d86a57d9053408f9a0190650211812&q=nepal&lat=${lat}&lon=${long}`
  )
    .then((response) => response.json())
    .then((res) => {
      console.log(res);
      const current = res.current;
      const temp = current.temp_c;
      const windspeed = current.wind_kph;
      const gust = current.gust_kph;

      document.querySelector(".temp__num").innerHTML = temp;
      document.querySelector(".weather__wind").innerHTML = windspeed + " km/hr";
      document.querySelector(".weather__prediction").innerHTML = gust + " km/hr";
    })
    .catch((err) => {
      console.error(err);
    });

  // await fetch(
  //   `https://www.7timer.info/bin/astro.php?lon=${long}&lat=${lat}&ac=0&unit=metric&output=json&tzshift=0`,
  //   {
  //     method: "GET",
  //   }
  // )
  //   .then((response) => {
  //     console.log(response.data);

  //     document.querySelector(".temp__num").innerHTML =
  //       response.dataseries[0].temp2m;

  //     document.querySelector(".weather__wind").innerHTML =
  //       response.dataseries[0].wind10m.speed;

  //     document.querySelector(".weather__prediction").innerHTML =
  //       response.dataseries[0].prec_type;
  //   })
  //   .catch((err) => {
  //     console.error(err);
  //   });
  //   alert(`lat: ${lat}, long:${long}`);
}

function error() {
  alert("Geolocator failed");
}

geoLocation();

// document.querySelector(".temp__num").innerHTML = 17;