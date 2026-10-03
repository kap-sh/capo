"""Generated from Smithy shape ``com.amazonaws.resiliencehub#LogicalResourceId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.string255


class LogicalResourceId(TypedDict, closed=True):
    identifier: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier of the resource.</p>"""
    logical_stack_name: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>The name of the CloudFormation stack this resource belongs to.</p>"""
    resource_group_name: NotRequired["capo_resiliencehub.types.entity_name.EntityName"]
    """<p>The name of the resource group that this resource belongs to.</p>"""
    terraform_source_name: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p> The name of the Terraform S3 state file this resource belongs to. </p>"""
    eks_source_name: NotRequired["capo_resiliencehub.types.string255.String255"]
    """<p>Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.</p> <note> <p>This parameter accepts values in "eks-cluster/namespace" format.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogicalResourceId) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "logical_stack_name" in value:
        out["logicalStackName"] = value["logical_stack_name"]
    if "resource_group_name" in value:
        out["resourceGroupName"] = value["resource_group_name"]
    if "terraform_source_name" in value:
        out["terraformSourceName"] = value["terraform_source_name"]
    if "eks_source_name" in value:
        out["eksSourceName"] = value["eks_source_name"]
    return out


def deserialize_json(data: dict) -> LogicalResourceId:
    out: LogicalResourceId = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("LogicalResourceId.identifier required")
    if data.get("logicalStackName") is not None:
        out["logical_stack_name"] = data["logicalStackName"]
    if data.get("resourceGroupName") is not None:
        out["resource_group_name"] = data["resourceGroupName"]
    if data.get("terraformSourceName") is not None:
        out["terraform_source_name"] = data["terraformSourceName"]
    if data.get("eksSourceName") is not None:
        out["eks_source_name"] = data["eksSourceName"]
    return out
