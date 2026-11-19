"""Generated from Smithy shape ``com.amazonaws.directoryservice#StartSchemaExtensionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.schema_extension_id


class StartSchemaExtensionResult(TypedDict, closed=True):
    schema_extension_id: NotRequired[
        "capo_directory_service.types.schema_extension_id.SchemaExtensionId"
    ]
    """<p>The identifier of the schema extension that will be applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSchemaExtensionResult) -> dict:
    out: dict = {}
    if "schema_extension_id" in value:
        out["SchemaExtensionId"] = value["schema_extension_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSchemaExtensionResult:
    out: StartSchemaExtensionResult = {}  # type: ignore[typeddict-item]
    if data.get("SchemaExtensionId") is not None:
        out["schema_extension_id"] = data["SchemaExtensionId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartSchemaExtensionResult) -> dict:
    out: dict = {}
    if "schema_extension_id" in value:
        out["SchemaExtensionId"] = value["schema_extension_id"]
    return out


def deserialize_cbor(data: dict) -> StartSchemaExtensionResult:
    out: StartSchemaExtensionResult = {}  # type: ignore[typeddict-item]
    if data.get("SchemaExtensionId") is not None:
        out["schema_extension_id"] = data["SchemaExtensionId"]
    return out
