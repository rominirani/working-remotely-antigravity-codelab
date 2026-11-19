# Working Remotely with Google Antigravity — Codelab Starter Repository

This repository contains all starter files for the **Working Remotely with Google Antigravity** hands-on codelab, covering both **Remote Control** (running on your own laptop) and **Remote Agents** (running in Google's cloud sandbox).

## Repository Structure

| Folder | Codelab Step | Mode | Description |
| :--- | :--- | :--- | :--- |
| `01-hello-remote-control/` | Steps 3 & 6 | Remote Control & Remote Agents | `sample_gcp_config.json` and `env_check.py` for the side-by-side "Hello World" comparison |
| `02-event-checkin/` | Step 4 | Remote Control (Business User) | `workshop_registrations.csv` and `vip_speaker_notes.md` for the zero-code on-site check-in & catering brief |
| `03-invoice-api/` | Step 5 | Remote Control (Developer) | `invoice_api.py` (starter with 2 bugs) and `test_invoice_api.py` (3 unit tests) |
| `04-prd-review/` | Step 7 | Remote Agents (Business & Product) | `webhook-service-gcp-prd.md` (attach via Google Drive) and `bigquery-customer-feedback-q3.csv` (upload to `/home/antigravity/upload`) |
| `05-order-discounts/` | Step 8 | Remote Agents (Developer — GitHub) | `order_discounts.py` (starter with 3 bugs) and `test_order_discounts.py` (6 unit tests) |

## Quick Start

1. **Fork** this repository to your own GitHub account (so you can attach your fork in Step 8 for Remote Agents).
2. **Clone** your fork locally under `$HOME/agy2-projects/`:
   ```bash
   mkdir -p "$HOME/agy2-projects"
   cd "$HOME/agy2-projects"
   git clone https://github.com/<your-github-username>/working-remotely-antigravity-codelab.git
   ```
3. Open `$HOME/agy2-projects/working-remotely-antigravity-codelab` as a **Project** in the Google Antigravity Desktop App and follow along with the codelab!

## Reference Links

- Google Antigravity: https://antigravity.google/
- Remote Control Docs: https://antigravity.google/docs/remote-control/
- Remote Agents Docs: https://antigravity.google/docs/remote-agents/
