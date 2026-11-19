"""Generated from Smithy shape ``com.amazonaws.guardduty#RuntimeSignals``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_text
    import capo_guardduty.types.signal_groups


class RuntimeSignals(TypedDict, closed=True):
    signal_groups: NotRequired["capo_guardduty.types.signal_groups.SignalGroups"]
    """<p>The runtime signals, grouped by finding type.</p>"""
    key_observation: NotRequired[
        "capo_guardduty.types.investigation_text.InvestigationText"
    ]
    """<p>A key observation about the runtime signals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSignals) -> dict:
    out: dict = {}
    if "signal_groups" in value:
        import capo_guardduty.types.signal_groups

        out["signalGroups"] = capo_guardduty.types.signal_groups.serialize_json(
            value["signal_groups"]
        )
    if "key_observation" in value:
        out["keyObservation"] = value["key_observation"]
    return out


def deserialize_json(data: dict) -> RuntimeSignals:
    out: RuntimeSignals = {}  # type: ignore[typeddict-item]
    if data.get("signalGroups") is not None:
        import capo_guardduty.types.signal_groups

        out["signal_groups"] = capo_guardduty.types.signal_groups.deserialize_json(
            data["signalGroups"]
        )
    if data.get("keyObservation") is not None:
        out["key_observation"] = data["keyObservation"]
    return out
