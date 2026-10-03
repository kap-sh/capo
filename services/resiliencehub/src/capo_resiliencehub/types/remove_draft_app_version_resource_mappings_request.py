"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RemoveDraftAppVersionResourceMappingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_name_list
    import capo_resiliencehub.types.string255_list


class RemoveDraftAppVersionResourceMappingsRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    resource_names: NotRequired[
        "capo_resiliencehub.types.entity_name_list.EntityNameList"
    ]
    """<p>The names of the resources you want to remove from the resource mappings.</p>"""
    logical_stack_names: NotRequired[
        "capo_resiliencehub.types.string255_list.String255List"
    ]
    """<p>The names of the CloudFormation stacks you want to remove from the resource mappings.</p>"""
    app_registry_app_names: NotRequired[
        "capo_resiliencehub.types.entity_name_list.EntityNameList"
    ]
    """<p>The names of the registered applications you want to remove from the resource mappings.</p>"""
    resource_group_names: NotRequired[
        "capo_resiliencehub.types.entity_name_list.EntityNameList"
    ]
    """<p>The names of the resource groups you want to remove from the resource mappings.</p>"""
    terraform_source_names: NotRequired[
        "capo_resiliencehub.types.string255_list.String255List"
    ]
    """<p>The names of the Terraform sources you want to remove from the resource mappings.</p>"""
    eks_source_names: NotRequired[
        "capo_resiliencehub.types.string255_list.String255List"
    ]
    """<p>The names of the Amazon Elastic Kubernetes Service clusters and namespaces you want to remove from the resource mappings.</p> <note> <p>This parameter accepts values in "eks-cluster/namespace" format.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveDraftAppVersionResourceMappingsRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "resource_names" in value:
        import capo_resiliencehub.types.entity_name_list

        out["resourceNames"] = capo_resiliencehub.types.entity_name_list.serialize_json(
            value["resource_names"]
        )
    if "logical_stack_names" in value:
        import capo_resiliencehub.types.string255_list

        out["logicalStackNames"] = (
            capo_resiliencehub.types.string255_list.serialize_json(
                value["logical_stack_names"]
            )
        )
    if "app_registry_app_names" in value:
        import capo_resiliencehub.types.entity_name_list

        out["appRegistryAppNames"] = (
            capo_resiliencehub.types.entity_name_list.serialize_json(
                value["app_registry_app_names"]
            )
        )
    if "resource_group_names" in value:
        import capo_resiliencehub.types.entity_name_list

        out["resourceGroupNames"] = (
            capo_resiliencehub.types.entity_name_list.serialize_json(
                value["resource_group_names"]
            )
        )
    if "terraform_source_names" in value:
        import capo_resiliencehub.types.string255_list

        out["terraformSourceNames"] = (
            capo_resiliencehub.types.string255_list.serialize_json(
                value["terraform_source_names"]
            )
        )
    if "eks_source_names" in value:
        import capo_resiliencehub.types.string255_list

        out["eksSourceNames"] = capo_resiliencehub.types.string255_list.serialize_json(
            value["eks_source_names"]
        )
    return out


def deserialize_json(data: dict) -> RemoveDraftAppVersionResourceMappingsRequest:
    out: RemoveDraftAppVersionResourceMappingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "RemoveDraftAppVersionResourceMappingsRequest.app_arn required"
        )
    if data.get("resourceNames") is not None:
        import capo_resiliencehub.types.entity_name_list

        out["resource_names"] = (
            capo_resiliencehub.types.entity_name_list.deserialize_json(
                data["resourceNames"]
            )
        )
    if data.get("logicalStackNames") is not None:
        import capo_resiliencehub.types.string255_list

        out["logical_stack_names"] = (
            capo_resiliencehub.types.string255_list.deserialize_json(
                data["logicalStackNames"]
            )
        )
    if data.get("appRegistryAppNames") is not None:
        import capo_resiliencehub.types.entity_name_list

        out["app_registry_app_names"] = (
            capo_resiliencehub.types.entity_name_list.deserialize_json(
                data["appRegistryAppNames"]
            )
        )
    if data.get("resourceGroupNames") is not None:
        import capo_resiliencehub.types.entity_name_list

        out["resource_group_names"] = (
            capo_resiliencehub.types.entity_name_list.deserialize_json(
                data["resourceGroupNames"]
            )
        )
    if data.get("terraformSourceNames") is not None:
        import capo_resiliencehub.types.string255_list

        out["terraform_source_names"] = (
            capo_resiliencehub.types.string255_list.deserialize_json(
                data["terraformSourceNames"]
            )
        )
    if data.get("eksSourceNames") is not None:
        import capo_resiliencehub.types.string255_list

        out["eks_source_names"] = (
            capo_resiliencehub.types.string255_list.deserialize_json(
                data["eksSourceNames"]
            )
        )
    return out
