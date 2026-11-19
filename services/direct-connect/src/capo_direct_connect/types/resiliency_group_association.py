"""Generated from Smithy shape ``com.amazonaws.directconnect#ResiliencyGroupAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_arn
    import capo_direct_connect.types.resiliency_group_association_state
    import capo_direct_connect.types.resiliency_group_id


class ResiliencyGroupAssociation(TypedDict, closed=True):
    resiliency_group_id: NotRequired[
        "capo_direct_connect.types.resiliency_group_id.ResiliencyGroupId"
    ]
    """<p>The ID of the resiliency group.</p>"""
    connection_arn: NotRequired[
        "capo_direct_connect.types.connection_arn.ConnectionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the associated connection.</p>"""
    state: NotRequired[
        "capo_direct_connect.types.resiliency_group_association_state.ResiliencyGroupAssociationState"
    ]
    """<p>The state of the association. The valid values are <code>associating</code>, <code>associated</code>, <code>disassociating</code>, and <code>disassociated</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResiliencyGroupAssociation) -> dict:
    out: dict = {}
    if "resiliency_group_id" in value:
        out["resiliencyGroupId"] = value["resiliency_group_id"]
    if "connection_arn" in value:
        out["connectionArn"] = value["connection_arn"]
    if "state" in value:
        import capo_direct_connect.types.resiliency_group_association_state

        out["state"] = (
            capo_direct_connect.types.resiliency_group_association_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResiliencyGroupAssociation:
    out: ResiliencyGroupAssociation = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupId") is not None:
        out["resiliency_group_id"] = data["resiliencyGroupId"]
    if data.get("connectionArn") is not None:
        out["connection_arn"] = data["connectionArn"]
    if data.get("state") is not None:
        import capo_direct_connect.types.resiliency_group_association_state

        out["state"] = (
            capo_direct_connect.types.resiliency_group_association_state.deserialize_aws_json_1_1(
                data["state"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResiliencyGroupAssociation) -> dict:
    out: dict = {}
    if "resiliency_group_id" in value:
        out["resiliencyGroupId"] = value["resiliency_group_id"]
    if "connection_arn" in value:
        out["connectionArn"] = value["connection_arn"]
    if "state" in value:
        import capo_direct_connect.types.resiliency_group_association_state

        out["state"] = (
            capo_direct_connect.types.resiliency_group_association_state.serialize_cbor(
                value["state"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ResiliencyGroupAssociation:
    out: ResiliencyGroupAssociation = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupId") is not None:
        out["resiliency_group_id"] = data["resiliencyGroupId"]
    if data.get("connectionArn") is not None:
        out["connection_arn"] = data["connectionArn"]
    if data.get("state") is not None:
        import capo_direct_connect.types.resiliency_group_association_state

        out["state"] = (
            capo_direct_connect.types.resiliency_group_association_state.deserialize_cbor(
                data["state"]
            )
        )
    return out
