"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementEntitlementsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_entitlement_list
    import capo_marketplace_agreement.types.next_token


class GetAgreementEntitlementsOutput(TypedDict, closed=True):
    agreement_entitlements: NotRequired[
        "capo_marketplace_agreement.types.agreement_entitlement_list.AgreementEntitlementList"
    ]
    """<p>A list of agreement entitlements which are part of the latest agreement.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementEntitlementsOutput) -> dict:
    out: dict = {}
    if "agreement_entitlements" in value:
        import capo_marketplace_agreement.types.agreement_entitlement_list

        out["agreementEntitlements"] = (
            capo_marketplace_agreement.types.agreement_entitlement_list.serialize_aws_json_1_0(
                value["agreement_entitlements"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementEntitlementsOutput:
    out: GetAgreementEntitlementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementEntitlements") is not None:
        import capo_marketplace_agreement.types.agreement_entitlement_list

        out["agreement_entitlements"] = (
            capo_marketplace_agreement.types.agreement_entitlement_list.deserialize_aws_json_1_0(
                data["agreementEntitlements"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAgreementEntitlementsOutput) -> dict:
    out: dict = {}
    if "agreement_entitlements" in value:
        import capo_marketplace_agreement.types.agreement_entitlement_list

        out["agreementEntitlements"] = (
            capo_marketplace_agreement.types.agreement_entitlement_list.serialize_cbor(
                value["agreement_entitlements"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> GetAgreementEntitlementsOutput:
    out: GetAgreementEntitlementsOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementEntitlements") is not None:
        import capo_marketplace_agreement.types.agreement_entitlement_list

        out["agreement_entitlements"] = (
            capo_marketplace_agreement.types.agreement_entitlement_list.deserialize_cbor(
                data["agreementEntitlements"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: GetAgreementEntitlementsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "agreement_entitlements" in value:
        import capo_marketplace_agreement.types.agreement_entitlement_list

        out["agreement_entitlements"] = (
            capo_marketplace_agreement.types.agreement_entitlement_list.redact_sensitive(
                value["agreement_entitlements"]
            )
        )
    return out
