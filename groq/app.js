// import Groq from "groq-sdk";

// // Use the new Groq API key
// const groq = new Groq({
//   apiKey: "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",
// });

// export async function main() {
//   const outputElement = document.getElementById("output");

//   try {
//     const chatCompletion = await getGroqChatCompletion();
//     const content = chatCompletion.choices[0]?.message?.content || "No response received.";

//     // Display the result on the webpage
//     outputElement.textContent = content;
//   } catch (error) {
//     // Display the error message on the webpage
//     outputElement.textContent = `Error: ${error.message}`;
//     console.error("Groq API Error:", error);
//   }
// }

// export async function getGroqChatCompletion() {
//   return groq.chat.completions.create({
//     messages: [
//       {
//         role: "user",
//         content: "Explain the importance of fast language models",
//       },
//     ],
//     model: "llama-3.3-70b-versatile",
//   });
// }

// // Run the main function when the script loads
// main();
