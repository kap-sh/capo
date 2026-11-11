"""Generated from Smithy shape ``com.amazonaws.wafv2#ConnectedAccountPrice``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.connected_account_price_amount
    import capo_wafv2.types.crypto_currency


class ConnectedAccountPrice(TypedDict, closed=True):
    amount: (
        "capo_wafv2.types.connected_account_price_amount.ConnectedAccountPriceAmount"
    )
    """<p>The price per request as a decimal string in the specified currency. Valid values range from 0.01 to 999999.99 USDC, with up to two decimal places. Sub-cent amounts are not supported.</p>"""
    currency: "capo_wafv2.types.crypto_currency.CryptoCurrency"
    """<p>The cryptocurrency for payment. Currently only <code>USDC</code> is supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedAccountPrice) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    import capo_wafv2.types.crypto_currency

    out["Currency"] = capo_wafv2.types.crypto_currency.serialize_aws_json_1_1(
        value["currency"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectedAccountPrice:
    out: ConnectedAccountPrice = {}  # type: ignore[typeddict-item]
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
