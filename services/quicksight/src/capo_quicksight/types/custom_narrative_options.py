"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomNarrativeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.narrative_string


class CustomNarrativeOptions(TypedDict, closed=True):
    narrative: "capo_quicksight.types.narrative_string.NarrativeString"
    """<p>The string input of custom narrative.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomNarrativeOptions) -> dict:
    out: dict = {}
    out["Narrative"] = value["narrative"]
    return out


def deserialize_json(data: dict) -> CustomNarrativeOptions:
    out: CustomNarrativeOptions = {}  # type: ignore[typeddict-item]
    if data.get("Narrative") is not None:
        out["narrative"] = data["Narrative"]
    else:
        out["narrative"] = ""
    return out
