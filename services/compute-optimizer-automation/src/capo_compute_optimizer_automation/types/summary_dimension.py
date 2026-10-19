"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#SummaryDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.summary_dimension_key


class SummaryDimension(TypedDict, closed=True):
    key: "capo_compute_optimizer_automation.types.summary_dimension_key.SummaryDimensionKey"
    """<p>The dimension key used for categorizing summary data.</p>"""
    value: "str"
    """<p>The specific value for this dimension key used in the summary grouping.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryDimension) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SummaryDimension:
    out: SummaryDimension = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
