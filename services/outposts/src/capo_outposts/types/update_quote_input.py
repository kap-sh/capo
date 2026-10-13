"""Generated from Smithy shape ``com.amazonaws.outposts#UpdateQuoteInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.country_code
    import capo_outposts.types.outpost_identifier_or_empty
    import capo_outposts.types.payment_option_list
    import capo_outposts.types.payment_term_list
    import capo_outposts.types.quote_capacity_list
    import capo_outposts.types.quote_constraint_list
    import capo_outposts.types.quote_description
    import capo_outposts.types.quote_identifier


class UpdateQuoteInput(TypedDict, closed=True):
    quote_identifier: "capo_outposts.types.quote_identifier.QuoteIdentifier"
    """<p>The ID of the quote.</p>"""
    outpost_identifier: NotRequired[
        "capo_outposts.types.outpost_identifier_or_empty.OutpostIdentifierOrEmpty"
    ]
    """<p>The ID or ARN of the Outpost to associate with the quote. Specify an empty string to remove the Outpost association.</p>"""
    country_code: NotRequired["capo_outposts.types.country_code.CountryCode"]
    """<p>The country code for the Outpost site location.</p>"""
    requested_capacities: NotRequired[
        "capo_outposts.types.quote_capacity_list.QuoteCapacityList"
    ]
    """<p>The updated capacity requirements for the quote.</p>"""
    requested_constraints: NotRequired[
        "capo_outposts.types.quote_constraint_list.QuoteConstraintList"
    ]
    """<p>The updated physical constraints for the quote.</p>"""
    requested_payment_options: NotRequired[
        "capo_outposts.types.payment_option_list.PaymentOptionList"
    ]
    """<p>The updated payment options to include in the quote pricing.</p>"""
    requested_payment_terms: NotRequired[
        "capo_outposts.types.payment_term_list.PaymentTermList"
    ]
    """<p>The updated payment terms to include in the quote pricing.</p>"""
    description: NotRequired["capo_outposts.types.quote_description.QuoteDescription"]
    """<p>A description for the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuoteInput) -> dict:
    out: dict = {}
    if "outpost_identifier" in value:
        out["OutpostIdentifier"] = value["outpost_identifier"]
    if "country_code" in value:
        out["CountryCode"] = value["country_code"]
    if "requested_capacities" in value:
        import capo_outposts.types.quote_capacity_list

        out["RequestedCapacities"] = (
            capo_outposts.types.quote_capacity_list.serialize_json(
                value["requested_capacities"]
            )
        )
    if "requested_constraints" in value:
        import capo_outposts.types.quote_constraint_list

        out["RequestedConstraints"] = (
            capo_outposts.types.quote_constraint_list.serialize_json(
                value["requested_constraints"]
            )
        )
    if "requested_payment_options" in value:
        import capo_outposts.types.payment_option_list

        out["RequestedPaymentOptions"] = (
            capo_outposts.types.payment_option_list.serialize_json(
                value["requested_payment_options"]
            )
        )
    if "requested_payment_terms" in value:
        import capo_outposts.types.payment_term_list

        out["RequestedPaymentTerms"] = (
            capo_outposts.types.payment_term_list.serialize_json(
                value["requested_payment_terms"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateQuoteInput:
    out: UpdateQuoteInput = {}  # type: ignore[typeddict-item]
    if data.get("OutpostIdentifier") is not None:
        out["outpost_identifier"] = data["OutpostIdentifier"]
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    if data.get("RequestedCapacities") is not None:
        import capo_outposts.types.quote_capacity_list

        out["requested_capacities"] = (
            capo_outposts.types.quote_capacity_list.deserialize_json(
                data["RequestedCapacities"]
            )
        )
    if data.get("RequestedConstraints") is not None:
        import capo_outposts.types.quote_constraint_list

        out["requested_constraints"] = (
            capo_outposts.types.quote_constraint_list.deserialize_json(
                data["RequestedConstraints"]
            )
        )
    if data.get("RequestedPaymentOptions") is not None:
        import capo_outposts.types.payment_option_list

        out["requested_payment_options"] = (
            capo_outposts.types.payment_option_list.deserialize_json(
                data["RequestedPaymentOptions"]
            )
        )
    if data.get("RequestedPaymentTerms") is not None:
        import capo_outposts.types.payment_term_list

        out["requested_payment_terms"] = (
            capo_outposts.types.payment_term_list.deserialize_json(
                data["RequestedPaymentTerms"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: UpdateQuoteInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
