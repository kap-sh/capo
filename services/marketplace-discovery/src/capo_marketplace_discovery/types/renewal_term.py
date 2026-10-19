"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#RenewalTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.bounded_string
    import capo_marketplace_discovery.types.price_increase
    import capo_marketplace_discovery.types.term_id
    import capo_marketplace_discovery.types.term_template_list
    import capo_marketplace_discovery.types.term_type


class RenewalTerm(TypedDict, closed=True):
    id: "capo_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "capo_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    max_renewals: NotRequired["int"]
    """<p>The maximum number of renewals allowed on this offer. Absent means unlimited renewals.</p>"""
    lockout_period: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>The duration before the agreement end date when the lockout window begins, in ISO 8601 format (for example, P30D). Absent means no lockout.</p>"""
    adjustment_deadline: NotRequired[
        "capo_marketplace_discovery.types.bounded_string.BoundedString"
    ]
    """<p>The duration before the agreement end date by which the renewal price is finalized, represented in ISO 8601 format (for example, P30D). Only applicable with <code>PercentageRange</code>.</p>"""
    price_increase: NotRequired[
        "capo_marketplace_discovery.types.price_increase.PriceIncrease"
    ]
    """<p>The price increase applied at each renewal cycle. Absent means identical pricing on renewal.</p>"""
    term_templates: NotRequired[
        "capo_marketplace_discovery.types.term_template_list.TermTemplateList"
    ]
    """<p>Structural templates defining how specific terms are reshaped on each renewal cycle. Absent for upfront-only offers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenewalTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_marketplace_discovery.types.term_type

    out["type"] = capo_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    if "max_renewals" in value:
        out["maxRenewals"] = value["max_renewals"]
    if "lockout_period" in value:
        out["lockoutPeriod"] = value["lockout_period"]
    if "adjustment_deadline" in value:
        out["adjustmentDeadline"] = value["adjustment_deadline"]
    if "price_increase" in value:
        import capo_marketplace_discovery.types.price_increase

        out["priceIncrease"] = (
            capo_marketplace_discovery.types.price_increase.serialize_json(
                value["price_increase"]
            )
        )
    if "term_templates" in value:
        import capo_marketplace_discovery.types.term_template_list

        out["termTemplates"] = (
            capo_marketplace_discovery.types.term_template_list.serialize_json(
                value["term_templates"]
            )
        )
    return out


def deserialize_json(data: dict) -> RenewalTerm:
    out: RenewalTerm = {}  # type: ignore[typeddict-item]
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
    if data.get("maxRenewals") is not None:
        out["max_renewals"] = data["maxRenewals"]
    if data.get("lockoutPeriod") is not None:
        out["lockout_period"] = data["lockoutPeriod"]
    if data.get("adjustmentDeadline") is not None:
        out["adjustment_deadline"] = data["adjustmentDeadline"]
    if data.get("priceIncrease") is not None:
        import capo_marketplace_discovery.types.price_increase

        out["price_increase"] = (
            capo_marketplace_discovery.types.price_increase.deserialize_json(
                data["priceIncrease"]
            )
        )
    if data.get("termTemplates") is not None:
        import capo_marketplace_discovery.types.term_template_list

        out["term_templates"] = (
            capo_marketplace_discovery.types.term_template_list.deserialize_json(
                data["termTemplates"]
            )
        )
    return out
