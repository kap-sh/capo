"""Generated from Smithy shape ``com.amazonaws.ssm#AssociateOpsItemRelatedItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_related_item_association_resource_type
    import capo_ssm.types.ops_item_related_item_association_resource_uri
    import capo_ssm.types.ops_item_related_item_association_type


class AssociateOpsItemRelatedItemRequest(TypedDict, closed=True):
    ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId"
    """<p>The ID of the OpsItem to which you want to associate a resource as a related item.</p>"""
    association_type: "capo_ssm.types.ops_item_related_item_association_type.OpsItemRelatedItemAssociationType"
    """<p>The type of association that you want to create between an OpsItem and a resource. OpsCenter supports <code>IsParentOf</code> and <code>RelatesTo</code> association types.</p>"""
    resource_type: "capo_ssm.types.ops_item_related_item_association_resource_type.OpsItemRelatedItemAssociationResourceType"
    """<p>The type of resource that you want to associate with an OpsItem. OpsCenter supports the following types:</p> <p> <code>AWS::SSMIncidents::IncidentRecord</code>: an Incident Manager incident. </p> <p> <code>AWS::SSM::Document</code>: a Systems Manager (SSM) document.</p>"""
    resource_uri: "capo_ssm.types.ops_item_related_item_association_resource_uri.OpsItemRelatedItemAssociationResourceUri"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services resource that you want to associate with the OpsItem.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateOpsItemRelatedItemRequest) -> dict:
    out: dict = {}
    out["OpsItemId"] = value["ops_item_id"]
    out["AssociationType"] = value["association_type"]
    out["ResourceType"] = value["resource_type"]
    out["ResourceUri"] = value["resource_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateOpsItemRelatedItemRequest:
    out: AssociateOpsItemRelatedItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    else:
        out["ops_item_id"] = ""
    if data.get("AssociationType") is not None:
        out["association_type"] = data["AssociationType"]
    else:
        out["association_type"] = ""
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("ResourceUri") is not None:
        out["resource_uri"] = data["ResourceUri"]
    else:
        out["resource_uri"] = ""
    return out
