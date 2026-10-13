"""Generated from Smithy shape ``com.amazonaws.datazone#AcceptChoice``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.edited_value


class AcceptChoice(TypedDict, closed=True):
    prediction_target: NotRequired["str"]
    """<p>Specifies the target (for example, a column name) where a prediction can be accepted.</p>"""
    prediction_choice: NotRequired["int"]
    """<p>Specifies the prediction (aka, the automatically generated piece of metadata) that can be accepted.</p>"""
    edited_value: NotRequired["capo_datazone.types.edited_value.EditedValue"]
    """<p>The edit of the prediction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AcceptChoice) -> dict:
    out: dict = {}
    if "prediction_target" in value:
        out["predictionTarget"] = value["prediction_target"]
    if "prediction_choice" in value:
        out["predictionChoice"] = value["prediction_choice"]
    if "edited_value" in value:
        out["editedValue"] = value["edited_value"]
    return out


def deserialize_json(data: dict) -> AcceptChoice:
    out: AcceptChoice = {}  # type: ignore[typeddict-item]
    if data.get("predictionTarget") is not None:
        out["prediction_target"] = data["predictionTarget"]
    if data.get("predictionChoice") is not None:
        out["prediction_choice"] = data["predictionChoice"]
    if data.get("editedValue") is not None:
        out["edited_value"] = data["editedValue"]
    return out


def redact_sensitive(value: AcceptChoice) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "edited_value" in value:
        out["edited_value"] = "*** Sensitive Data Redacted ***"
    return out
