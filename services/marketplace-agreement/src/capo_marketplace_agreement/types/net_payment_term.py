"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#NetPaymentTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type


class NetPaymentTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Type of the term being updated.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    payment_due_period: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>The duration after an invoice is issued within which the payment is due. The duration is represented in the ISO 8601 format (for example, <code>P30D</code> for 30 days or <code>P60D</code> for 60 days).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetPaymentTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "payment_due_period" in value:
        out["paymentDuePeriod"] = value["payment_due_period"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NetPaymentTerm:
    out: NetPaymentTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("paymentDuePeriod") is not None:
        out["payment_due_period"] = data["paymentDuePeriod"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetPaymentTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "payment_due_period" in value:
        out["paymentDuePeriod"] = value["payment_due_period"]
    return out


def deserialize_cbor(data: dict) -> NetPaymentTerm:
    out: NetPaymentTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("paymentDuePeriod") is not None:
        out["payment_due_period"] = data["paymentDuePeriod"]
    return out
