import os
import requests

WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL")


def post_to_slack(message_text):
  if not WEBHOOK_URL:
    print("❌ ERROR: SLACK_WEBHOOK_URL environment variable is None or empty.")
    return False

  payload = {"text": message_text}

  try:
    response = requests.post(WEBHOOK_URL, json=payload, timeout=10)

    # Slack returns 200 with body 'ok' on success
    if response.status_code == 200 and response.text == "ok":
      print(f"✅ Slack Ping Sent Successfully: {message_text[:30]}...")
      return True
    else:
      print(f"❌ Slack API Rejected Request!")
      print(f"   HTTP Status: {response.status_code}")
      print(f"   Slack Response: {response.text}")
      return False

  except requests.exceptions.RequestException as e:
    print(f"❌ Network/Connection Exception while posting to Slack: {e}")
    return False


def post_job_alert(company, title, url, platform):
  message = (
      f"🚀 *{company.upper()}* - {title}\n"
      f"📌 *Platform:* {platform}\n"
      f"🔗 <{url}|Tap to Apply on Mobile>\n"
      f"────────────────────────"
  )
  return post_to_slack(message)


# IMMEDIATE SELF-TEST ON RUN
if __name__ == "__main__":
  print("--- Starting Diagnostic Run ---")
  print(
      f"SLACK_WEBHOOK_URL detected: {'YES (starts with ' + WEBHOOK_URL[:30] + '...)' if WEBHOOK_URL else 'NO (None)'}"
  )

  test_success = post_to_slack(
      "🟢 *Job Screener Diagnostic Ping:* Webhook connection verified!"
  )

  if test_success:
    print(
        "Self-test succeeded. Webhook is valid. Proceeding to job scan logic..."
    )
  else:
    print("Self-test failed. Fix the error above before troubleshooting ATS scraping.")
