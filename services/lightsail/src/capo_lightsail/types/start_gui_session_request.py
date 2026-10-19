"""Generated from Smithy shape ``com.amazonaws.lightsail#StartGUISessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class StartGUISessionRequest(TypedDict, closed=True):
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The resource name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartGUISessionRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartGUISessionRequest:
    out: StartGUISessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    return out
