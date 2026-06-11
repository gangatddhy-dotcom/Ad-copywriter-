from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

SYSTEM_PROMPT = """
You are an elite direct-response copywriter.

Your job:
1. Analyze product details.
2. Identify target audience.
3. Find pain points.
4. Create marketing angles.
5. Generate:
   - Headlines
   - Hooks
   - Ad copy
   - CTAs
6. Follow AIDA and PAS frameworks.
7. Output multiple variations.

Always write persuasive, conversion-focused copy.
"""

def generate_ad_copy(product, audience, offer):
    response = client.responses.create(
        model="gpt-5",
        instructions=SYSTEM_PROMPT,
        input=f"""
        Product: {product}

        Audience: {audience}

        Offer: {offer}

        Generate:
        - 10 Headlines
        - 5 Hooks
        - 3 Facebook Ads
        - 3 Google Ads
        - 3 TikTok Ads
        - 5 CTA Variations
        """
    )

    return response.output_text


if __name__ == "__main__":
    result = generate_ad_copy(
        product="AI-powered Finance Tracker",
        audience="College Students",
        offer="Free 30-Day Trial"
    )

    print(result)