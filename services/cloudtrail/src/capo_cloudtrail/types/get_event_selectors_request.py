"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetEventSelectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.string


class GetEventSelectorsRequest(TypedDict, closed=True):
    trail_name: "capo_cloudtrail.types.string.String"
    """<p>Specifies the name of the trail or trail ARN. If you specify a trail name, the string must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), periods (.), underscores (_), or dashes (-)</p> </li> <li> <p>Start with a letter or number, and end with a letter or number</p> </li> <li> <p>Be between 3 and 128 characters</p> </li> <li> <p>Have no adjacent periods, underscores or dashes. Names like <code>my-_namespace</code> and <code>my--namespace</code> are not valid.</p> </li> <li> <p>Not be in IP address format (for example, 192.168.5.4)</p> </li> </ul> <p>If you specify a trail ARN, it must be in the format:</p> <p> <code>arn:aws:cloudtrail:us-east-2:123456789012:trail/MyTrail</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventSelectorsRequest) -> dict:
    out: dict = {}
    out["TrailName"] = value["trail_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventSelectorsRequest:
    out: GetEventSelectorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrailName") is not None:
        out["trail_name"] = data["TrailName"]
    else:
        out["trail_name"] = ""
    return out
