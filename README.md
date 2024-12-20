
# TheBADCoinBot

**TheBADCoinBot** automates various tasks on the BadCoin Telegram Bot, such as tapping and holding, with configurable options for delays and randomization.

---

## Features

- **Automated Tapping**: Automatically taps to earn rewards based on available energy.
- **Automated Holding**: Performs holding tasks with random checkpoints and claims rewards.
- **Randomized Delays**: Mimics realistic activity with random sleep periods.
- **Error Handling**: Logs errors and restarts tasks automatically.
- **Configurable Sleep Delay**: Customize delay between task cycles using environment variables.

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Praveensenpai/TheBADCoinBot.git
cd TheBADCoinBot
```

### 2. Install `uv` Package Manager

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Linux/macOS:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Sync Dependencies with `uv`

```bash
uv sync
```

### 4. Configure `.env`

Create a `.env` file in the project directory and add the following variables:

```plaintext
API_ID=your_api_id
API_HASH=your_api_hash
REF_ID=w6t00gnbr9
SESSION_NAME=bad
PHONE=+91
SLEEP_DELAY_MINUTES=1
MIN_HOLD=5
MAX_HOLD=8
```

| Key                   | Description                                   |
| --------------------- | --------------------------------------------- |
| `API_ID`              | Your Telegram API ID                          |
| `API_HASH`            | Your Telegram API Hash                        |
| `REF_ID`              | Referral ID from the referral link            |
| `SESSION_NAME`        | Session name (e.g., `bad`)                    |
| `PHONE`               | Your phone number                             |
| `SLEEP_DELAY_MINUTES` | Delay between task cycles (in minutes)        |
| `MIN_HOLD`            | Minimum holding checkpoints                   |
| `MAX_HOLD`            | Maximum holding checkpoints                   |

---

## Running the Bot

To run the bot, use the following command:

```bash
uv run main.py
```

The bot will log in, perform tasks (tapping and holding), and rest for the configured time before repeating.

---

## Notes

- **No Proxy**: The bot operates without any proxy settings.
- **Single Session**: Only one active session is supported at a time.
- **Restart on Failure**: The bot restarts automatically in case of errors.
- **Future Enhancements**: Additional features like task completion will be added in future updates.

---

## Getting Your Telegram API ID and Hash

To obtain the **API ID** and **API Hash** for Telegram, follow these steps:

1. **Log in to Telegram**: Use the official [Telegram Web](https://web.telegram.org/) or app to log in to your account.
2. **Access the Telegram Developer Portal**:
   - Go to [https://my.telegram.org](https://my.telegram.org) and sign in with your Telegram credentials.
3. **Create a New Application**:
   - After logging in, click on **API Development Tools**.
   - Choose **Create new application** and fill in the required details (e.g., app name, platform).
4. **Get Your API ID and Hash**:
   - After completion, Telegram will provide an **API ID** and **API Hash**. Copy and paste them into your `.env` file.

Keep these credentials secure and avoid sharing them publicly.

---

## Troubleshooting

If the bot encounters an error, it will log the issue and restart automatically after a short delay. Check the logs for detailed information.

---

## Disclaimer

This bot is provided as-is without any guarantees. Use it responsibly and ensure compliance with Telegram's terms of service.
