"""Generated from Smithy shape ``com.amazonaws.directoryservice#CancelSchemaExtensionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.schema_extension_id


class CancelSchemaExtensionRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory whose schema extension will be canceled.</p>"""
    schema_extension_id: (
        "capo_directory_service.types.schema_extension_id.SchemaExtensionId"
    )
    """<p>The identifier of the schema extension that will be canceled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelSchemaExtensionRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["SchemaExtensionId"] = value["schema_extension_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelSchemaExtensionRequest:
    out: CancelSchemaExtensionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("SchemaExtensionId") is not None:
        out["schema_extension_id"] = data["SchemaExtensionId"]
    else:
        out["schema_extension_id"] = ""
    return out
