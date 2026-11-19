"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ByolPricingTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type


class ByolPricingTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Type of the term being updated.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ByolPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ByolPricingTerm:
    out: ByolPricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ByolPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_cbor(data: dict) -> ByolPricingTerm:
    out: ByolPricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out
