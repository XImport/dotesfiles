function search() {
  query = document.getElementById("googleBox").value;
  url = "http://www.google.com/search?q=" + query;
  window.open(url, "_blank");
}
