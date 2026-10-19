"""Generated from Smithy shape ``com.amazonaws.inspector#CreateResourceGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn


class CreateResourceGroupResponse(TypedDict, closed=True):
    resource_group_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the resource group that is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResourceGroupResponse) -> dict:
    out: dict = {}
    out["resourceGroupArn"] = value["resource_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResourceGroupResponse:
    out: CreateResourceGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceGroupArn") is not None:
        out["resource_group_arn"] = data["resourceGroupArn"]
    else:
        out["resource_group_arn"] = ""
    return out
