"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateResiliencyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.idempotency_token
    import capo_direct_connect.types.resiliency_group_id
    import capo_direct_connect.types.resiliency_group_name


class UpdateResiliencyGroupRequest(TypedDict, closed=True):
    resiliency_group_id: (
        "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId"
    )
    """<p>The ID of the resiliency group.</p>"""
    resiliency_group_name: (
        "capo_direct_connect.types.resiliency_group_name.ResiliencyGroupName"
    )
    """<p>The new name of the resiliency group.</p>"""
    client_token: NotRequired[
        "capo_direct_connect.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResiliencyGroupRequest) -> dict:
    out: dict = {}
    out["resiliencyGroupId"] = value["resiliency_group_id"]
    out["resiliencyGroupName"] = value["resiliency_group_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResiliencyGroupRequest:
    out: UpdateResiliencyGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupId") is not None:
        out["resiliency_group_id"] = data["resiliencyGroupId"]
    else:
        out["resiliency_group_id"] = ""
    if data.get("resiliencyGroupName") is not None:
        out["resiliency_group_name"] = data["resiliencyGroupName"]
    else:
        out["resiliency_group_name"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
