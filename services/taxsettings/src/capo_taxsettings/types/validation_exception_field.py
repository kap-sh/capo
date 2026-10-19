"""Generated from Smithy shape ``com.amazonaws.taxsettings#ValidationExceptionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.field_name


class ValidationExceptionField(TypedDict, closed=True):
    name: "capo_taxsettings.types.field_name.FieldName"
    """<p>The name of the parameter that caused a <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ValidationExceptionField:
    out: ValidationExceptionField = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
