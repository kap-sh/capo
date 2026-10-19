"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeregisterResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.resource_arn_string


class DeregisterResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DeregisterResourceRequest:
    out: DeregisterResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
