//Constructor function
//Constructor function needs to start with an uppercase letter
//Constructor function comes into play when we make a new instance of the object
//Each new instance of the object has a its own copy of the properties and methods defined
//in the Constructor

function Book(name, pages){
  this.name = name;
  this.pages = pages;
  this.showDetails = function(){
    return `The name of the book is '${this.name}'. It has ${this.pages} pages`;
  }
}

//Instance of the Book object
let habit = new Book("The Power Of Habit", 450);
console.log(habit.showDetails());

//Another instance of the Book object
let roots = new Book("Roots", 671);
console.log(roots.showDetails());

/*Each instance of the book object has its own copy of the showDetails function*/
