"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.import_export_file_password
    import capo_lex_models_v2.types.import_resource_specification
    import capo_lex_models_v2.types.merge_strategy


class StartImportRequest(TypedDict, closed=True):
    import_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier for the import. It is included in the response from the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateUploadUrl.html">CreateUploadUrl</a> operation.</p>"""
    resource_specification: "capo_lex_models_v2.types.import_resource_specification.ImportResourceSpecification"
    """<p>Parameters for creating the bot, bot locale or custom vocabulary.</p>"""
    merge_strategy: "capo_lex_models_v2.types.merge_strategy.MergeStrategy"
    """<p>The strategy to use when there is a name conflict between the imported resource and an existing resource. When the merge strategy is <code>FailOnConflict</code> existing resources are not overwritten and the import fails.</p>"""
    file_password: NotRequired[
        "capo_lex_models_v2.types.import_export_file_password.ImportExportFilePassword"
    ]
    """<p>The password used to encrypt the zip archive that contains the resource definition. You should always encrypt the zip archive to protect it during transit between your site and Amazon Lex.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportRequest) -> dict:
    out: dict = {}
    out["importId"] = value["import_id"]
    import capo_lex_models_v2.types.import_resource_specification

    out["resourceSpecification"] = (
        capo_lex_models_v2.types.import_resource_specification.serialize_json(
            value["resource_specification"]
        )
    )
    import capo_lex_models_v2.types.merge_strategy

    out["mergeStrategy"] = capo_lex_models_v2.types.merge_strategy.serialize_json(
        value["merge_strategy"]
    )
    if "file_password" in value:
        out["filePassword"] = value["file_password"]
    return out


def deserialize_json(data: dict) -> StartImportRequest:
    out: StartImportRequest = {}  # type: ignore[typeddict-item]
    if data.get("importId") is not None:
        out["import_id"] = data["importId"]
    else:
        raise DeserializationError("StartImportRequest.import_id required")
    if data.get("resourceSpecification") is not None:
        import capo_lex_models_v2.types.import_resource_specification

        out["resource_specification"] = (
            capo_lex_models_v2.types.import_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    else:
        raise DeserializationError("StartImportRequest.resource_specification required")
    if data.get("mergeStrategy") is not None:
        import capo_lex_models_v2.types.merge_strategy

        out["merge_strategy"] = (
            capo_lex_models_v2.types.merge_strategy.deserialize_json(
                data["mergeStrategy"]
            )
        )
    else:
        raise DeserializationError("StartImportRequest.merge_strategy required")
    if data.get("filePassword") is not None:
        out["file_password"] = data["filePassword"]
    return out
