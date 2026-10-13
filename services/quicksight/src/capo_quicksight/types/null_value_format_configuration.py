"""Generated from Smithy shape ``com.amazonaws.quicksight#NullValueFormatConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.null_string


class NullValueFormatConfiguration(TypedDict, closed=True):
    null_string: "capo_quicksight.types.null_string.NullString"
    """<p>Determines the null string of null values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NullValueFormatConfiguration) -> dict:
    out: dict = {}
    out["NullString"] = value["null_string"]
    return out


def deserialize_json(data: dict) -> NullValueFormatConfiguration:
    out: NullValueFormatConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("NullString") is not None:
        out["null_string"] = data["NullString"]
    else:
        raise DeserializationError("NullValueFormatConfiguration.null_string required")
    return out


def redact_sensitive(value: NullValueFormatConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "null_string" in value:
        out["null_string"] = "*** Sensitive Data Redacted ***"
    return out
