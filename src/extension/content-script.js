// content.js

// console.log("Hello world !")
// const articles = document.querySelectorAll('article');
// articles.forEach((article, index) => {
// });

function processArticles(articles){
    console.log(articles);
    articles.forEach(article => {
        article.style.border = '2px solid red'; // Apply a red border to each article for visibility
        var link = article.querySelector(':scope > a');
        console.log(link.textContent);
        console.log(link.href);
    })
}

const initialArticles = document.querySelectorAll('article');
processArticles(initialArticles);


// Set up a MutationObserver to watch for newly added article elements
const observer = new MutationObserver((mutations) => {
    console.log("mutations");
    console.log(mutations)
    mutations.forEach((mutation) => {
      mutation.addedNodes.forEach((node) => {
        console.log("added node");
        console.log(node);
        // if (node.nodeType === Node.ELEMENT_NODE && node.tagName.toLowerCase() === 'article') {
        //   // Process the newly added article
        //   processArticles([node]);
        // }
      });
    });
  });

observer.observe(document.body, { childList: true, subtree: true });

  