"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteSchemaMappingOutput``."""

from typing_extensions import TypedDict


class DeleteSchemaMappingOutput(TypedDict, closed=True):
    message: "str"
    """<p>A successful operation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaMappingOutput) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteSchemaMappingOutput:
    out: DeleteSchemaMappingOutput = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
