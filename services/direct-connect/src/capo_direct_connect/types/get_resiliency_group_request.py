"""Generated from Smithy shape ``com.amazonaws.directconnect#GetResiliencyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.resiliency_group_id


class GetResiliencyGroupRequest(TypedDict, closed=True):
    resiliency_group_id: (
        "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId"
    )
    """<p>The ID of the resiliency group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResiliencyGroupRequest) -> dict:
    out: dict = {}
    out["resiliencyGroupId"] = value["resiliency_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResiliencyGroupRequest:
    out: GetResiliencyGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupId") is not None:
        out["resiliency_group_id"] = data["resiliencyGroupId"]
    else:
        out["resiliency_group_id"] = ""
    return out
