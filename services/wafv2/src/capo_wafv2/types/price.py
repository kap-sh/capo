"""Generated from Smithy shape ``com.amazonaws.wafv2#Price``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.crypto_currency
    import capo_wafv2.types.price_amount


class Price(TypedDict, closed=True):
    amount: "capo_wafv2.types.price_amount.PriceAmount"
    """<p>The price per request as a decimal string in the specified currency. Minimum: 0.001. Maximum: 999999999.999. Supports up to 3 decimal places.</p>"""
    currency: "capo_wafv2.types.crypto_currency.CryptoCurrency"
    """<p>The cryptocurrency for payment. Currently only <code>USDC</code> is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Price) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    import capo_wafv2.types.crypto_currency

    out["Currency"] = capo_wafv2.types.crypto_currency.serialize_aws_json_1_1(
        value["currency"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Price:
    out: Price = {}  # type: ignore[typeddict-item]
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    else:
        out["amount"] = ""
    if data.get("Currency") is not None:
        import capo_wafv2.types.crypto_currency

        out["currency"] = capo_wafv2.types.crypto_currency.deserialize_aws_json_1_1(
            data["Currency"]
        )
    else:
        import typing

        out["currency"] = typing.cast(
            "capo_wafv2.types.crypto_currency.CryptoCurrency", ""
        )
    return out
