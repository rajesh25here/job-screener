import os
import requests

WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")


def post_to_slack(company, title, url, platform):
  if not WEBHOOK_URL:
    print("SLACK_WEBHOOK_URL is not configured.")
    return

  message = (
      f"🚀 *{company.upper()}* - {title}\n"
      f"📌 *Platform:* {platform}\n"
      f"🔗 <{url}|Tap to Apply on Mobile>\n"
      f"────────────────────────"
  )
  payload = {"text": message}
  try:
    requests.post(WEBHOOK_URL, json=payload, timeout=10)
  except Exception as e:
    print(f"Error alerting Slack: {e}")
