//Script for determining which videos to show improvement area/ improvement text
var subject = document.getElementById('subjectname').textContent.toLowerCase().replaceAll(" ","");

const math = ['<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/M9Rrf9-yWxw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/CAtw6yDRPe4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/AEtk2xNQlno" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/wUlZjCYIVsE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>','math'];
const computerscience = ['<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/b4pCjnAE7zk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>, <iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/f7JwN0gr_ww" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/f7JwN0gr_ww" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen ></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/f7JwN0gr_ww" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen ></iframe>', '<iframe style="width: 100%; height: 25vh;" src="https://www.youtube.com/embed/C6jVcqBacO8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>','computerscience'];
const individualsandsocieties = ['individualsandsocieties'];
const chinese = [0,0,0,0,'chinese'];
const english = [0,0,0,0,'english'];
const science = [0,0,0,0,'science'];
const music = [0,0,0,0,'music'];
const visualarts = ['visualarts'];
const designtechnology = ['designtechnology'];

const mathfb = [];
const computersciencefb = [];
const individualsandsocietiesfb = [];
const chinesefb = [];
const englishfb = [];
const sciencefb = [];
const musicfb = [];
const visualartsfb = [];
const designtechnologyfb = [];

const videoarray = [math, computerscience, individualsandsocieties, chinese, english, science, music, visualarts, designtechnology];
const feedbackarray = [];
//Find weakest criterion:
var criterionavgtemp = document.getElementById('criterionavg').textContent.replaceAll(" ", "").replaceAll("[", "").replaceAll("]", "").split(',');
var criterionavg = [];
for(grade in criterionavgtemp) {
    criterionavg.push(parseFloat(criterionavgtemp[grade]));
}
var weakcrit = Math.min.apply(Math,criterionavg);
var weakcritindex = 0;

for(grade in criterionavg){
    if(criterionavg[grade] == weakcrit){
        weakcritindex = grade;
        break;
    }
}

for(item in videoarray){
    if(subject == videoarray[item].slice(-1))
        document.getElementById("video").innerHTML += videoarray[item][weakcritindex];
        console.log(videoarray[item][weakcritindex]);
}

