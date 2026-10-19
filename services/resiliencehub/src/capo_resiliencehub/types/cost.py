"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Cost``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.cost_frequency
    import capo_resiliencehub.types.currency_code
    import capo_resiliencehub.types.double


class Cost(TypedDict, closed=True):
    amount: "capo_resiliencehub.types.double.Double"
    """<p>The cost amount.</p>"""
    currency: "capo_resiliencehub.types.currency_code.CurrencyCode"
    """<p>The cost currency, for example <code>USD</code>.</p>"""
    frequency: "capo_resiliencehub.types.cost_frequency.CostFrequency"
    """<p>The cost frequency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cost) -> dict:
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
    out["currency"] = value["currency"]
    import capo_resiliencehub.types.cost_frequency

    out["frequency"] = capo_resiliencehub.types.cost_frequency.serialize_json(
        value["frequency"]
    )
    return out


def deserialize_json(data: dict) -> Cost:
    out: Cost = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        out["amount"] = float(data["amount"])
    else:
        out["amount"] = 0
    if data.get("currency") is not None:
        out["currency"] = data["currency"]
    else:
        out["currency"] = ""
    if data.get("frequency") is not None:
        import capo_resiliencehub.types.cost_frequency

        out["frequency"] = capo_resiliencehub.types.cost_frequency.deserialize_json(
            data["frequency"]
        )
    else:
        import typing

        out["frequency"] = typing.cast(
            "capo_resiliencehub.types.cost_frequency.CostFrequency", ""
        )
    return out
