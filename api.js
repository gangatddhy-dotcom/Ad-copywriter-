import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

export async function POST(req: Request) {
  const body = await req.json();

  const completion = await openai.responses.create({
    model: "gpt-5",
    instructions: `
      You are a world-class ad copywriter.
      Generate high-converting ad copy.
    `,
    input: body.prompt
  });

  return Response.json({
    output: completion.output_text
  });
}