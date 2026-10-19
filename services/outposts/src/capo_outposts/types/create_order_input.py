"""Generated from Smithy shape ``com.amazonaws.outposts#CreateOrderInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.line_item_request_list_definition
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.payment_option
    import capo_outposts.types.payment_term
    import capo_outposts.types.quote_identifier
    import capo_outposts.types.quote_option_identifier


class CreateOrderInput(TypedDict, closed=True):
    outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p> The ID or the Amazon Resource Name (ARN) of the Outpost. </p>"""
    quote_identifier: NotRequired[
        "capo_outposts.types.quote_identifier.QuoteIdentifier"
    ]
    """<p>The ID of the quote to use for the order.</p>"""
    quote_option_identifier: NotRequired[
        "capo_outposts.types.quote_option_identifier.QuoteOptionIdentifier"
    ]
    """<p>The ID of the quote option to use for the order.</p>"""
    line_items: NotRequired[
        "capo_outposts.types.line_item_request_list_definition.LineItemRequestListDefinition"
    ]
    """<p>The line items that make up the order.</p>"""
    payment_option: "capo_outposts.types.payment_option.PaymentOption"
    """<p>The payment option.</p>"""
    payment_term: NotRequired["capo_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment terms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOrderInput) -> dict:
    out: dict = {}
    out["OutpostIdentifier"] = value["outpost_identifier"]
    if "quote_identifier" in value:
        out["QuoteIdentifier"] = value["quote_identifier"]
    if "quote_option_identifier" in value:
        out["QuoteOptionIdentifier"] = value["quote_option_identifier"]
    if "line_items" in value:
        import capo_outposts.types.line_item_request_list_definition

        out["LineItems"] = (
            capo_outposts.types.line_item_request_list_definition.serialize_json(
                value["line_items"]
            )
        )
    import capo_outposts.types.payment_option

    out["PaymentOption"] = capo_outposts.types.payment_option.serialize_json(
        value["payment_option"]
    )
    if "payment_term" in value:
        import capo_outposts.types.payment_term

        out["PaymentTerm"] = capo_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    return out


def deserialize_json(data: dict) -> CreateOrderInput:
    out: CreateOrderInput = {}  # type: ignore[typeddict-item]
    if data.get("OutpostIdentifier") is not None:
        out["outpost_identifier"] = data["OutpostIdentifier"]
    else:
        out["outpost_identifier"] = ""
    if data.get("QuoteIdentifier") is not None:
        out["quote_identifier"] = data["QuoteIdentifier"]
    if data.get("QuoteOptionIdentifier") is not None:
        out["quote_option_identifier"] = data["QuoteOptionIdentifier"]
    if data.get("LineItems") is not None:
        import capo_outposts.types.line_item_request_list_definition

        out["line_items"] = (
            capo_outposts.types.line_item_request_list_definition.deserialize_json(
                data["LineItems"]
            )
        )
    if data.get("PaymentOption") is not None:
        import capo_outposts.types.payment_option

        out["payment_option"] = capo_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    else:
        import typing

        out["payment_option"] = typing.cast(
            "capo_outposts.types.payment_option.PaymentOption", ""
        )
    if data.get("PaymentTerm") is not None:
        import capo_outposts.types.payment_term

        out["payment_term"] = capo_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    return out
