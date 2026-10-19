"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteIdNamespaceOutput``."""

from typing_extensions import TypedDict


class DeleteIdNamespaceOutput(TypedDict, closed=True):
    message: "str"
    """<p>A successful operation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdNamespaceOutput) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteIdNamespaceOutput:
    out: DeleteIdNamespaceOutput = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
