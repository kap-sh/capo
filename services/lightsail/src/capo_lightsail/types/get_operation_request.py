"""Generated from Smithy shape ``com.amazonaws.lightsail#GetOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.non_empty_string


class GetOperationRequest(TypedDict, closed=True):
    operation_id: "capo_lightsail.types.non_empty_string.NonEmptyString"
    """<p>A GUID used to identify the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationRequest) -> dict:
    out: dict = {}
    out["operationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationRequest:
    out: GetOperationRequest = {}  # type: ignore[typeddict-item]
    if data.get("operationId") is not None:
        out["operation_id"] = data["operationId"]
    else:
        out["operation_id"] = ""
    return out
