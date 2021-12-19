const handleScroll = () => {
  if (window.scrollY > 0) {
    document.querySelector(".navbar").classList.add("active__navbar");
    document.querySelector(".link").classList.add("active__link");
  } else {
    document.querySelector(".navbar").classList.remove("active__navbar");
    document.querySelector(".link").classList.add("active__link");
  }
};
window.addEventListener("scroll", handleScroll);

// handleScroll();
