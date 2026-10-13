"""Generated from Smithy shape ``com.amazonaws.outposts#QuoteSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.account_id
    import capo_outposts.types.country_code
    import capo_outposts.types.iso8601_timestamp
    import capo_outposts.types.order_identifier
    import capo_outposts.types.outpost_arn
    import capo_outposts.types.payment_option_list
    import capo_outposts.types.payment_term_list
    import capo_outposts.types.quote_capacity_list
    import capo_outposts.types.quote_constraint_list
    import capo_outposts.types.quote_description
    import capo_outposts.types.quote_id
    import capo_outposts.types.quote_option_list
    import capo_outposts.types.quote_status
    import capo_outposts.types.status_message


class QuoteSummary(TypedDict, closed=True):
    quote_id: NotRequired["capo_outposts.types.quote_id.QuoteId"]
    """<p>The ID of the quote.</p>"""
    account_id: NotRequired["capo_outposts.types.account_id.AccountId"]
    """<p>The ID of the account that owns the quote.</p>"""
    quote_status: NotRequired["capo_outposts.types.quote_status.QuoteStatus"]
    """<p>The status of the quote.</p>"""
    status_message: NotRequired["capo_outposts.types.status_message.StatusMessage"]
    """<p>A message about the status of the quote.</p>"""
    outpost_arn: NotRequired["capo_outposts.types.outpost_arn.OutpostArn"]
    """<p>The ARN of the Outpost associated with the quote.</p>"""
    country_code: NotRequired["capo_outposts.types.country_code.CountryCode"]
    """<p>The country code for the Outpost site location.</p>"""
    requested_capacities: NotRequired[
        "capo_outposts.types.quote_capacity_list.QuoteCapacityList"
    ]
    """<p>The capacity requirements specified in the quote request.</p>"""
    requested_constraints: NotRequired[
        "capo_outposts.types.quote_constraint_list.QuoteConstraintList"
    ]
    """<p>The physical constraints specified in the quote request.</p>"""
    requested_payment_options: NotRequired[
        "capo_outposts.types.payment_option_list.PaymentOptionList"
    ]
    """<p>The payment options specified in the quote request.</p>"""
    requested_payment_terms: NotRequired[
        "capo_outposts.types.payment_term_list.PaymentTermList"
    ]
    """<p>The payment terms specified in the quote request.</p>"""
    quote_options: NotRequired["capo_outposts.types.quote_option_list.QuoteOptionList"]
    """<p>The configuration and pricing options for the quote.</p>"""
    submitted_order_id: NotRequired[
        "capo_outposts.types.order_identifier.OrderIdentifier"
    ]
    """<p>The ID of the order submitted for the quote.</p>"""
    created_date: NotRequired["capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"]
    """<p>The date the quote was created.</p>"""
    expiration_date: NotRequired[
        "capo_outposts.types.iso8601_timestamp.ISO8601Timestamp"
    ]
    """<p>The date the quote expires.</p>"""
    description: NotRequired["capo_outposts.types.quote_description.QuoteDescription"]
    """<p>The description of the quote.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuoteSummary) -> dict:
    out: dict = {}
    if "quote_id" in value:
        out["QuoteId"] = value["quote_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "quote_status" in value:
        import capo_outposts.types.quote_status

        out["QuoteStatus"] = capo_outposts.types.quote_status.serialize_json(
            value["quote_status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
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
    if "quote_options" in value:
        import capo_outposts.types.quote_option_list

        out["QuoteOptions"] = capo_outposts.types.quote_option_list.serialize_json(
            value["quote_options"]
        )
    if "submitted_order_id" in value:
        out["SubmittedOrderId"] = value["submitted_order_id"]
    if "created_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["CreatedDate"] = capo_outposts.types.iso8601_timestamp.serialize_json(
            value["created_date"]
        )
    if "expiration_date" in value:
        import capo_outposts.types.iso8601_timestamp

        out["ExpirationDate"] = capo_outposts.types.iso8601_timestamp.serialize_json(
            value["expiration_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> QuoteSummary:
    out: QuoteSummary = {}  # type: ignore[typeddict-item]
    if data.get("QuoteId") is not None:
        out["quote_id"] = data["QuoteId"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("QuoteStatus") is not None:
        import capo_outposts.types.quote_status

        out["quote_status"] = capo_outposts.types.quote_status.deserialize_json(
            data["QuoteStatus"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("OutpostArn") is not None:
        out["outpost_arn"] = data["OutpostArn"]
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
    if data.get("QuoteOptions") is not None:
        import capo_outposts.types.quote_option_list

        out["quote_options"] = capo_outposts.types.quote_option_list.deserialize_json(
            data["QuoteOptions"]
        )
    if data.get("SubmittedOrderId") is not None:
        out["submitted_order_id"] = data["SubmittedOrderId"]
    if data.get("CreatedDate") is not None:
        import capo_outposts.types.iso8601_timestamp

        out["created_date"] = capo_outposts.types.iso8601_timestamp.deserialize_json(
            data["CreatedDate"]
        )
    if data.get("ExpirationDate") is not None:
        import capo_outposts.types.iso8601_timestamp

        out["expiration_date"] = capo_outposts.types.iso8601_timestamp.deserialize_json(
            data["ExpirationDate"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: QuoteSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
