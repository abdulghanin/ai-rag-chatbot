(function(){

const iframe=document.createElement("iframe")

iframe.src="http://localhost:8080"

iframe.style.position="fixed"
iframe.style.bottom="20px"
iframe.style.right="20px"
iframe.style.width="400px"
iframe.style.height="600px"
iframe.style.border="none"
iframe.style.borderRadius="14px"
iframe.style.boxShadow="0 10px 40px rgba(0,0,0,0.2)"

document.body.appendChild(iframe)

})();