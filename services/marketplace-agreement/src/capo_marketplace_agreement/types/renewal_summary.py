"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RenewalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.offer_id


class RenewalSummary(TypedDict, closed=True):
    offer_id: NotRequired["capo_marketplace_agreement.types.offer_id.OfferId"]
    """<p>The unique identifier of the offer that provides the terms for the next renewal cycle. For most renewals, this is the same offer that the agreement was created from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RenewalSummary) -> dict:
    out: dict = {}
    if "offer_id" in value:
        out["offerId"] = value["offer_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RenewalSummary:
    out: RenewalSummary = {}  # type: ignore[typeddict-item]
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RenewalSummary) -> dict:
    out: dict = {}
    if "offer_id" in value:
        out["offerId"] = value["offer_id"]
    return out


def deserialize_cbor(data: dict) -> RenewalSummary:
    out: RenewalSummary = {}  # type: ignore[typeddict-item]
    if data.get("offerId") is not None:
        out["offer_id"] = data["offerId"]
    return out
