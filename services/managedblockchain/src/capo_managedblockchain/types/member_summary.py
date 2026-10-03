"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.arn_string
    import capo_managedblockchain.types.description_string
    import capo_managedblockchain.types.is_owned
    import capo_managedblockchain.types.member_status
    import capo_managedblockchain.types.network_member_name_string
    import capo_managedblockchain.types.resource_id_string
    import capo_managedblockchain.types.timestamp


class MemberSummary(TypedDict, closed=True):
    id: NotRequired["capo_managedblockchain.types.resource_id_string.ResourceIdString"]
    """<p>The unique identifier of the member.</p>"""
    name: NotRequired[
        "capo_managedblockchain.types.network_member_name_string.NetworkMemberNameString"
    ]
    """<p>The name of the member.</p>"""
    description: NotRequired[
        "capo_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>An optional description of the member.</p>"""
    status: NotRequired["capo_managedblockchain.types.member_status.MemberStatus"]
    """<p>The status of the member.</p> <ul> <li> <p> <code>CREATING</code> - The Amazon Web Services account is in the process of creating a member.</p> </li> <li> <p> <code>AVAILABLE</code> - The member has been created and can participate in the network.</p> </li> <li> <p> <code>CREATE_FAILED</code> - The Amazon Web Services account attempted to create a member and creation failed.</p> </li> <li> <p> <code>UPDATING</code> - The member is in the process of being updated.</p> </li> <li> <p> <code>DELETING</code> - The member and all associated resources are in the process of being deleted. Either the Amazon Web Services account that owns the member deleted it, or the member is being deleted as the result of an <code>APPROVED</code> <code>PROPOSAL</code> to remove the member.</p> </li> <li> <p> <code>DELETED</code> - The member can no longer participate on the network and all associated resources are deleted. Either the Amazon Web Services account that owns the member deleted it, or the member is being deleted as the result of an <code>APPROVED</code> <code>PROPOSAL</code> to remove the member.</p> </li> <li> <p> <code>INACCESSIBLE_ENCRYPTION_KEY</code> - The member is impaired and might not function as expected because it cannot access the specified customer managed key in Key Management Service (KMS) for encryption at rest. Either the KMS key was disabled or deleted, or the grants on the key were revoked.</p> <p>The effect of disabling or deleting a key or of revoking a grant isn't immediate. It might take some time for the member resource to discover that the key is inaccessible. When a resource is in this state, we recommend deleting and recreating the resource.</p> </li> </ul>"""
    creation_date: NotRequired["capo_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the member was created.</p>"""
    is_owned: NotRequired["capo_managedblockchain.types.is_owned.IsOwned"]
    """<p>An indicator of whether the member is owned by your Amazon Web Services account or a different Amazon Web Services account.</p>"""
    arn: NotRequired["capo_managedblockchain.types.arn_string.ArnString"]
    """<p>The Amazon Resource Name (ARN) of the member. For more information about ARNs and their format, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_managedblockchain.types.member_status

        out["Status"] = capo_managedblockchain.types.member_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import capo_managedblockchain.types.timestamp

        out["CreationDate"] = capo_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "is_owned" in value:
        out["IsOwned"] = value["is_owned"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> MemberSummary:
    out: MemberSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_managedblockchain.types.member_status

        out["status"] = capo_managedblockchain.types.member_status.deserialize_json(
            data["Status"]
        )
    if data.get("CreationDate") is not None:
        import capo_managedblockchain.types.timestamp

        out["creation_date"] = capo_managedblockchain.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if data.get("IsOwned") is not None:
        out["is_owned"] = data["IsOwned"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out
