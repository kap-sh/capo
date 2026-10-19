"""Generated from Smithy shape ``com.amazonaws.freetier#MonetaryAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_freetier.types.currency_code
    import capo_freetier.types.generic_double


class MonetaryAmount(TypedDict, closed=True):
    amount: "capo_freetier.types.generic_double.GenericDouble"
    """<p> The aggregated monetary amount of credits earned. </p>"""
    unit: "capo_freetier.types.currency_code.CurrencyCode"
    """<p> The unit that the monetary amount is given in. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonetaryAmount) -> dict:
    out: dict = {}
    out["amount"] = (
        "NaN"
        if value.get("amount", 0) != value.get("amount", 0)
        else "Infinity"
        if value.get("amount", 0) == float("inf")
        else "-Infinity"
        if value.get("amount", 0) == float("-inf")
        else value.get("amount", 0)
    )
    import capo_freetier.types.currency_code

    out["unit"] = capo_freetier.types.currency_code.serialize_aws_json_1_0(
        value["unit"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MonetaryAmount:
    out: MonetaryAmount = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        out["amount"] = float(data["amount"])
    else:
        out["amount"] = 0
    if data.get("unit") is not None:
        import capo_freetier.types.currency_code

        out["unit"] = capo_freetier.types.currency_code.deserialize_aws_json_1_0(
            data["unit"]
        )
    else:
        import typing

        out["unit"] = typing.cast("capo_freetier.types.currency_code.CurrencyCode", "")
    return out
