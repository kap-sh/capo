"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#BatchPutPropertyError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iottwinmaker.types.property_value_entry
    import capo_iottwinmaker.types.string


class BatchPutPropertyError(TypedDict, closed=True):
    error_code: "capo_iottwinmaker.types.string.String"
    """<p>The error code.</p>"""
    error_message: "capo_iottwinmaker.types.string.String"
    """<p>The error message.</p>"""
    entry: "capo_iottwinmaker.types.property_value_entry.PropertyValueEntry"
    """<p>An object that contains information about errors returned by the <code>BatchPutProperty</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutPropertyError) -> dict:
    out: dict = {}
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    import capo_iottwinmaker.types.property_value_entry

    out["entry"] = capo_iottwinmaker.types.property_value_entry.serialize_json(
        value["entry"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutPropertyError:
    out: BatchPutPropertyError = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    else:
        out["error_code"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    if data.get("entry") is not None:
        import capo_iottwinmaker.types.property_value_entry

        out["entry"] = capo_iottwinmaker.types.property_value_entry.deserialize_json(
            data["entry"]
        )
    else:
        raise DeserializationError("BatchPutPropertyError.entry required")
    return out
