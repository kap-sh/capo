"""Generated from Smithy shape ``com.amazonaws.guardduty#Detection``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.anomaly
    import capo_guardduty.types.sequence


class Detection(TypedDict, closed=True):
    anomaly: NotRequired["capo_guardduty.types.anomaly.Anomaly"]
    """<p>The details about the anomalous activity that caused GuardDuty to generate the finding.</p>"""
    sequence: NotRequired["capo_guardduty.types.sequence.Sequence"]
    """<p>The details about the attack sequence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Detection) -> dict:
    out: dict = {}
    if "anomaly" in value:
        import capo_guardduty.types.anomaly

        out["anomaly"] = capo_guardduty.types.anomaly.serialize_json(value["anomaly"])
    if "sequence" in value:
        import capo_guardduty.types.sequence

        out["sequence"] = capo_guardduty.types.sequence.serialize_json(
            value["sequence"]
        )
    return out


def deserialize_json(data: dict) -> Detection:
    out: Detection = {}  # type: ignore[typeddict-item]
    if data.get("anomaly") is not None:
        import capo_guardduty.types.anomaly

        out["anomaly"] = capo_guardduty.types.anomaly.deserialize_json(data["anomaly"])
    if data.get("sequence") is not None:
        import capo_guardduty.types.sequence

        out["sequence"] = capo_guardduty.types.sequence.deserialize_json(
            data["sequence"]
        )
    return out


def redact_sensitive(value: Detection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sequence" in value:
        import capo_guardduty.types.sequence

        out["sequence"] = capo_guardduty.types.sequence.redact_sensitive(
            value["sequence"]
        )
    return out
