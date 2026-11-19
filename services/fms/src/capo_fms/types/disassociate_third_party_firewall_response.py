"""Generated from Smithy shape ``com.amazonaws.fms#DisassociateThirdPartyFirewallResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.third_party_firewall_association_status


class DisassociateThirdPartyFirewallResponse(TypedDict, closed=True):
    third_party_firewall_status: NotRequired[
        "capo_fms.types.third_party_firewall_association_status.ThirdPartyFirewallAssociationStatus"
    ]
    """<p>The current status for the disassociation of a Firewall Manager administrators account with a third-party firewall.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateThirdPartyFirewallResponse) -> dict:
    out: dict = {}
    if "third_party_firewall_status" in value:
        import capo_fms.types.third_party_firewall_association_status

        out["ThirdPartyFirewallStatus"] = (
            capo_fms.types.third_party_firewall_association_status.serialize_aws_json_1_1(
                value["third_party_firewall_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateThirdPartyFirewallResponse:
    out: DisassociateThirdPartyFirewallResponse = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewallStatus") is not None:
        import capo_fms.types.third_party_firewall_association_status

        out["third_party_firewall_status"] = (
            capo_fms.types.third_party_firewall_association_status.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisassociateThirdPartyFirewallResponse) -> dict:
    out: dict = {}
    if "third_party_firewall_status" in value:
        import capo_fms.types.third_party_firewall_association_status

        out["ThirdPartyFirewallStatus"] = (
            capo_fms.types.third_party_firewall_association_status.serialize_cbor(
                value["third_party_firewall_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DisassociateThirdPartyFirewallResponse:
    out: DisassociateThirdPartyFirewallResponse = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewallStatus") is not None:
        import capo_fms.types.third_party_firewall_association_status

        out["third_party_firewall_status"] = (
            capo_fms.types.third_party_firewall_association_status.deserialize_cbor(
                data["ThirdPartyFirewallStatus"]
            )
        )
    return out
