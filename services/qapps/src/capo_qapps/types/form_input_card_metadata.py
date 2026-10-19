"""Generated from Smithy shape ``com.amazonaws.qapps#FormInputCardMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.form_input_card_metadata_schema


class FormInputCardMetadata(TypedDict, closed=True):
    schema: (
        "capo_qapps.types.form_input_card_metadata_schema.FormInputCardMetadataSchema"
    )
    """<p>The JSON schema that defines the shape of the response data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputCardMetadata) -> dict:
    out: dict = {}
    out["schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> FormInputCardMetadata:
    out: FormInputCardMetadata = {}  # type: ignore[typeddict-item]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    else:
        out["schema"] = None
    return out
