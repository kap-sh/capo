"""Generated from Smithy shape ``com.amazonaws.pi#ResponseResourceMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.description
    import capo_pi.types.string


class ResponseResourceMetric(TypedDict, closed=True):
    metric: NotRequired["capo_pi.types.string.String"]
    """<p>The full name of the metric.</p>"""
    description: NotRequired["capo_pi.types.description.Description"]
    """<p>The description of the metric.</p>"""
    unit: NotRequired["capo_pi.types.string.String"]
    """<p>The unit of the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseResourceMetric) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "description" in value:
        out["Description"] = value["description"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseResourceMetric:
    out: ResponseResourceMetric = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResponseResourceMetric) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "description" in value:
        out["Description"] = value["description"]
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_cbor(data: dict) -> ResponseResourceMetric:
    out: ResponseResourceMetric = {}  # type: ignore[typeddict-item]
    if data.get("Metric") is not None:
        out["metric"] = data["Metric"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    return out
