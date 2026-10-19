"""Generated from Smithy shape ``com.amazonaws.rdsdata#RollbackTransactionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rds_data.types.arn
    import capo_rds_data.types.id


class RollbackTransactionRequest(TypedDict, closed=True):
    resource_arn: "capo_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>"""
    secret_arn: "capo_rds_data.types.arn.Arn"
    """<p>The name or ARN of the secret that enables access to the DB cluster.</p>"""
    transaction_id: "capo_rds_data.types.id.Id"
    """<p>The identifier of the transaction to roll back.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackTransactionRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    out["transactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> RollbackTransactionRequest:
    out: RollbackTransactionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    if data.get("transactionId") is not None:
        out["transaction_id"] = data["transactionId"]
    else:
        out["transaction_id"] = ""
    return out
