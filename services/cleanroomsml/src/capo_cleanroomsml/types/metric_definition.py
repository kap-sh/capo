"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MetricDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.metric_name
    import capo_cleanroomsml.types.metric_regex


class MetricDefinition(TypedDict, closed=True):
    name: "capo_cleanroomsml.types.metric_name.MetricName"
    """<p>The name of the model metric.</p>"""
    regex: "capo_cleanroomsml.types.metric_regex.MetricRegex"
    """<p>The regular expression statement that defines how the model metric is reported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["regex"] = value["regex"]
    return out


def deserialize_json(data: dict) -> MetricDefinition:
    out: MetricDefinition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("regex") is not None:
        out["regex"] = data["regex"]
    else:
        out["regex"] = ""
    return out
