 $(document).ready(function(){
          $("#c").append($('#culturaEmpreendedora').html());
          $("#indicadores").focus();
            
        
        //Mudando a opcaidade das outras imagens
        $("#inovacao").css({ opacity: 0.5 });
        $("#extensao").css({ opacity: 0.5 });
        $("#infraestrutura").css({ opacity: 0.5 });
        $("#internacionalizacao").css({ opacity: 0.5 });
        $("#capital").css({ opacity: 0.5 });
      });
      
    $("#cultura a").click(function(){
        $("#c").focus();
        $("#c").html(''); 
        $("#c").append($('#culturaEmpreendedora').html());
        $("#cultura").css({ opacity: 1});
        $("#inovacao").css({ opacity: 0.5 });
        $("#extensao").css({ opacity: 0.5 });
        $("#infraestrutura").css({ opacity: 0.5 });
        $("#internacionalizacao").css({ opacity: 0.5 });
        $("#capital").css({ opacity: 0.5 });
        
    });
    //carrega o conteudo de inovação
     $("#inovacao a").click(function(){
        $("#c").focus();
        $("#c").html(''); 
        $("#c").append($('#Inovacao').html());
        $("#cultura").css({ opacity: 0.5});
        $("#inovacao").css({ opacity: 1 });
        $("#extensao").css({ opacity: 0.5 });
        $("#infraestrutura").css({ opacity: 0.5 });
        $("#internacionalizacao").css({ opacity: 0.5 });
        $("#capital").css({ opacity: 0.5 });
        
    });
    
    //carrega o conteudo de extensao
    $("#extensao a").click(function(){
        $("#c").html(''); 
        $("#c").append($('#Extensao').html());
        $("#cultura").css({ opacity: 0.5});
        $("#inovacao").css({ opacity: 0.5 });
        $("#extensao").css({ opacity: 1 });
        $("#infraestrutura").css({ opacity: 0.5 });
        $("#internacionalizacao").css({ opacity: 0.5 });
        $("#capital").css({ opacity: 0.5 });
    });
    
     //carrega o conteudo de infraestrutura
    $("#infraestrutura a").click(function(){
        $("#c").html(''); 
        $("#c").append($('#Infraestrutura').html());
        $("#cultura").css({ opacity: 0.5});
        $("#inovacao").css({ opacity: 0.5 });
        $("#extensao").css({ opacity: 0.5 });
        $("#infraestrutura").css({ opacity: 1 });
        $("#internacionalizacao").css({ opacity: 0.5 });
        $("#capital").css({ opacity: 0.5 });
    });
    
     //carrega o conteudo de internacionalização
    $("#internacionalizacao a").click(function(){
        $("#c").html(''); 
        $("#c").append($('#Internacionalizacao').html());
        $("#cultura").css({ opacity: 0.5});
        $("#inovacao").css({ opacity: 0.5 });
        $("#extensao").css({ opacity: 0.5 });
        $("#infraestrutura").css({ opacity: 0.5 });
        $("#internacionalizacao").css({ opacity: 1 });
        $("#capital").css({ opacity: 0.5 });
    });
    
     //carrega o conteudo de capital financeiro
    $("#capital a").click(function(){
        $("#c").html(''); 
        $("#c").append($('#CapitalFinanceiro').html());
        $("#cultura").css({ opacity: 0.5});
        $("#inovacao").css({ opacity: 0.5 });
        $("#extensao").css({ opacity: 0.5 });
        $("#infraestrutura").css({ opacity: 0.5 });
        $("#internacionalizacao").css({ opacity: 0.5 });
        $("#capital").css({ opacity: 1 });
    });

