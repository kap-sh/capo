"""Generated from Smithy shape ``com.amazonaws.ssm#DisassociateOpsItemRelatedItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_related_item_association_id


class DisassociateOpsItemRelatedItemRequest(TypedDict, closed=True):
    ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId"
    """<p>The ID of the OpsItem for which you want to delete an association between the OpsItem and a related item.</p>"""
    association_id: "capo_ssm.types.ops_item_related_item_association_id.OpsItemRelatedItemAssociationId"
    """<p>The ID of the association for which you want to delete an association between the OpsItem and a related item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateOpsItemRelatedItemRequest) -> dict:
    out: dict = {}
    out["OpsItemId"] = value["ops_item_id"]
    out["AssociationId"] = value["association_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateOpsItemRelatedItemRequest:
    out: DisassociateOpsItemRelatedItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("OpsItemId") is not None:
        out["ops_item_id"] = data["OpsItemId"]
    else:
        out["ops_item_id"] = ""
    if data.get("AssociationId") is not None:
        out["association_id"] = data["AssociationId"]
    else:
        out["association_id"] = ""
    return out
