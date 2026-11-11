"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FreeTrialPricingTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.grant_list
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.unversioned_term_type


class FreeTrialPricingTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term.</p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the terms.</p>"""
    duration: NotRequired[
        "capo_marketplace_agreement.types.bounded_string.BoundedString"
    ]
    """<p>Duration of the free trial period. The allowed duration depends on the product type. For SaaS products, the free trial lasts 7 to 90 days.</p>"""
    grants: NotRequired["capo_marketplace_agreement.types.grant_list.GrantList"]
    """<p>Entitlements granted to the acceptor of a free trial as part of an agreement execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FreeTrialPricingTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "grants" in value:
        import capo_marketplace_agreement.types.grant_list

        out["grants"] = (
            capo_marketplace_agreement.types.grant_list.serialize_aws_json_1_0(
                value["grants"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FreeTrialPricingTerm:
    out: FreeTrialPricingTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("duration") is not None:
        out["duration"] = data["duration"]
    if data.get("grants") is not None:
        import capo_marketplace_agreement.types.grant_list

        out["grants"] = (
            capo_marketplace_agreement.types.grant_list.deserialize_aws_json_1_0(
                data["grants"]
            )
        )
    return out
