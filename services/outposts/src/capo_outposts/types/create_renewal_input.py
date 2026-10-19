"""Generated from Smithy shape ``com.amazonaws.outposts#CreateRenewalInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.auto_fill_idempotency_token
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.payment_option
    import capo_outposts.types.payment_term


class CreateRenewalInput(TypedDict, closed=True):
    payment_option: "capo_outposts.types.payment_option.PaymentOption"
    """<p>The payment option.</p>"""
    payment_term: "capo_outposts.types.payment_term.PaymentTerm"
    """<p>The payment term.</p>"""
    outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost.</p>"""
    client_token: NotRequired[
        "capo_outposts.types.auto_fill_idempotency_token.AutoFillIdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRenewalInput) -> dict:
    out: dict = {}
    import capo_outposts.types.payment_option

    out["PaymentOption"] = capo_outposts.types.payment_option.serialize_json(
        value["payment_option"]
    )
    import capo_outposts.types.payment_term

    out["PaymentTerm"] = capo_outposts.types.payment_term.serialize_json(
        value["payment_term"]
    )
    out["OutpostIdentifier"] = value["outpost_identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRenewalInput:
    out: CreateRenewalInput = {}  # type: ignore[typeddict-item]
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
    else:
        import typing

        out["payment_term"] = typing.cast(
            "capo_outposts.types.payment_term.PaymentTerm", ""
        )
    if data.get("OutpostIdentifier") is not None:
        out["outpost_identifier"] = data["OutpostIdentifier"]
    else:
        out["outpost_identifier"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
