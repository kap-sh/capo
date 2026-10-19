"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetSemanticDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_descriptive_text


class DataSetSemanticDescription(TypedDict, closed=True):
    text: "capo_quicksight.types.data_set_descriptive_text.DataSetDescriptiveText"
    """<p>The descriptive text for the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSemanticDescription) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_json(data: dict) -> DataSetSemanticDescription:
    out: DataSetSemanticDescription = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    return out


def redact_sensitive(value: DataSetSemanticDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
