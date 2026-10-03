"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclEntrySet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.boolean_object
    import capo_fms.types.network_acl_entries


class NetworkAclEntrySet(TypedDict, closed=True):
    first_entries: NotRequired["capo_fms.types.network_acl_entries.NetworkAclEntries"]
    """<p>The rules that you want to run first in the Firewall Manager managed network ACLs. </p> <note> <p>Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates. </p> </note> <p>You must specify at least one first entry or one last entry in any network ACL policy. </p>"""
    force_remediate_for_first_entries: "capo_fms.types.boolean_object.BooleanObject"
    """<p>Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries. </p> <p>If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation">Remediation for managed network ACLs</a> in the <i>Firewall Manager Developer Guide</i>.</p>"""
    last_entries: NotRequired["capo_fms.types.network_acl_entries.NetworkAclEntries"]
    """<p>The rules that you want to run last in the Firewall Manager managed network ACLs. </p> <note> <p>Provide these in the order in which you want them to run. Firewall Manager will assign the specific rule numbers for you, in the network ACLs that it creates. </p> </note> <p>You must specify at least one first entry or one last entry in any network ACL policy. </p>"""
    force_remediate_for_last_entries: "capo_fms.types.boolean_object.BooleanObject"
    """<p>Applies only when remediation is enabled for the policy as a whole. Firewall Manager uses this setting when it finds policy violations that involve conflicts between the custom entries and the policy entries. </p> <p>If forced remediation is disabled, Firewall Manager marks the network ACL as noncompliant and does not try to remediate. For more information about the remediation behavior, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/network-acl-policies.html#network-acls-remediation">Remediation for managed network ACLs</a> in the <i>Firewall Manager Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclEntrySet) -> dict:
    out: dict = {}
    if "first_entries" in value:
        import capo_fms.types.network_acl_entries

        out["FirstEntries"] = capo_fms.types.network_acl_entries.serialize_aws_json_1_1(
            value["first_entries"]
        )
    out["ForceRemediateForFirstEntries"] = value["force_remediate_for_first_entries"]
    if "last_entries" in value:
        import capo_fms.types.network_acl_entries

        out["LastEntries"] = capo_fms.types.network_acl_entries.serialize_aws_json_1_1(
            value["last_entries"]
        )
    out["ForceRemediateForLastEntries"] = value["force_remediate_for_last_entries"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAclEntrySet:
    out: NetworkAclEntrySet = {}  # type: ignore[typeddict-item]
    if data.get("FirstEntries") is not None:
        import capo_fms.types.network_acl_entries

        out["first_entries"] = (
            capo_fms.types.network_acl_entries.deserialize_aws_json_1_1(
                data["FirstEntries"]
            )
        )
    if data.get("ForceRemediateForFirstEntries") is not None:
        out["force_remediate_for_first_entries"] = data["ForceRemediateForFirstEntries"]
    else:
        raise DeserializationError(
            "NetworkAclEntrySet.force_remediate_for_first_entries required"
        )
    if data.get("LastEntries") is not None:
        import capo_fms.types.network_acl_entries

        out["last_entries"] = (
            capo_fms.types.network_acl_entries.deserialize_aws_json_1_1(
                data["LastEntries"]
            )
        )
    if data.get("ForceRemediateForLastEntries") is not None:
        out["force_remediate_for_last_entries"] = data["ForceRemediateForLastEntries"]
    else:
        raise DeserializationError(
            "NetworkAclEntrySet.force_remediate_for_last_entries required"
        )
    return out
