var currentFlashcardIndex = 1;

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
  flashcards[currentFlashcardIndex - 1].style.display = "block";
}

// Call showFlashcard initially to display the first flashcard
showFlashcard(0);

function prevFlashcard() {
  showFlashcard(-1);
}

function nextFlashcard() {
  showFlashcard(1);
}
