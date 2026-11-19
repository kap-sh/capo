"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductViewAggregationValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.approximate_count
    import capo_service_catalog.types.attribute_value


class ProductViewAggregationValue(TypedDict, closed=True):
    value: NotRequired["capo_service_catalog.types.attribute_value.AttributeValue"]
    """<p>The value of the product view aggregation.</p>"""
    approximate_count: "capo_service_catalog.types.approximate_count.ApproximateCount"
    """<p>An approximate count of the products that match the value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductViewAggregationValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    out["ApproximateCount"] = value.get("approximate_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductViewAggregationValue:
    out: ProductViewAggregationValue = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("ApproximateCount") is not None:
        out["approximate_count"] = data["ApproximateCount"]
    else:
        out["approximate_count"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProductViewAggregationValue) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    out["ApproximateCount"] = value.get("approximate_count", 0)
    return out


def deserialize_cbor(data: dict) -> ProductViewAggregationValue:
    out: ProductViewAggregationValue = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("ApproximateCount") is not None:
        out["approximate_count"] = data["ApproximateCount"]
    else:
        out["approximate_count"] = 0
    return out
