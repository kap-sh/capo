"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PercentageRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.price_increase_percentage


class PercentageRange(TypedDict, closed=True):
    min_value: NotRequired[
        "capo_marketplace_agreement.types.price_increase_percentage.PriceIncreasePercentage"
    ]
    """<p>The lowest percentage that the proposer can choose, from <code>0.00</code> to <code>100.00</code> with up to two decimal places.</p>"""
    max_value: NotRequired[
        "capo_marketplace_agreement.types.price_increase_percentage.PriceIncreasePercentage"
    ]
    """<p>The highest percentage that the proposer can choose, from <code>0.00</code> to <code>100.00</code> with up to two decimal places.</p>"""
    default_value: NotRequired[
        "capo_marketplace_agreement.types.price_increase_percentage.PriceIncreasePercentage"
    ]
    """<p>The percentage that is applied if the proposer doesn't choose a value before the adjustment deadline. Valid values range from <code>0.00</code> to <code>100.00</code>, with up to two decimal places.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PercentageRange) -> dict:
    out: dict = {}
    if "min_value" in value:
        out["minValue"] = value["min_value"]
    if "max_value" in value:
        out["maxValue"] = value["max_value"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PercentageRange:
    out: PercentageRange = {}  # type: ignore[typeddict-item]
    if data.get("minValue") is not None:
        out["min_value"] = data["minValue"]
    if data.get("maxValue") is not None:
        out["max_value"] = data["maxValue"]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PercentageRange) -> dict:
    out: dict = {}
    if "min_value" in value:
        out["minValue"] = value["min_value"]
    if "max_value" in value:
        out["maxValue"] = value["max_value"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_cbor(data: dict) -> PercentageRange:
    out: PercentageRange = {}  # type: ignore[typeddict-item]
    if data.get("minValue") is not None:
        out["min_value"] = data["minValue"]
    if data.get("maxValue") is not None:
        out["max_value"] = data["maxValue"]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    return out
