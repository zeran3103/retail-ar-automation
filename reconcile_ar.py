"""
Retail Accounts Receivable (AR) & Invoice Reconciliation Pipeline
Author: Lukman Nul Hakim
Portfolio: https://zeranparcel.co-id.id/portfolio/
"""

import sys
from typing import Dict, Any

try:
    import pandas as pd
except ImportError:
    pd = None


def audit_accounts_receivable(transactions: list) -> Dict[str, Any]:
    """
    Audits incoming invoice batches against credit rules:
    - Overdue status check (TOP / Terms of Payment exceeded)
    - Store credit limit threshold breach
    - Generates order hold / release action list
    """
    summary = {
        "total_records": len(transactions),
        "total_outstanding": 0.0,
        "blocked_stores": [],
        "approved_orders": [],
    }

    for row in transactions:
        store_code = row.get("store_code")
        credit_limit = row.get("credit_limit", 0.0)
        current_balance = row.get("outstanding_balance", 0.0)
        new_order_amount = row.get("order_amount", 0.0)
        overdue_days = row.get("overdue_days", 0)

        total_projected = current_balance + new_order_amount
        summary["total_outstanding"] += current_balance

        # Rule 1: Strict block if invoice overdue > 7 days
        # Rule 2: Block if projected exposure exceeds approved credit limit
        if overdue_days > 7 or total_projected > credit_limit:
            summary["blocked_stores"].append({
                "store_code": store_code,
                "reason": "Overdue" if overdue_days > 7 else "Credit Limit Exceeded",
                "exposure": total_projected,
                "limit": credit_limit
            })
        else:
            summary["approved_orders"].append(store_code)

    return summary


if __name__ == "__main__":
    mock_data = [
        {"store_code": "TOKO-A1", "credit_limit": 50000000, "outstanding_balance": 12000000, "order_amount": 5000000, "overdue_days": 0},
        {"store_code": "TOKO-B2", "credit_limit": 30000000, "outstanding_balance": 28000000, "order_amount": 4000000, "overdue_days": 2},
        {"store_code": "TOKO-C3", "credit_limit": 20000000, "outstanding_balance": 15000000, "order_amount": 2000000, "overdue_days": 14},
    ]
    
    result = audit_accounts_receivable(mock_data)
    print(f"Audited {result['total_records']} stores.")
    print(f"Approved: {len(result['approved_orders'])} | Blocked: {len(result['blocked_stores'])}")
