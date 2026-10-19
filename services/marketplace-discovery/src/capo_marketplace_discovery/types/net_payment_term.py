"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#NetPaymentTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class NetPaymentTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    payment_due_period: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The duration after invoice date by which payment is due.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetPaymentTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["paymentDuePeriod"] = value["payment_due_period"]
    return out


def deserialize_json(data: dict) -> NetPaymentTerm:
    out: NetPaymentTerm = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_marketplace_discovery.types.term_type

        out["type"] = capo_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_marketplace_discovery.types.term_type.TermType", ""
        )
    if data.get("paymentDuePeriod") is not None:
        out["payment_due_period"] = data["paymentDuePeriod"]
    else:
        out["payment_due_period"] = ""
    return out
