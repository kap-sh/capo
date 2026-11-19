"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteContainerAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.container_association_status
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DeleteContainerAssociationResponse(TypedDict, closed=True):
    container_association_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the container association.</p>"""
    container_association_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container association.</p>"""
    status: NotRequired[
        "capo_network_firewall.types.container_association_status.ContainerAssociationStatus"
    ]
    """<p>The current status of the container association. After deletion is initiated, the status is <code>DELETING</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteContainerAssociationResponse) -> dict:
    out: dict = {}
    if "container_association_name" in value:
        out["ContainerAssociationName"] = value["container_association_name"]
    if "container_association_arn" in value:
        out["ContainerAssociationArn"] = value["container_association_arn"]
    if "status" in value:
        import capo_network_firewall.types.container_association_status

        out["Status"] = (
            capo_network_firewall.types.container_association_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteContainerAssociationResponse:
    out: DeleteContainerAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociationName") is not None:
        out["container_association_name"] = data["ContainerAssociationName"]
    if data.get("ContainerAssociationArn") is not None:
        out["container_association_arn"] = data["ContainerAssociationArn"]
    if data.get("Status") is not None:
        import capo_network_firewall.types.container_association_status

        out["status"] = (
            capo_network_firewall.types.container_association_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteContainerAssociationResponse) -> dict:
    out: dict = {}
    if "container_association_name" in value:
        out["ContainerAssociationName"] = value["container_association_name"]
    if "container_association_arn" in value:
        out["ContainerAssociationArn"] = value["container_association_arn"]
    if "status" in value:
        import capo_network_firewall.types.container_association_status

        out["Status"] = (
            capo_network_firewall.types.container_association_status.serialize_cbor(
                value["status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteContainerAssociationResponse:
    out: DeleteContainerAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociationName") is not None:
        out["container_association_name"] = data["ContainerAssociationName"]
    if data.get("ContainerAssociationArn") is not None:
        out["container_association_arn"] = data["ContainerAssociationArn"]
    if data.get("Status") is not None:
        import capo_network_firewall.types.container_association_status

        out["status"] = (
            capo_network_firewall.types.container_association_status.deserialize_cbor(
                data["Status"]
            )
        )
    return out
