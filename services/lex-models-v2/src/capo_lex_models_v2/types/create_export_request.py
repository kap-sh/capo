"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CreateExportRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.export_resource_specification
    import capo_lex_models_v2.types.import_export_file_format
    import capo_lex_models_v2.types.import_export_file_password


class CreateExportRequest(TypedDict, closed=True):
    resource_specification: "capo_lex_models_v2.types.export_resource_specification.ExportResourceSpecification"
    """<p>Specifies the type of resource to export, either a bot or a bot locale. You can only specify one type of resource to export.</p>"""
    file_format: (
        "capo_lex_models_v2.types.import_export_file_format.ImportExportFileFormat"
    )
    """<p>The file format of the bot or bot locale definition files.</p>"""
    file_password: NotRequired[
        "capo_lex_models_v2.types.import_export_file_password.ImportExportFilePassword"
    ]
    """<p>An password to use to encrypt the exported archive. Using a password is optional, but you should encrypt the archive to protect the data in transit between Amazon Lex and your local computer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExportRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.export_resource_specification

    out["resourceSpecification"] = (
        capo_lex_models_v2.types.export_resource_specification.serialize_json(
            value["resource_specification"]
        )
    )
    import capo_lex_models_v2.types.import_export_file_format

    out["fileFormat"] = (
        capo_lex_models_v2.types.import_export_file_format.serialize_json(
            value["file_format"]
        )
    )
    if "file_password" in value:
        out["filePassword"] = value["file_password"]
    return out


def deserialize_json(data: dict) -> CreateExportRequest:
    out: CreateExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceSpecification") is not None:
        import capo_lex_models_v2.types.export_resource_specification

        out["resource_specification"] = (
            capo_lex_models_v2.types.export_resource_specification.deserialize_json(
                data["resourceSpecification"]
            )
        )
    else:
        raise DeserializationError(
            "CreateExportRequest.resource_specification required"
        )
    if data.get("fileFormat") is not None:
        import capo_lex_models_v2.types.import_export_file_format

        out["file_format"] = (
            capo_lex_models_v2.types.import_export_file_format.deserialize_json(
                data["fileFormat"]
            )
        )
    else:
        import typing

        out["file_format"] = typing.cast(
            "capo_lex_models_v2.types.import_export_file_format.ImportExportFileFormat",
            "",
        )
    if data.get("filePassword") is not None:
        out["file_password"] = data["filePassword"]
    return out


def redact_sensitive(value: CreateExportRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "file_password" in value:
        out["file_password"] = "*** Sensitive Data Redacted ***"
    return out
