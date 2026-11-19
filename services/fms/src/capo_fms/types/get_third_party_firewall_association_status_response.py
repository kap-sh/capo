"""Generated from Smithy shape ``com.amazonaws.fms#GetThirdPartyFirewallAssociationStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.marketplace_subscription_onboarding_status
    import capo_fms.types.third_party_firewall_association_status


class GetThirdPartyFirewallAssociationStatusResponse(TypedDict, closed=True):
    third_party_firewall_status: NotRequired[
        "capo_fms.types.third_party_firewall_association_status.ThirdPartyFirewallAssociationStatus"
    ]
    """<p>The current status for setting a Firewall Manager policy administrators account as an administrator of the third-party firewall tenant.</p> <ul> <li> <p> <code>ONBOARDING</code> - The Firewall Manager policy administrator is being designated as a tenant administrator.</p> </li> <li> <p> <code>ONBOARD_COMPLETE</code> - The Firewall Manager policy administrator is designated as a tenant administrator.</p> </li> <li> <p> <code>OFFBOARDING</code> - The Firewall Manager policy administrator is being removed as a tenant administrator.</p> </li> <li> <p> <code>OFFBOARD_COMPLETE</code> - The Firewall Manager policy administrator has been removed as a tenant administrator.</p> </li> <li> <p> <code>NOT_EXIST</code> - The Firewall Manager policy administrator doesn't exist as a tenant administrator.</p> </li> </ul>"""
    marketplace_onboarding_status: NotRequired[
        "capo_fms.types.marketplace_subscription_onboarding_status.MarketplaceSubscriptionOnboardingStatus"
    ]
    """<p>The status for subscribing to the third-party firewall vendor in the Amazon Web Services Marketplace.</p> <ul> <li> <p> <code>NO_SUBSCRIPTION</code> - The Firewall Manager policy administrator isn't subscribed to the third-party firewall service in the Amazon Web Services Marketplace.</p> </li> <li> <p> <code>NOT_COMPLETE</code> - The Firewall Manager policy administrator is in the process of subscribing to the third-party firewall service in the Amazon Web Services Marketplace, but doesn't yet have an active subscription.</p> </li> <li> <p> <code>COMPLETE</code> - The Firewall Manager policy administrator has an active subscription to the third-party firewall service in the Amazon Web Services Marketplace.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetThirdPartyFirewallAssociationStatusResponse,
) -> dict:
    out: dict = {}
    if "third_party_firewall_status" in value:
        import capo_fms.types.third_party_firewall_association_status

        out["ThirdPartyFirewallStatus"] = (
            capo_fms.types.third_party_firewall_association_status.serialize_aws_json_1_1(
                value["third_party_firewall_status"]
            )
        )
    if "marketplace_onboarding_status" in value:
        import capo_fms.types.marketplace_subscription_onboarding_status

        out["MarketplaceOnboardingStatus"] = (
            capo_fms.types.marketplace_subscription_onboarding_status.serialize_aws_json_1_1(
                value["marketplace_onboarding_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetThirdPartyFirewallAssociationStatusResponse:
    out: GetThirdPartyFirewallAssociationStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewallStatus") is not None:
        import capo_fms.types.third_party_firewall_association_status

        out["third_party_firewall_status"] = (
            capo_fms.types.third_party_firewall_association_status.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallStatus"]
            )
        )
    if data.get("MarketplaceOnboardingStatus") is not None:
        import capo_fms.types.marketplace_subscription_onboarding_status

        out["marketplace_onboarding_status"] = (
            capo_fms.types.marketplace_subscription_onboarding_status.deserialize_aws_json_1_1(
                data["MarketplaceOnboardingStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetThirdPartyFirewallAssociationStatusResponse) -> dict:
    out: dict = {}
    if "third_party_firewall_status" in value:
        import capo_fms.types.third_party_firewall_association_status

        out["ThirdPartyFirewallStatus"] = (
            capo_fms.types.third_party_firewall_association_status.serialize_cbor(
                value["third_party_firewall_status"]
            )
        )
    if "marketplace_onboarding_status" in value:
        import capo_fms.types.marketplace_subscription_onboarding_status

        out["MarketplaceOnboardingStatus"] = (
            capo_fms.types.marketplace_subscription_onboarding_status.serialize_cbor(
                value["marketplace_onboarding_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetThirdPartyFirewallAssociationStatusResponse:
    out: GetThirdPartyFirewallAssociationStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewallStatus") is not None:
        import capo_fms.types.third_party_firewall_association_status

        out["third_party_firewall_status"] = (
            capo_fms.types.third_party_firewall_association_status.deserialize_cbor(
                data["ThirdPartyFirewallStatus"]
            )
        )
    if data.get("MarketplaceOnboardingStatus") is not None:
        import capo_fms.types.marketplace_subscription_onboarding_status

        out["marketplace_onboarding_status"] = (
            capo_fms.types.marketplace_subscription_onboarding_status.deserialize_cbor(
                data["MarketplaceOnboardingStatus"]
            )
        )
    return out
