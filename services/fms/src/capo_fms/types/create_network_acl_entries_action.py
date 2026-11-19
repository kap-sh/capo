"""Generated from Smithy shape ``com.amazonaws.fms#CreateNetworkAclEntriesAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.action_target
    import capo_fms.types.boolean
    import capo_fms.types.entries_description
    import capo_fms.types.length_bounded_string


class CreateNetworkAclEntriesAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>Brief description of this remediation action. </p>"""
    network_acl_id: NotRequired["capo_fms.types.action_target.ActionTarget"]
    """<p>The network ACL that's associated with the remediation action.</p>"""
    network_acl_entries_to_be_created: NotRequired[
        "capo_fms.types.entries_description.EntriesDescription"
    ]
    """<p>Lists the entries that the remediation action would create.</p>"""
    fms_can_remediate: "capo_fms.types.boolean.Boolean"
    """<p>Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNetworkAclEntriesAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "network_acl_id" in value:
        import capo_fms.types.action_target

        out["NetworkAclId"] = capo_fms.types.action_target.serialize_aws_json_1_1(
            value["network_acl_id"]
        )
    if "network_acl_entries_to_be_created" in value:
        import capo_fms.types.entries_description

        out["NetworkAclEntriesToBeCreated"] = (
            capo_fms.types.entries_description.serialize_aws_json_1_1(
                value["network_acl_entries_to_be_created"]
            )
        )
    out["FMSCanRemediate"] = value.get("fms_can_remediate", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNetworkAclEntriesAction:
    out: CreateNetworkAclEntriesAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("NetworkAclId") is not None:
        import capo_fms.types.action_target

        out["network_acl_id"] = capo_fms.types.action_target.deserialize_aws_json_1_1(
            data["NetworkAclId"]
        )
    if data.get("NetworkAclEntriesToBeCreated") is not None:
        import capo_fms.types.entries_description

        out["network_acl_entries_to_be_created"] = (
            capo_fms.types.entries_description.deserialize_aws_json_1_1(
                data["NetworkAclEntriesToBeCreated"]
            )
        )
    if data.get("FMSCanRemediate") is not None:
        out["fms_can_remediate"] = data["FMSCanRemediate"]
    else:
        out["fms_can_remediate"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateNetworkAclEntriesAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "network_acl_id" in value:
        import capo_fms.types.action_target

        out["NetworkAclId"] = capo_fms.types.action_target.serialize_cbor(
            value["network_acl_id"]
        )
    if "network_acl_entries_to_be_created" in value:
        import capo_fms.types.entries_description

        out["NetworkAclEntriesToBeCreated"] = (
            capo_fms.types.entries_description.serialize_cbor(
                value["network_acl_entries_to_be_created"]
            )
        )
    out["FMSCanRemediate"] = value.get("fms_can_remediate", False)
    return out


def deserialize_cbor(data: dict) -> CreateNetworkAclEntriesAction:
    out: CreateNetworkAclEntriesAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("NetworkAclId") is not None:
        import capo_fms.types.action_target

        out["network_acl_id"] = capo_fms.types.action_target.deserialize_cbor(
            data["NetworkAclId"]
        )
    if data.get("NetworkAclEntriesToBeCreated") is not None:
        import capo_fms.types.entries_description

        out["network_acl_entries_to_be_created"] = (
            capo_fms.types.entries_description.deserialize_cbor(
                data["NetworkAclEntriesToBeCreated"]
            )
        )
    if data.get("FMSCanRemediate") is not None:
        out["fms_can_remediate"] = data["FMSCanRemediate"]
    else:
        out["fms_can_remediate"] = False
    return out
