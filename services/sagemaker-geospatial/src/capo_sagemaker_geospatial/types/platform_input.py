"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#PlatformInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.comparison_operator


class PlatformInput(TypedDict, closed=True):
    value: "str"
    """<p>The value of the platform.</p>"""
    comparison_operator: NotRequired[
        "capo_sagemaker_geospatial.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The ComparisonOperator to use with PlatformInput.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlatformInput) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    if "comparison_operator" in value:
        out["ComparisonOperator"] = value["comparison_operator"]
    return out


def deserialize_json(data: dict) -> PlatformInput:
    out: PlatformInput = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("ComparisonOperator") is not None:
        out["comparison_operator"] = data["ComparisonOperator"]
    return out
