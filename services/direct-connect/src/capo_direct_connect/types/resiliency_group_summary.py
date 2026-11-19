"""Generated from Smithy shape ``com.amazonaws.directconnect#ResiliencyGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.owner_account
    import capo_direct_connect.types.resiliency_group_arn
    import capo_direct_connect.types.resiliency_group_id
    import capo_direct_connect.types.resiliency_group_name
    import capo_direct_connect.types.resiliency_group_state
    import capo_direct_connect.types.resiliency_group_type


class ResiliencyGroupSummary(TypedDict, closed=True):
    resiliency_group_id: NotRequired[
        "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId"
    ]
    """<p>The ID of the resiliency group.</p>"""
    resiliency_group_arn: NotRequired[
        "capo_direct_connect.types.resiliency_group_arn.ResiliencyGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resiliency group.</p>"""
    resiliency_group_name: NotRequired[
        "capo_direct_connect.types.resiliency_group_name.ResiliencyGroupName"
    ]
    """<p>The name of the resiliency group.</p>"""
    resiliency_group_type: NotRequired[
        "capo_direct_connect.types.resiliency_group_type.ResiliencyGroupType"
    ]
    """<p>The type of the resiliency group. The valid value is <code>Managed</code>.</p>"""
    owner_account: NotRequired["capo_direct_connect.types.owner_account.OwnerAccount"]
    """<p>The ID of the Amazon Web Services account that owns the resiliency group.</p>"""
    state: NotRequired[
        "capo_direct_connect.types.resiliency_group_state.ResiliencyGroupState"
    ]
    """<p>The state of the resiliency group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResiliencyGroupSummary) -> dict:
    out: dict = {}
    if "resiliency_group_id" in value:
        out["resiliencyGroupId"] = value["resiliency_group_id"]
    if "resiliency_group_arn" in value:
        out["resiliencyGroupArn"] = value["resiliency_group_arn"]
    if "resiliency_group_name" in value:
        out["resiliencyGroupName"] = value["resiliency_group_name"]
    if "resiliency_group_type" in value:
        import capo_direct_connect.types.resiliency_group_type

        out["resiliencyGroupType"] = (
            capo_direct_connect.types.resiliency_group_type.serialize_aws_json_1_1(
                value["resiliency_group_type"]
            )
        )
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "state" in value:
        import capo_direct_connect.types.resiliency_group_state

        out["state"] = (
            capo_direct_connect.types.resiliency_group_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResiliencyGroupSummary:
    out: ResiliencyGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupId") is not None:
        out["resiliency_group_id"] = data["resiliencyGroupId"]
    if data.get("resiliencyGroupArn") is not None:
        out["resiliency_group_arn"] = data["resiliencyGroupArn"]
    if data.get("resiliencyGroupName") is not None:
        out["resiliency_group_name"] = data["resiliencyGroupName"]
    if data.get("resiliencyGroupType") is not None:
        import capo_direct_connect.types.resiliency_group_type

        out["resiliency_group_type"] = (
            capo_direct_connect.types.resiliency_group_type.deserialize_aws_json_1_1(
                data["resiliencyGroupType"]
            )
        )
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("state") is not None:
        import capo_direct_connect.types.resiliency_group_state

        out["state"] = (
            capo_direct_connect.types.resiliency_group_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResiliencyGroupSummary) -> dict:
    out: dict = {}
    if "resiliency_group_id" in value:
        out["resiliencyGroupId"] = value["resiliency_group_id"]
    if "resiliency_group_arn" in value:
        out["resiliencyGroupArn"] = value["resiliency_group_arn"]
    if "resiliency_group_name" in value:
        out["resiliencyGroupName"] = value["resiliency_group_name"]
    if "resiliency_group_type" in value:
        import capo_direct_connect.types.resiliency_group_type

        out["resiliencyGroupType"] = (
            capo_direct_connect.types.resiliency_group_type.serialize_cbor(
                value["resiliency_group_type"]
            )
        )
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "state" in value:
        import capo_direct_connect.types.resiliency_group_state

        out["state"] = capo_direct_connect.types.resiliency_group_state.serialize_cbor(
            value["state"]
        )
    return out


def deserialize_cbor(data: dict) -> ResiliencyGroupSummary:
    out: ResiliencyGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupId") is not None:
        out["resiliency_group_id"] = data["resiliencyGroupId"]
    if data.get("resiliencyGroupArn") is not None:
        out["resiliency_group_arn"] = data["resiliencyGroupArn"]
    if data.get("resiliencyGroupName") is not None:
        out["resiliency_group_name"] = data["resiliencyGroupName"]
    if data.get("resiliencyGroupType") is not None:
        import capo_direct_connect.types.resiliency_group_type

        out["resiliency_group_type"] = (
            capo_direct_connect.types.resiliency_group_type.deserialize_cbor(
                data["resiliencyGroupType"]
            )
        )
    if data.get("ownerAccount") is not None:
        out["owner_account"] = data["ownerAccount"]
    if data.get("state") is not None:
        import capo_direct_connect.types.resiliency_group_state

        out["state"] = (
            capo_direct_connect.types.resiliency_group_state.deserialize_cbor(
                data["state"]
            )
        )
    return out
