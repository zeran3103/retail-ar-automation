# Retail Accounts Receivable (AR) Automation Engine

A high-performance Python-based data reconciliation pipeline built to audit daily retail distribution invoices, validate distributor credit limits (Terms of Payment / TOP), and parse multi-thousand-row raw ERP reports (Bosnet / SFHOA format).

---

## Technical Highlights
- **Fast Tabular Processing**: Uses Pandas vectorized operations for sub-second reconciliation of 5,000+ transaction rows.
- **Credit Limit & Overdue Auditing**: Automatically cross-references outstanding balances against predefined store limits to flag blocked orders instantly.
- **Channel Segmentation**: Separates General Trade (GT) and Modern Trade (MT) sales flows with custom credit terms.
- **Zero Cloud Leakage**: Designed to run entirely on-premise or on isolated local servers for sensitive financial privacy.

---

## Architecture Overview
```text
Raw Invoice / AR Report (Excel/CSV)
       │
       ▼
Bosnet / SFHOA Schema Normalizer (Python)
       │
       ▼
Data Audit Engine (Pandas Vectorized Verification)
  ├── 1. Terms of Payment (TOP) Calculation
  ├── 2. Credit Limit vs Outstanding Balance
  └── 3. Order Hold / Release Status Determination
       │
       ▼
Structured Reconciliation Report & Operational Dashboard
```

---

## Project Structure
- `reconcile_ar.py`: Core reconciliation and credit limit validation pipeline.
- `requirements.txt`: Minimal dependencies (pandas, openpyxl).

---

## Live Case Study & Portfolio
- **Production Reference**: Verified and deployed for Kalbe pharmaceutical/consumer goods distribution workflows.
- **Full Engineering Portfolio**: [https://zeranparcel.co-id.id/portfolio/](https://zeranparcel.co-id.id/portfolio/)
- **Freelance Order & Inquiries**: [Fastwork Official Profile](https://fastwork.id/user/ruekdjmx)

---

## Author
**Lukman Nul Hakim**  
Software Engineer & Automation Specialist  
GitHub: [@zeran3103](https://github.com/zeran3103)
