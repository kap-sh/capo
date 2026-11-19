"""Generated from Smithy shape ``com.amazonaws.guardduty#KeyObservations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.investigation_observations
    import capo_guardduty.types.string


class KeyObservations(TypedDict, closed=True):
    title: NotRequired["capo_guardduty.types.string.String"]
    """<p>A short title for the key observations.</p>"""
    narrative: NotRequired["capo_guardduty.types.string.String"]
    """<p>A narrative explanation of the key observations.</p>"""
    observations: NotRequired[
        "capo_guardduty.types.investigation_observations.InvestigationObservations"
    ]
    """<p>The individual key observations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyObservations) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "narrative" in value:
        out["narrative"] = value["narrative"]
    if "observations" in value:
        import capo_guardduty.types.investigation_observations

        out["observations"] = (
            capo_guardduty.types.investigation_observations.serialize_json(
                value["observations"]
            )
        )
    return out


def deserialize_json(data: dict) -> KeyObservations:
    out: KeyObservations = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("narrative") is not None:
        out["narrative"] = data["narrative"]
    if data.get("observations") is not None:
        import capo_guardduty.types.investigation_observations

        out["observations"] = (
            capo_guardduty.types.investigation_observations.deserialize_json(
                data["observations"]
            )
        )
    return out
