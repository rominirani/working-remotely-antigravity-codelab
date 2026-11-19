# Product Requirements Document (PRD): Cloud Run & Firestore Webhook Delivery Service (v1)

**Author:** Platform Product Team  
**Status:** Draft for Engineering Review  
**Target Architecture:** Google Cloud (**Cloud Run**, **Firestore**, **Cloud Storage**, **BigQuery**)

## 1. Objective
Customers rely on our outbound webhooks (`order.created`, `payment.succeeded`, `shipment.updated`) to sync events into their ERP and inventory systems. Currently, our monolith fires synchronous HTTP requests; if a customer's webhook endpoint times out once, the event is lost. We are migrating to a resilient delivery service on **Google Cloud** using **Cloud Run**, **Firestore**, **Cloud Storage**, and **BigQuery**.

## 2. Proposed Google Cloud Architecture & Scope (v1)
1. **Cloud Run Dispatcher + Firestore Delivery State (`2-Hour` Retry Window)**
   - Run an autoscaled **Cloud Run** service (`webhook-dispatcher`) that records each outbound webhook attempt in **Firestore** (`webhook_deliveries/{eventId}`) and retries failed deliveries with exponential backoff over a **2-hour window**.
2. **BigQuery Delivery Analytics Table (`24-Hour` Partition Expiration)**
   - Stream delivery attempt records into a **BigQuery** table (`acme_analytics.webhook_deliveries`) partitioned by `attempt_timestamp` with a **24-hour partition expiration**, backing `GET /v1/webhooks/deliveries`.
3. **Single Static HMAC-SHA256 Signing Key in Firestore**
   - Store a single static signing secret per customer in their **Firestore** tenant configuration document (`tenants/{tenantId}`) and pass the signature in `X-Webhook-Signature`.

## 3. Out of Scope for v1 (Deferred to v2)
- **Cloud Storage (GCS) Dead-Letter Archive & Manual Replay API:** Archiving exhausted webhook payloads as JSON objects in **Cloud Storage** (`gs://acme-webhook-dlq-prod`) and exposing `POST /v1/webhooks/replay` so customers can replay events after downtime.
- **7-Day Retention in Firestore & BigQuery:** Extending Firestore TTL policies and BigQuery partition retention from 24 hours to **7 days** to cover weekend outages.
- **Zero-Downtime Dual-Key Rotation in Firestore:** Supporting two active signing keys (`primary_key` and `previous_key`) in the customer's **Firestore** tenant config document during 30-day compliance key rotations.
- **Per-Tenant Concurrency Limits on Cloud Run:** Using Firestore distributed counters to cap concurrent **Cloud Run** webhook deliveries per customer endpoint when a customer's server recovers from downtime.
