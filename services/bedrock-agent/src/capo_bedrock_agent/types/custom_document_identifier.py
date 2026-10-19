"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CustomDocumentIdentifier``."""

from typing_extensions import TypedDict


class CustomDocumentIdentifier(TypedDict, closed=True):
    id: "str"
    """<p>The identifier of the document to ingest into a custom data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomDocumentIdentifier) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> CustomDocumentIdentifier:
    out: CustomDocumentIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
