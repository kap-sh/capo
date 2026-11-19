"""Generated from Smithy shape ``com.amazonaws.fms#AssociateThirdPartyFirewallResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.third_party_firewall_association_status


class AssociateThirdPartyFirewallResponse(TypedDict, closed=True):
    third_party_firewall_status: NotRequired[
        "capo_fms.types.third_party_firewall_association_status.ThirdPartyFirewallAssociationStatus"
    ]
    """<p>The current status for setting a Firewall Manager policy administrator's account as an administrator of the third-party firewall tenant.</p> <ul> <li> <p> <code>ONBOARDING</code> - The Firewall Manager policy administrator is being designated as a tenant administrator.</p> </li> <li> <p> <code>ONBOARD_COMPLETE</code> - The Firewall Manager policy administrator is designated as a tenant administrator.</p> </li> <li> <p> <code>OFFBOARDING</code> - The Firewall Manager policy administrator is being removed as a tenant administrator.</p> </li> <li> <p> <code>OFFBOARD_COMPLETE</code> - The Firewall Manager policy administrator has been removed as a tenant administrator.</p> </li> <li> <p> <code>NOT_EXIST</code> - The Firewall Manager policy administrator doesn't exist as a tenant administrator.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateThirdPartyFirewallResponse) -> dict:
    out: dict = {}
    if "third_party_firewall_status" in value:
        import capo_fms.types.third_party_firewall_association_status

        out["ThirdPartyFirewallStatus"] = (
            capo_fms.types.third_party_firewall_association_status.serialize_aws_json_1_1(
                value["third_party_firewall_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateThirdPartyFirewallResponse:
    out: AssociateThirdPartyFirewallResponse = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewallStatus") is not None:
        import capo_fms.types.third_party_firewall_association_status

        out["third_party_firewall_status"] = (
            capo_fms.types.third_party_firewall_association_status.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateThirdPartyFirewallResponse) -> dict:
    out: dict = {}
    if "third_party_firewall_status" in value:
        import capo_fms.types.third_party_firewall_association_status

        out["ThirdPartyFirewallStatus"] = (
            capo_fms.types.third_party_firewall_association_status.serialize_cbor(
                value["third_party_firewall_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AssociateThirdPartyFirewallResponse:
    out: AssociateThirdPartyFirewallResponse = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewallStatus") is not None:
        import capo_fms.types.third_party_firewall_association_status

        out["third_party_firewall_status"] = (
            capo_fms.types.third_party_firewall_association_status.deserialize_cbor(
                data["ThirdPartyFirewallStatus"]
            )
        )
    return out
