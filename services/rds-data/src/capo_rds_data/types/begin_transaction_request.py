"""Generated from Smithy shape ``com.amazonaws.rdsdata#BeginTransactionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rds_data.types.arn
    import capo_rds_data.types.db_name


class BeginTransactionRequest(TypedDict, closed=True):
    resource_arn: "capo_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>"""
    secret_arn: "capo_rds_data.types.arn.Arn"
    """<p>The name or ARN of the secret that enables access to the DB cluster.</p>"""
    database: NotRequired["capo_rds_data.types.db_name.DbName"]
    """<p>The name of the database.</p>"""
    schema: NotRequired["capo_rds_data.types.db_name.DbName"]
    """<p>The name of the database schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BeginTransactionRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    if "database" in value:
        out["database"] = value["database"]
    if "schema" in value:
        out["schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> BeginTransactionRequest:
    out: BeginTransactionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    if data.get("database") is not None:
        out["database"] = data["database"]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    return out
