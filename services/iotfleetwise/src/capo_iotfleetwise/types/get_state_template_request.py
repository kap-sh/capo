"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetStateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.resource_identifier


class GetStateTemplateRequest(TypedDict, closed=True):
    identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier"
    """<p>The unique ID of the state template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetStateTemplateRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetStateTemplateRequest:
    out: GetStateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
