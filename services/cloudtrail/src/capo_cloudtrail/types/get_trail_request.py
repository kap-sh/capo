"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetTrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.string


class GetTrailRequest(TypedDict, closed=True):
    name: "capo_cloudtrail.types.string.String"
    """<p>The name or the Amazon Resource Name (ARN) of the trail for which you want to retrieve settings information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTrailRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTrailRequest:
    out: GetTrailRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
