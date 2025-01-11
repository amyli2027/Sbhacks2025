// import Groq from "groq-sdk";

// // Use the new Groq API key
// const groq = new Groq({
//   apiKey: "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",
// });

// async function testGroq() {
//   try {
//     const response = await groq.chat.completions.create({
//       messages: [
//         {
//           role: "user",
//           content: "Explain the importance of fast language models",
//         },
//       ],
//       model: "llama-3.3-70b-versatile",
//     });

//     console.log("API Response:", response.choices[0]?.message?.content || "No content received.");
//   } catch (error) {
//     console.error("Error calling Groq API:", error.message);
//   }
// }

// testGroq();
