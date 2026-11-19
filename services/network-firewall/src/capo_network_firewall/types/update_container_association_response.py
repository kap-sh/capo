"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateContainerAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.container_association_status
    import capo_network_firewall.types.container_monitoring_configurations
    import capo_network_firewall.types.container_monitoring_type
    import capo_network_firewall.types.description
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.tag_list
    import capo_network_firewall.types.update_token


class UpdateContainerAssociationResponse(TypedDict, closed=True):
    container_association_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the container association.</p>"""
    container_association_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the container association.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the container association.</p>"""
    type: NotRequired[
        "capo_network_firewall.types.container_monitoring_type.ContainerMonitoringType"
    ]
    """<p>The container type. Valid values:</p> <ul> <li> <p> <code>ECS</code> - Amazon Elastic Container Service</p> </li> <li> <p> <code>EKS</code> - Amazon Elastic Kubernetes Service</p> </li> </ul>"""
    container_monitoring_configurations: NotRequired[
        "capo_network_firewall.types.container_monitoring_configurations.ContainerMonitoringConfigurations"
    ]
    """<p>The monitoring configurations for the container association.</p>"""
    status: NotRequired[
        "capo_network_firewall.types.container_association_status.ContainerAssociationStatus"
    ]
    """<p>The current status of the container association.</p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    update_token: NotRequired["capo_network_firewall.types.update_token.UpdateToken"]
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the container association. The token marks the state of the container association resource at the time of the request.</p> <p>To make changes to the container association, you provide the token in your request. Network Firewall uses the token to ensure that the container association hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the container association again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateContainerAssociationResponse) -> dict:
    out: dict = {}
    if "container_association_name" in value:
        out["ContainerAssociationName"] = value["container_association_name"]
    if "container_association_arn" in value:
        out["ContainerAssociationArn"] = value["container_association_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_network_firewall.types.container_monitoring_type

        out["Type"] = (
            capo_network_firewall.types.container_monitoring_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    if "container_monitoring_configurations" in value:
        import capo_network_firewall.types.container_monitoring_configurations

        out["ContainerMonitoringConfigurations"] = (
            capo_network_firewall.types.container_monitoring_configurations.serialize_aws_json_1_0(
                value["container_monitoring_configurations"]
            )
        )
    if "status" in value:
        import capo_network_firewall.types.container_association_status

        out["Status"] = (
            capo_network_firewall.types.container_association_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateContainerAssociationResponse:
    out: UpdateContainerAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociationName") is not None:
        out["container_association_name"] = data["ContainerAssociationName"]
    if data.get("ContainerAssociationArn") is not None:
        out["container_association_arn"] = data["ContainerAssociationArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.container_monitoring_type

        out["type"] = (
            capo_network_firewall.types.container_monitoring_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    if data.get("ContainerMonitoringConfigurations") is not None:
        import capo_network_firewall.types.container_monitoring_configurations

        out["container_monitoring_configurations"] = (
            capo_network_firewall.types.container_monitoring_configurations.deserialize_aws_json_1_0(
                data["ContainerMonitoringConfigurations"]
            )
        )
    if data.get("Status") is not None:
        import capo_network_firewall.types.container_association_status

        out["status"] = (
            capo_network_firewall.types.container_association_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateContainerAssociationResponse) -> dict:
    out: dict = {}
    if "container_association_name" in value:
        out["ContainerAssociationName"] = value["container_association_name"]
    if "container_association_arn" in value:
        out["ContainerAssociationArn"] = value["container_association_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_network_firewall.types.container_monitoring_type

        out["Type"] = (
            capo_network_firewall.types.container_monitoring_type.serialize_cbor(
                value["type"]
            )
        )
    if "container_monitoring_configurations" in value:
        import capo_network_firewall.types.container_monitoring_configurations

        out["ContainerMonitoringConfigurations"] = (
            capo_network_firewall.types.container_monitoring_configurations.serialize_cbor(
                value["container_monitoring_configurations"]
            )
        )
    if "status" in value:
        import capo_network_firewall.types.container_association_status

        out["Status"] = (
            capo_network_firewall.types.container_association_status.serialize_cbor(
                value["status"]
            )
        )
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_cbor(value["tags"])
    if "update_token" in value:
        out["UpdateToken"] = value["update_token"]
    return out


def deserialize_cbor(data: dict) -> UpdateContainerAssociationResponse:
    out: UpdateContainerAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociationName") is not None:
        out["container_association_name"] = data["ContainerAssociationName"]
    if data.get("ContainerAssociationArn") is not None:
        out["container_association_arn"] = data["ContainerAssociationArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.container_monitoring_type

        out["type"] = (
            capo_network_firewall.types.container_monitoring_type.deserialize_cbor(
                data["Type"]
            )
        )
    if data.get("ContainerMonitoringConfigurations") is not None:
        import capo_network_firewall.types.container_monitoring_configurations

        out["container_monitoring_configurations"] = (
            capo_network_firewall.types.container_monitoring_configurations.deserialize_cbor(
                data["ContainerMonitoringConfigurations"]
            )
        )
    if data.get("Status") is not None:
        import capo_network_firewall.types.container_association_status

        out["status"] = (
            capo_network_firewall.types.container_association_status.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_cbor(
            data["Tags"]
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    return out
