//Script for determining which videos to show improvement area/ improvement text
var subject = document.getElementById('subjectname').textContent.toLowerCase().replaceAll(" ","");
console.log(subject)

const math = ['<iframe width="560" height="315" src="https://www.youtube.com/embed/M9Rrf9-yWxw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', '<iframe width="560" height="315" src="https://www.youtube.com/embed/CAtw6yDRPe4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', '<iframe width="560" height="315" src="https://www.youtube.com/embed/AEtk2xNQlno" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', '<iframe width="560" height="315" src="https://www.youtube.com/embed/wUlZjCYIVsE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'];
const computerscience = ['<iframe width="560" height="315" src="https://www.youtube.com/embed/b4pCjnAE7zk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>, <iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/f7JwN0gr_ww" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/f7JwN0gr_ww" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen ></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/f7JwN0gr_ww" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen ></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/C6jVcqBacO8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'];
const individualsandsocieties = [];
const chinese = [];
const english = [];
const science = [];
const music = [];
const visualarts = [];
const designtechnology = [];




