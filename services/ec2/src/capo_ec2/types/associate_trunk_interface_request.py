"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTrunkInterfaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.network_interface_id
    import capo_ec2.types.string


class AssociateTrunkInterfaceRequest(TypedDict, closed=True):
    branch_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the branch network interface.</p>"""
    trunk_interface_id: NotRequired[
        "capo_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the trunk network interface.</p>"""
    vlan_id: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The ID of the VLAN. This applies to the VLAN protocol.</p>"""
    gre_key: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The application key. This applies to the GRE protocol.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateTrunkInterfaceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "branch_interface_id" in value:
        pairs.append(
            (f"{key_prefix}BranchInterfaceId", str(value["branch_interface_id"]))
        )
    if "trunk_interface_id" in value:
        pairs.append(
            (f"{key_prefix}TrunkInterfaceId", str(value["trunk_interface_id"]))
        )
    if "vlan_id" in value:
        pairs.append((f"{key_prefix}VlanId", str(value["vlan_id"])))
    if "gre_key" in value:
        pairs.append((f"{key_prefix}GreKey", str(value["gre_key"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> AssociateTrunkInterfaceRequest:
    out: AssociateTrunkInterfaceRequest = {}  # type: ignore[typeddict-item]
    child_branch_interface_id = el.find("BranchInterfaceId")
    if child_branch_interface_id is not None:
        out["branch_interface_id"] = str(child_branch_interface_id.text or "")
    child_trunk_interface_id = el.find("TrunkInterfaceId")
    if child_trunk_interface_id is not None:
        out["trunk_interface_id"] = str(child_trunk_interface_id.text or "")
    child_vlan_id = el.find("VlanId")
    if child_vlan_id is not None:
        out["vlan_id"] = int(child_vlan_id.text or "")
    child_gre_key = el.find("GreKey")
    if child_gre_key is not None:
        out["gre_key"] = int(child_gre_key.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
