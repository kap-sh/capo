"""Generated from Smithy shape ``com.amazonaws.outposts#CreateQuoteInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_outposts.types.country_code
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.payment_option_list
    import capo_outposts.types.payment_term_list
    import capo_outposts.types.quote_capacity_list
    import capo_outposts.types.quote_constraint_list
    import capo_outposts.types.quote_description


class CreateQuoteInput(TypedDict, closed=True):
    outpost_identifier: NotRequired[
        "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    ]
    """<p>The ID or ARN of the Outpost to associate with the quote. If not specified, the quote is created without an Outpost association.</p>"""
    country_code: "capo_outposts.types.country_code.CountryCode"
    """<p>The country code for the Outpost site location.</p>"""
    requested_capacities: "capo_outposts.types.quote_capacity_list.QuoteCapacityList"
    """<p>The capacity requirements for the quote. Each entry specifies a capacity type (such as Amazon EC2), the unit, and the quantity. For Amazon EC2, the quantity is the number of additional instances to add to the Outpost. For Amazon EBS and Amazon S3, the quantity is the total desired end-state capacity of the Outpost.</p>"""
    requested_constraints: NotRequired[
        "capo_outposts.types.quote_constraint_list.QuoteConstraintList"
    ]
    """<p>The physical constraints for the quote, such as maximum number of racks, maximum power draw per rack, or maximum weight per rack.</p>"""
    requested_payment_options: NotRequired[
        "capo_outposts.types.payment_option_list.PaymentOptionList"
    ]
    """<p>The payment options to include in the quote pricing. If not specified, all available payment options are returned.</p>"""
    requested_payment_terms: NotRequired[
        "capo_outposts.types.payment_term_list.PaymentTermList"
    ]
    """<p>The payment terms to include in the quote pricing. If not specified, all available payment terms are returned.</p>"""
    description: NotRequired["capo_outposts.types.quote_description.QuoteDescription"]
    """<p>A description for the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuoteInput) -> dict:
    out: dict = {}
    if "outpost_identifier" in value:
        out["OutpostIdentifier"] = value["outpost_identifier"]
    out["CountryCode"] = value["country_code"]
    import capo_outposts.types.quote_capacity_list

    out["RequestedCapacities"] = capo_outposts.types.quote_capacity_list.serialize_json(
        value["requested_capacities"]
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


def deserialize_json(data: dict) -> CreateQuoteInput:
    out: CreateQuoteInput = {}  # type: ignore[typeddict-item]
    if data.get("OutpostIdentifier") is not None:
        out["outpost_identifier"] = data["OutpostIdentifier"]
    if data.get("CountryCode") is not None:
        out["country_code"] = data["CountryCode"]
    else:
        raise DeserializationError("CreateQuoteInput.country_code required")
    if data.get("RequestedCapacities") is not None:
        import capo_outposts.types.quote_capacity_list

        out["requested_capacities"] = (
            capo_outposts.types.quote_capacity_list.deserialize_json(
                data["RequestedCapacities"]
            )
        )
    else:
        raise DeserializationError("CreateQuoteInput.requested_capacities required")
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


def redact_sensitive(value: CreateQuoteInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
