"""Generated from Smithy shape ``com.amazonaws.directconnect#AssociateConnectionsToResiliencyGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.resiliency_group_association_list


class AssociateConnectionsToResiliencyGroupResult(TypedDict, closed=True):
    resiliency_group_associations: NotRequired[
        "capo_direct_connect.types.resiliency_group_association_list.ResiliencyGroupAssociationList"
    ]
    """<p>The connection associations for the resiliency group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateConnectionsToResiliencyGroupResult) -> dict:
    out: dict = {}
    if "resiliency_group_associations" in value:
        import capo_direct_connect.types.resiliency_group_association_list

        out["resiliencyGroupAssociations"] = (
            capo_direct_connect.types.resiliency_group_association_list.serialize_aws_json_1_1(
                value["resiliency_group_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateConnectionsToResiliencyGroupResult:
    out: AssociateConnectionsToResiliencyGroupResult = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupAssociations") is not None:
        import capo_direct_connect.types.resiliency_group_association_list

        out["resiliency_group_associations"] = (
            capo_direct_connect.types.resiliency_group_association_list.deserialize_aws_json_1_1(
                data["resiliencyGroupAssociations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateConnectionsToResiliencyGroupResult) -> dict:
    out: dict = {}
    if "resiliency_group_associations" in value:
        import capo_direct_connect.types.resiliency_group_association_list

        out["resiliencyGroupAssociations"] = (
            capo_direct_connect.types.resiliency_group_association_list.serialize_cbor(
                value["resiliency_group_associations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AssociateConnectionsToResiliencyGroupResult:
    out: AssociateConnectionsToResiliencyGroupResult = {}  # type: ignore[typeddict-item]
    if data.get("resiliencyGroupAssociations") is not None:
        import capo_direct_connect.types.resiliency_group_association_list

        out["resiliency_group_associations"] = (
            capo_direct_connect.types.resiliency_group_association_list.deserialize_cbor(
                data["resiliencyGroupAssociations"]
            )
        )
    return out
