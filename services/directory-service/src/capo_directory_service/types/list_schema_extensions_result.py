"""Generated from Smithy shape ``com.amazonaws.directoryservice#ListSchemaExtensionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.next_token
    import capo_directory_service.types.schema_extensions_info


class ListSchemaExtensionsResult(TypedDict, closed=True):
    schema_extensions_info: NotRequired[
        "capo_directory_service.types.schema_extensions_info.SchemaExtensionsInfo"
    ]
    """<p>Information about the schema extensions applied to the directory.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent call to <code>ListSchemaExtensions</code> to retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSchemaExtensionsResult) -> dict:
    out: dict = {}
    if "schema_extensions_info" in value:
        import capo_directory_service.types.schema_extensions_info

        out["SchemaExtensionsInfo"] = (
            capo_directory_service.types.schema_extensions_info.serialize_aws_json_1_1(
                value["schema_extensions_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSchemaExtensionsResult:
    out: ListSchemaExtensionsResult = {}  # type: ignore[typeddict-item]
    if data.get("SchemaExtensionsInfo") is not None:
        import capo_directory_service.types.schema_extensions_info

        out["schema_extensions_info"] = (
            capo_directory_service.types.schema_extensions_info.deserialize_aws_json_1_1(
                data["SchemaExtensionsInfo"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSchemaExtensionsResult) -> dict:
    out: dict = {}
    if "schema_extensions_info" in value:
        import capo_directory_service.types.schema_extensions_info

        out["SchemaExtensionsInfo"] = (
            capo_directory_service.types.schema_extensions_info.serialize_cbor(
                value["schema_extensions_info"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListSchemaExtensionsResult:
    out: ListSchemaExtensionsResult = {}  # type: ignore[typeddict-item]
    if data.get("SchemaExtensionsInfo") is not None:
        import capo_directory_service.types.schema_extensions_info

        out["schema_extensions_info"] = (
            capo_directory_service.types.schema_extensions_info.deserialize_cbor(
                data["SchemaExtensionsInfo"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
