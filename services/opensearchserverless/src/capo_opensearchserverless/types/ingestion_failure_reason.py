"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionFailureReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.ingestion_failure_code


class IngestionFailureReason(TypedDict, closed=True):
    code: NotRequired[
        "capo_opensearchserverless.types.ingestion_failure_code.IngestionFailureCode"
    ]
    """<p>The code that identifies the reason for the failure.</p>"""
    message: NotRequired["str"]
    """<p>A description of the reason for the failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionFailureReason) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionFailureReason:
    out: IngestionFailureReason = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
