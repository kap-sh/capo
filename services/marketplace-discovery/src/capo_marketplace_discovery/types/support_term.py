"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SupportTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_type


class SupportTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    refund_policy: "capo_marketplace_discovery.types.bounded_string.BoundedString"
    """<p>The refund policy description for the offer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["refundPolicy"] = value["refund_policy"]
    return out


def deserialize_json(data: dict) -> SupportTerm:
    out: SupportTerm = {}  # type: ignore[typeddict-item]
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
    if data.get("refundPolicy") is not None:
        out["refund_policy"] = data["refundPolicy"]
    else:
        out["refund_policy"] = ""
    return out
