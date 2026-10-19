"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#As2805PekDerivationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.system_trace_audit_number_type
    import capo_payment_cryptography_data.types.transaction_amount_type


class As2805PekDerivationAttributes(TypedDict, closed=True):
    system_trace_audit_number: "capo_payment_cryptography_data.types.system_trace_audit_number_type.SystemTraceAuditNumberType"
    """<p>The system trace audit number for the transaction.</p>"""
    transaction_amount: "capo_payment_cryptography_data.types.transaction_amount_type.TransactionAmountType"
    """<p>The transaction amount for the transaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: As2805PekDerivationAttributes) -> dict:
    out: dict = {}
    out["SystemTraceAuditNumber"] = value["system_trace_audit_number"]
    out["TransactionAmount"] = value["transaction_amount"]
    return out


def deserialize_json(data: dict) -> As2805PekDerivationAttributes:
    out: As2805PekDerivationAttributes = {}  # type: ignore[typeddict-item]
    if data.get("SystemTraceAuditNumber") is not None:
        out["system_trace_audit_number"] = data["SystemTraceAuditNumber"]
    else:
        out["system_trace_audit_number"] = ""
    if data.get("TransactionAmount") is not None:
        out["transaction_amount"] = data["TransactionAmount"]
    else:
        out["transaction_amount"] = ""
    return out
