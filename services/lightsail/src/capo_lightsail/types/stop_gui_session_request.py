"""Generated from Smithy shape ``com.amazonaws.lightsail#StopGUISessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class StopGUISessionRequest(TypedDict, closed=True):
    resource_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The resource name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopGUISessionRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopGUISessionRequest:
    out: StopGUISessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    else:
        out["resource_name"] = ""
    return out
