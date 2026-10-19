"""Generated from Smithy shape ``com.amazonaws.amp#LimitsPerLabelSet``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.label_set
    import capo_amp.types.limits_per_label_set_entry


class LimitsPerLabelSet(TypedDict, closed=True):
    limits: "capo_amp.types.limits_per_label_set_entry.LimitsPerLabelSetEntry"
    """<p>This structure contains the information about the limits that apply to time series that match this label set.</p>"""
    label_set: "capo_amp.types.label_set.LabelSet"
    """<p>This defines one label set that will have an enforced active time series limit. </p> <p>Label values accept ASCII characters and must contain at least one character that isn't whitespace. ASCII control characters are not accepted. If the label name is metric name label <code>__<i>name</i>__</code>, then the <i>metric</i> part of the name must conform to the following pattern: <code>[a-zA-Z_:][a-zA-Z0-9_:]*</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitsPerLabelSet) -> dict:
    out: dict = {}
    import capo_amp.types.limits_per_label_set_entry

    out["limits"] = capo_amp.types.limits_per_label_set_entry.serialize_json(
        value["limits"]
    )
    import capo_amp.types.label_set

    out["labelSet"] = capo_amp.types.label_set.serialize_json(value["label_set"])
    return out


def deserialize_json(data: dict) -> LimitsPerLabelSet:
    out: LimitsPerLabelSet = {}  # type: ignore[typeddict-item]
    if data.get("limits") is not None:
        import capo_amp.types.limits_per_label_set_entry

        out["limits"] = capo_amp.types.limits_per_label_set_entry.deserialize_json(
            data["limits"]
        )
    else:
        raise DeserializationError("LimitsPerLabelSet.limits required")
    if data.get("labelSet") is not None:
        import capo_amp.types.label_set

        out["label_set"] = capo_amp.types.label_set.deserialize_json(data["labelSet"])
    else:
        out["label_set"] = {}
    return out
