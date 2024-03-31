var currentFlashcardIndex = 1;
var currentIndex = 1;

function showFlashcard(indexChange) {
  const flashcards = document.getElementsByClassName("flashcards");
  const flashcardCount = flashcards.length;

  // Update current index with boundaries and handle no flashcards case
  if (flashcardCount === 0) {
    alert("There are no flashcards to display.");
    return;
  }
  currentFlashcardIndex = Math.max(Math.min(currentFlashcardIndex + indexChange, flashcardCount), 1);

  // Hide all flashcards
  for (let i = 0; i < flashcardCount; i++) {
    flashcards[i].style.display = "none";
  }

  // Show the current flashcard
  flashcards[currentFlashcardIndex - 1].style.display = "";
}

function showIndex(indexChange) {
  const indexes = document.getElementsByClassName("indexes");
  const indexCount = indexes.length;

  // Update current index with boundaries and handle no flashcards case
  if (indexCount === 0) {
    // alert("There are no flashcards to display.");
    return;
  }
  currentIndex = Math.max(Math.min(currentIndex + indexChange, indexCount), 1);

  // Hide all indexes
  for (let i = 0; i < indexCount; i++) {
    indexes[i].style.display = "none";
  }

  // Show the current flashcard
  indexes[currentIndex - 1].style.display = "";
}

// Call showFlashcard initially to display the first flashcard
showFlashcard(0);
showIndex(0);

function prevFlashcard() {
  showFlashcard(-1);
  showIndex(-1);
}

function nextFlashcard() {
  showFlashcard(1);
  showIndex(1);
}