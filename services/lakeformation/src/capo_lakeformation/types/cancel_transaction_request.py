"""Generated from Smithy shape ``com.amazonaws.lakeformation#CancelTransactionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.transaction_id_string


class CancelTransactionRequest(TypedDict, closed=True):
    transaction_id: "capo_lakeformation.types.transaction_id_string.TransactionIdString"
    """<p>The transaction to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelTransactionRequest) -> dict:
    out: dict = {}
    out["TransactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> CancelTransactionRequest:
    out: CancelTransactionRequest = {}  # type: ignore[typeddict-item]
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    else:
        out["transaction_id"] = ""
    return out
