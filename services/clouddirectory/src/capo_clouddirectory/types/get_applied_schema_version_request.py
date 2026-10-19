"""Generated from Smithy shape ``com.amazonaws.clouddirectory#GetAppliedSchemaVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class GetAppliedSchemaVersionRequest(TypedDict, closed=True):
    schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The ARN of the applied schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAppliedSchemaVersionRequest) -> dict:
    out: dict = {}
    out["SchemaArn"] = value["schema_arn"]
    return out


def deserialize_json(data: dict) -> GetAppliedSchemaVersionRequest:
    out: GetAppliedSchemaVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SchemaArn") is not None:
        out["schema_arn"] = data["SchemaArn"]
    else:
        out["schema_arn"] = ""
    return out
