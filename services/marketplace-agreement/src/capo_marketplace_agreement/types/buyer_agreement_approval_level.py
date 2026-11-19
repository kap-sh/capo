"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApprovalLevel``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_level_name
    import capo_marketplace_agreement.types.buyer_agreement_approval_groups


class BuyerAgreementApprovalLevel(TypedDict, closed=True):
    name: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_level_name.AgreementApprovalLevelName"
    ]
    """<p>The name of the level.</p>"""
    groups: "capo_marketplace_agreement.types.buyer_agreement_approval_groups.BuyerAgreementApprovalGroups"
    """<p>The group of approvers at this level.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApprovalLevel) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import capo_marketplace_agreement.types.buyer_agreement_approval_groups

    out["groups"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_groups.serialize_aws_json_1_0(
            value["groups"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApprovalLevel:
    out: BuyerAgreementApprovalLevel = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("groups") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_groups

        out["groups"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_groups.deserialize_aws_json_1_0(
                data["groups"]
            )
        )
    else:
        out["groups"] = []
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuyerAgreementApprovalLevel) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    import capo_marketplace_agreement.types.buyer_agreement_approval_groups

    out["groups"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_groups.serialize_cbor(
            value["groups"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> BuyerAgreementApprovalLevel:
    out: BuyerAgreementApprovalLevel = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("groups") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_groups

        out["groups"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_groups.deserialize_cbor(
                data["groups"]
            )
        )
    else:
        out["groups"] = []
    return out


def redact_sensitive(value: BuyerAgreementApprovalLevel) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "groups" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_groups

        out["groups"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_groups.redact_sensitive(
                value["groups"]
            )
        )
    return out
