"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionAlert``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_alert_code


class IngestionAlert(TypedDict, closed=True):
    code: NotRequired[
        "capo_opensearchserverless.types.ingestion_alert_code.IngestionAlertCode"
    ]
    """<p>The code that identifies the alert.</p>"""
    message: NotRequired["str"]
    """<p>A description of the alert.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionAlert) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionAlert:
    out: IngestionAlert = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
