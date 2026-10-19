"""Generated from Smithy shape ``com.amazonaws.glue#StopSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.orchestration_name_string


class StopSessionRequest(TypedDict, closed=True):
    id: "capo_glue.types.name_string.NameString"
    """<p>The ID of the session to be stopped.</p>"""
    request_origin: NotRequired[
        "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopSessionRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopSessionRequest:
    out: StopSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("RequestOrigin") is not None:
        out["request_origin"] = data["RequestOrigin"]
    return out
