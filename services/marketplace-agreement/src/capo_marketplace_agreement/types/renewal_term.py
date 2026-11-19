"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#RenewalTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.day_duration
    import capo_marketplace_agreement.types.price_increase
    import capo_marketplace_agreement.types.renewal_term_configuration
    import capo_marketplace_agreement.types.term_id
    import capo_marketplace_agreement.types.term_template_list
    import capo_marketplace_agreement.types.unversioned_term_type


class RenewalTerm(TypedDict, closed=True):
    type: NotRequired[
        "capo_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Category of the term being updated. </p>"""
    id: NotRequired["capo_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    configuration: NotRequired[
        "capo_marketplace_agreement.types.renewal_term_configuration.RenewalTermConfiguration"
    ]
    """<p>Additional parameters specified by the acceptor while accepting the term.</p>"""
    lockout_period: NotRequired[
        "capo_marketplace_agreement.types.day_duration.DayDuration"
    ]
    """<p>The renewal decision deadline, measured back from the end date of the agreement. This is the last day either party can opt in to or opt out of the renewal. The duration is represented in the ISO 8601 format in whole days (for example, <code>P30D</code> for 30 days or <code>P60D</code> for 60 days).</p> <p>The field is <code>null</code> when no renewal decision deadline is set. In that case, either party can change the auto-renewal decision up to the end date of the agreement.</p>"""
    max_renewals: NotRequired["int"]
    """<p>The maximum number of times the agreement can be renewed. The field is <code>null</code> when the number of renewals is unlimited.</p> <p>After the agreement reaches this limit, it expires on its end date instead of renewing.</p>"""
    adjustment_deadline: NotRequired[
        "capo_marketplace_agreement.types.day_duration.DayDuration"
    ]
    """<p>The date by which the proposer must finalize the price increase for the next renewal, measured back from the end date of the agreement. The duration is represented in the ISO 8601 format in whole days (for example, <code>P30D</code> for 30 days or <code>P60D</code> for 60 days).</p> <p>This field applies only when <code>PriceIncrease</code> is a <code>PercentageRange</code>. The field is <code>null</code> when <code>PriceIncrease</code> is a <code>FixedPercentage</code>, because the price increase is already fixed and there is nothing for the proposer to finalize. If the proposer doesn't finalize a value by the adjustment deadline, the <code>DefaultValue</code> of the range applies.</p> <p> <code>AdjustmentDeadline</code> must be greater than <code>LockoutPeriod</code>.</p>"""
    price_increase: NotRequired[
        "capo_marketplace_agreement.types.price_increase.PriceIncrease"
    ]
    """<p>The price increase that is applied each time the agreement renews. The field is <code>null</code> when the price doesn't change at renewal.</p>"""
    term_templates: NotRequired[
        "capo_marketplace_agreement.types.term_template_list.TermTemplateList"
    ]
    """<p>Defines how specific terms change each time the agreement renews. The field is <code>null</code> when no terms change at renewal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RenewalTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "configuration" in value:
        import capo_marketplace_agreement.types.renewal_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.renewal_term_configuration.serialize_aws_json_1_0(
                value["configuration"]
            )
        )
    if "lockout_period" in value:
        out["lockoutPeriod"] = value["lockout_period"]
    if "max_renewals" in value:
        out["maxRenewals"] = value["max_renewals"]
    if "adjustment_deadline" in value:
        out["adjustmentDeadline"] = value["adjustment_deadline"]
    if "price_increase" in value:
        import capo_marketplace_agreement.types.price_increase

        out["priceIncrease"] = (
            capo_marketplace_agreement.types.price_increase.serialize_aws_json_1_0(
                value["price_increase"]
            )
        )
    if "term_templates" in value:
        import capo_marketplace_agreement.types.term_template_list

        out["termTemplates"] = (
            capo_marketplace_agreement.types.term_template_list.serialize_aws_json_1_0(
                value["term_templates"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RenewalTerm:
    out: RenewalTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("configuration") is not None:
        import capo_marketplace_agreement.types.renewal_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.renewal_term_configuration.deserialize_aws_json_1_0(
                data["configuration"]
            )
        )
    if data.get("lockoutPeriod") is not None:
        out["lockout_period"] = data["lockoutPeriod"]
    if data.get("maxRenewals") is not None:
        out["max_renewals"] = data["maxRenewals"]
    if data.get("adjustmentDeadline") is not None:
        out["adjustment_deadline"] = data["adjustmentDeadline"]
    if data.get("priceIncrease") is not None:
        import capo_marketplace_agreement.types.price_increase

        out["price_increase"] = (
            capo_marketplace_agreement.types.price_increase.deserialize_aws_json_1_0(
                data["priceIncrease"]
            )
        )
    if data.get("termTemplates") is not None:
        import capo_marketplace_agreement.types.term_template_list

        out["term_templates"] = (
            capo_marketplace_agreement.types.term_template_list.deserialize_aws_json_1_0(
                data["termTemplates"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RenewalTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "configuration" in value:
        import capo_marketplace_agreement.types.renewal_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.renewal_term_configuration.serialize_cbor(
                value["configuration"]
            )
        )
    if "lockout_period" in value:
        out["lockoutPeriod"] = value["lockout_period"]
    if "max_renewals" in value:
        out["maxRenewals"] = value["max_renewals"]
    if "adjustment_deadline" in value:
        out["adjustmentDeadline"] = value["adjustment_deadline"]
    if "price_increase" in value:
        import capo_marketplace_agreement.types.price_increase

        out["priceIncrease"] = (
            capo_marketplace_agreement.types.price_increase.serialize_cbor(
                value["price_increase"]
            )
        )
    if "term_templates" in value:
        import capo_marketplace_agreement.types.term_template_list

        out["termTemplates"] = (
            capo_marketplace_agreement.types.term_template_list.serialize_cbor(
                value["term_templates"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RenewalTerm:
    out: RenewalTerm = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("configuration") is not None:
        import capo_marketplace_agreement.types.renewal_term_configuration

        out["configuration"] = (
            capo_marketplace_agreement.types.renewal_term_configuration.deserialize_cbor(
                data["configuration"]
            )
        )
    if data.get("lockoutPeriod") is not None:
        out["lockout_period"] = data["lockoutPeriod"]
    if data.get("maxRenewals") is not None:
        out["max_renewals"] = data["maxRenewals"]
    if data.get("adjustmentDeadline") is not None:
        out["adjustment_deadline"] = data["adjustmentDeadline"]
    if data.get("priceIncrease") is not None:
        import capo_marketplace_agreement.types.price_increase

        out["price_increase"] = (
            capo_marketplace_agreement.types.price_increase.deserialize_cbor(
                data["priceIncrease"]
            )
        )
    if data.get("termTemplates") is not None:
        import capo_marketplace_agreement.types.term_template_list

        out["term_templates"] = (
            capo_marketplace_agreement.types.term_template_list.deserialize_cbor(
                data["termTemplates"]
            )
        )
    return out
