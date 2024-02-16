// Replace with your GPT-4 API key
const apiKey = 'YOUR_API_KEY_HERE';

// Function to start the chat
function startChat() {
    const userMessage = prompt('Enter your message:');
    if (userMessage) {
        getChatbotResponse(userMessage);
    }
}

// Function to get a chatbot response
async function getChatbotResponse(userMessage) {
    try {
        const response = await fetch('https://api.openai.com/v1/engines/davinci/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${apiKey}`,
            },
            body: JSON.stringify({
                prompt: userMessage,
                max_tokens: 50, // Adjust as needed
            }),
        });

        const data = await response.json();
        const chatbotResponse = data.choices[0].text;

        // Display the chatbot response
        alert(`Chatbot: ${chatbotResponse}`);
    } catch (error) {
        console.error('Error fetching chatbot response:', error);
    }
}
