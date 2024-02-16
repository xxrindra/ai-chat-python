// Define an array of possible chat bot responses
const chatBotResponses = [
  "Hello! How can I assist you today?",
  "Tell me more about yourself.",
  "What's your favorite color?",
  "I'm a friendly chat bot!",
  "Ask me anything!",
  "How's the weather where you are?",
  // Add more responses as needed
];

// Function to generate a random chat bot response
function getRandomResponse() {
  const randomIndex = Math.floor(Math.random() * chatBotResponses.length);
  return chatBotResponses[randomIndex];
}

// Example usage: Call this function to get a random response
const userMessage = "Hi, chat bot!";
const chatBotResponse = getRandomResponse();
console.log(`User: ${userMessage}`);
console.log(`Chat Bot: ${chatBotResponse}`);
