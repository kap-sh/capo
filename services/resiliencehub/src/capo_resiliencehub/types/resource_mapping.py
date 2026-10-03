"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.physical_resource_id
    import capo_resiliencehub.types.resource_mapping_type
    import capo_resiliencehub.types.string255


class ResourceMapping(TypedDict, closed=True):
    resource_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the resource that this resource is mapped to when the <code>mappingType</code> is <code>Resource</code>.</p>"""
    logical_stack_name: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Name of the CloudFormation stack this resource is mapped to when the <code>mappingType</code> is <code>CfnStack</code>.</p>"""
    app_registry_app_name: NotRequired[
        "capo_resiliencehub.types.entity_name.EntityName"
    ]
    """<p>Name of the application this resource is mapped to when the <code>mappingType</code> is <code>AppRegistryApp</code>.</p>"""
    resource_group_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>Name of the Resource Groups that this resource is mapped to when the <code>mappingType</code> is <code>ResourceGroup</code>.</p>"""
    mapping_type: "capo_resiliencehub.types.resource_mapping_type.ResourceMappingType"
    """<p>Specifies the type of resource mapping.</p>"""
    physical_resource_id: (
        "capo_resiliencehub.types.physical_resource_id.PhysicalResourceId"
    )
    """<p>Identifier of the physical resource.</p>"""
    terraform_source_name: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Name of the Terraform source that this resource is mapped to when the <code>mappingType</code> is <code>Terraform</code>.</p>"""
    eks_source_name: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Name of the Amazon Elastic Kubernetes Service cluster and namespace that this resource is mapped to when the <code>mappingType</code> is <code>EKS</code>.</p> <note> <p>This parameter accepts values in "eks-cluster/namespace" format.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMapping) -> dict:
    out: dict = {}
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "logical_stack_name" in value:
        out["logicalStackName"] = value["logical_stack_name"]
    if "app_registry_app_name" in value:
        out["appRegistryAppName"] = value["app_registry_app_name"]
    if "resource_group_name" in value:
        out["resourceGroupName"] = value["resource_group_name"]
    import capo_resiliencehub.types.resource_mapping_type

    out["mappingType"] = capo_resiliencehub.types.resource_mapping_type.serialize_json(
        value["mapping_type"]
    )
    import capo_resiliencehub.types.physical_resource_id

    out["physicalResourceId"] = (
        capo_resiliencehub.types.physical_resource_id.serialize_json(
            value["physical_resource_id"]
        )
    )
    if "terraform_source_name" in value:
        out["terraformSourceName"] = value["terraform_source_name"]
    if "eks_source_name" in value:
        out["eksSourceName"] = value["eks_source_name"]
    return out


def deserialize_json(data: dict) -> ResourceMapping:
    out: ResourceMapping = {}  # type: ignore[typeddict-item]
    if data.get("resourceName") is not None:
        out["resource_name"] = data["resourceName"]
    if data.get("logicalStackName") is not None:
        out["logical_stack_name"] = data["logicalStackName"]
    if data.get("appRegistryAppName") is not None:
        out["app_registry_app_name"] = data["appRegistryAppName"]
    if data.get("resourceGroupName") is not None:
        out["resource_group_name"] = data["resourceGroupName"]
    if data.get("mappingType") is not None:
        import capo_resiliencehub.types.resource_mapping_type

        out["mapping_type"] = (
            capo_resiliencehub.types.resource_mapping_type.deserialize_json(
                data["mappingType"]
            )
        )
    else:
        raise DeserializationError("ResourceMapping.mapping_type required")
    if data.get("physicalResourceId") is not None:
        import capo_resiliencehub.types.physical_resource_id

        out["physical_resource_id"] = (
            capo_resiliencehub.types.physical_resource_id.deserialize_json(
                data["physicalResourceId"]
            )
        )
    else:
        raise DeserializationError("ResourceMapping.physical_resource_id required")
    if data.get("terraformSourceName") is not None:
        out["terraform_source_name"] = data["terraformSourceName"]
    if data.get("eksSourceName") is not None:
        out["eks_source_name"] = data["eksSourceName"]
    return out
