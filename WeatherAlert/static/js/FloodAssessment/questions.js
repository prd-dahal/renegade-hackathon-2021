

var thisquestion = "A"
function handleNextQuestion(s){
    $.getJSON("{% static 'js/FloodAssessment/questions.json'%}", function(jd){
        if(s=='yes'){
            thisquestion = jd.config[thisquestion][0]
             
        }else{
            thisquestion = jd.config[thisquestion][1] 
        }
        

        if (!parseFloat(thisquestion)){
            
            jd.questions.forEach((data)=>{
                if (data.name == thisquestion){
                    $(".questiontitle").html(data.question)
                }
            })        
        }
        else{
            console.log(thisquestion)
            $(".questionDiv").hide()
            $(".answer").css('display','block')
            $(".answer").append("<p> It has "+thisquestion+" risk factor</p>")
        }
    })
}
$(document).ready(()=>{
    
    $.getJSON("{% static 'js/FloodAssessment/questions.json'%}", function (jd){
        $(".questionDiv").css("display","block")
        $(".questiontitle").append(jd.questions[0].question)
        
    })
})