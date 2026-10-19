"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateContainerAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.container_monitoring_configurations
    import capo_network_firewall.types.container_monitoring_type
    import capo_network_firewall.types.description
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.tag_list


class CreateContainerAssociationRequest(TypedDict, closed=True):
    container_association_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the container association. You can't change the name of a container association after you create it.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the container association.</p>"""
    type: (
        "capo_network_firewall.types.container_monitoring_type.ContainerMonitoringType"
    )
    """<p>The type of containers to monitor. You can't change the container type after creation. Valid values:</p> <ul> <li> <p> <code>ECS</code> - Amazon Elastic Container Service</p> </li> <li> <p> <code>EKS</code> - Amazon Elastic Kubernetes Service</p> </li> </ul>"""
    container_monitoring_configurations: "capo_network_firewall.types.container_monitoring_configurations.ContainerMonitoringConfigurations"
    """<p>The monitoring configurations for the container association. Each configuration specifies an Amazon ECS or Amazon EKS cluster to monitor and optional attribute filters to narrow which containers are tracked.</p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateContainerAssociationRequest) -> dict:
    out: dict = {}
    out["ContainerAssociationName"] = value["container_association_name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_network_firewall.types.container_monitoring_type

    out["Type"] = (
        capo_network_firewall.types.container_monitoring_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    import capo_network_firewall.types.container_monitoring_configurations

    out["ContainerMonitoringConfigurations"] = (
        capo_network_firewall.types.container_monitoring_configurations.serialize_aws_json_1_0(
            value["container_monitoring_configurations"]
        )
    )
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateContainerAssociationRequest:
    out: CreateContainerAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContainerAssociationName") is not None:
        out["container_association_name"] = data["ContainerAssociationName"]
    else:
        out["container_association_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_network_firewall.types.container_monitoring_type

        out["type"] = (
            capo_network_firewall.types.container_monitoring_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_network_firewall.types.container_monitoring_type.ContainerMonitoringType",
            "",
        )
    if data.get("ContainerMonitoringConfigurations") is not None:
        import capo_network_firewall.types.container_monitoring_configurations

        out["container_monitoring_configurations"] = (
            capo_network_firewall.types.container_monitoring_configurations.deserialize_aws_json_1_0(
                data["ContainerMonitoringConfigurations"]
            )
        )
    else:
        out["container_monitoring_configurations"] = []
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
