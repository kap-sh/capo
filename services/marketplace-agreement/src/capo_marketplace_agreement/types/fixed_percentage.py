"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#FixedPercentage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.price_increase_percentage


class FixedPercentage(TypedDict, closed=True):
    value: NotRequired[
        "capo_marketplace_agreement.types.price_increase_percentage.PriceIncreasePercentage"
    ]
    """<p>The percentage by which the price increases at each renewal, from <code>0.00</code> to <code>100.00</code> with up to two decimal places. A value of <code>0.00</code> means that the agreement renews at the same price.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FixedPercentage) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FixedPercentage:
    out: FixedPercentage = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FixedPercentage) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_cbor(data: dict) -> FixedPercentage:
    out: FixedPercentage = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
