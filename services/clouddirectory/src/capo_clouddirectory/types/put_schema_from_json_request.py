"""Generated from Smithy shape ``com.amazonaws.clouddirectory#PutSchemaFromJsonRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn
    import capo_clouddirectory.types.schema_json_document


class PutSchemaFromJsonRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the schema to update.</p>"""
    document: "capo_clouddirectory.types.schema_json_document.SchemaJsonDocument"
    """<p>The replacement JSON schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSchemaFromJsonRequest) -> dict:
    out: dict = {}
    out["Document"] = value["document"]
    return out


def deserialize_json(data: dict) -> PutSchemaFromJsonRequest:
    out: PutSchemaFromJsonRequest = {}  # type: ignore[typeddict-item]
    if data.get("Document") is not None:
        out["document"] = data["Document"]
    else:
        out["document"] = ""
    return out
