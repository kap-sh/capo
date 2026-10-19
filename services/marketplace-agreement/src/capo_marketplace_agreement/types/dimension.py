"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Dimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.bounded_string
    import capo_marketplace_agreement.types.zero_value_integer


class Dimension(TypedDict, closed=True):
    dimension_key: "capo_marketplace_agreement.types.bounded_string.BoundedString"
    """<p>The name of key value of the dimension.</p>"""
    dimension_value: (
        "capo_marketplace_agreement.types.zero_value_integer.ZeroValueInteger"
    )
    """<p>The number of units of the dimension the acceptor has purchased.</p> <note> <p>For Agreements with <code>ConfigurableUpfrontPricingTerm</code>, the <code>RateCard</code> section will define the prices and dimensions defined by the seller (proposer), whereas the <code>Configuration</code> section will define the actual dimensions, prices, and units the buyer has chosen to accept.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Dimension) -> dict:
    out: dict = {}
    out["dimensionKey"] = value["dimension_key"]
    out["dimensionValue"] = value.get("dimension_value", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if data.get("dimensionKey") is not None:
        out["dimension_key"] = data["dimensionKey"]
    else:
        out["dimension_key"] = ""
    if data.get("dimensionValue") is not None:
        out["dimension_value"] = data["dimensionValue"]
    else:
        out["dimension_value"] = 0
    return out
