"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeleteTrailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.string


class DeleteTrailRequest(TypedDict, closed=True):
    name: "capo_cloudtrail.types.string.String"
    """<p>Specifies the name or the CloudTrail ARN of the trail to be deleted. The following is the format of a trail ARN. <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrailRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrailRequest:
    out: DeleteTrailRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
