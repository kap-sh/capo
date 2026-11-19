"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SupportTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type


class SupportTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term being updated.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    refund_policy: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Free-text field about the refund policy description that will be shown to customers as is on the website and console.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "refund_policy" in value:
        out["refundPolicy"] = value["refund_policy"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SupportTerm:
    out: SupportTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("refundPolicy") is not None:
        out["refund_policy"] = data["refundPolicy"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SupportTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "refund_policy" in value:
        out["refundPolicy"] = value["refund_policy"]
    return out


def deserialize_cbor(data: dict) -> SupportTerm:
    out: SupportTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("refundPolicy") is not None:
        out["refund_policy"] = data["refundPolicy"]
    return out
