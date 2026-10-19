"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EvaluationErrorItem``."""

from typing_extensions import TypedDict


class EvaluationErrorItem(TypedDict, closed=True):
    error_description: "str"
    """<p>The error description.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationErrorItem) -> dict:
    out: dict = {}
    out["errorDescription"] = value["error_description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EvaluationErrorItem:
    out: EvaluationErrorItem = {}  # type: ignore[typeddict-item]
    if data.get("errorDescription") is not None:
        out["error_description"] = data["errorDescription"]
    else:
        out["error_description"] = ""
    return out
