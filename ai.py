# ai_assistant.py
import aiohttp

OPENROUTER_API_KEY = "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"

async def get_ai_response(user_message):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "X-Title": "TelegramBotGPT"
    }

    json_data = {
        "model": "openai/gpt-3.5-turbo",  # Istasangiz "mistralai/mistral-7b-instruct" ham bo‘ladi
        "messages": [
            {"role": "system", "content": "Siz foydalanuvchiga yordam beradigan sun’iy intellektsiyasiz."},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=json_data) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data["choices"][0]["message"]["content"]
                else:
                    return "❌ Javob olishda xatolik: OpenRouter API dan xatolik."
    except Exception as e:
        print(f"Xatolik: {e}")
        return "⚠️ Xatolik yuz berdi."
