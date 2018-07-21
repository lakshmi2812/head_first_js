//To create methods and properties owned at the class level, we use prototype object
//Methods and properties defined on the prototype object are owned once and run many times
//When a new object instance is created, it does not get its own class method. It will
//instead refer to the method stored on the prototype only

//Let us consider the same Book class that we referred to before

function Book(name, pages){
  this.name = name;
  this.pages = pages;
}

Book.prototype.showDetails = function(){
  return `The name of the book is '${this.name}'. It has ${this.pages} pages`;
}

//Instance of the Book object
let habit = new Book("The Power Of Habit", 450); // create new object from constructor function using 'new' keyword
console.log(habit.showDetails());

//Another instance of the Book object
let roots = new Book("Roots", 671);
console.log(roots.showDetails());

/*
  The output will be exactly the same as that in 'understanding_constructor.js' in ch_9_objects folder
  But, each instance of the book object will not get its own copy of the 'showDetails' function
  It will instead refer to the method stored in the prototype object and run the method from there
  Quote from HeadFirstJavaScript:
   - Every object in JavsScript has a hidden object called prototype that exists as its property
   Note: Every instance of Book object will still get its own 'name' and 'pages' properties.
*/
