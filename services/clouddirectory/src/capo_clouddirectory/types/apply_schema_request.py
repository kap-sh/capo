"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ApplySchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.arn


class ApplySchemaRequest(TypedDict, closed=True):
    published_schema_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>Published schema Amazon Resource Name (ARN) that needs to be copied. For more information, see <a>arns</a>.</p>"""
    directory_arn: "capo_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a> into which the schema is copied. For more information, see <a>arns</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplySchemaRequest) -> dict:
    out: dict = {}
    out["PublishedSchemaArn"] = value["published_schema_arn"]
    return out


def deserialize_json(data: dict) -> ApplySchemaRequest:
    out: ApplySchemaRequest = {}  # type: ignore[typeddict-item]
    if data.get("PublishedSchemaArn") is not None:
        out["published_schema_arn"] = data["PublishedSchemaArn"]
    else:
        out["published_schema_arn"] = ""
    return out
