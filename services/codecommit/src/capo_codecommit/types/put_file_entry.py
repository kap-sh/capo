"""Generated from Smithy shape ``com.amazonaws.codecommit#PutFileEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_content
    import capo_codecommit.types.file_mode_type_enum
    import capo_codecommit.types.path
    import capo_codecommit.types.source_file_specifier


class PutFileEntry(TypedDict, closed=True):
    file_path: "capo_codecommit.types.path.Path"
    """<p>The full path to the file in the repository, including the name of the file.</p>"""
    file_mode: NotRequired["capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.</p>"""
    file_content: NotRequired["capo_codecommit.types.file_content.FileContent"]
    """<p>The content of the file, if a source file is not specified.</p>"""
    source_file: NotRequired[
        "capo_codecommit.types.source_file_specifier.SourceFileSpecifier"
    ]
    """<p>The name and full path of the file that contains the changes you want to make as part of the commit, if you are not providing the file content directly.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFileEntry) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    if "file_mode" in value:
        import capo_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    if "file_content" in value:
        import capo_codecommit.types.file_content

        out["fileContent"] = capo_codecommit.types.file_content.serialize_aws_json_1_1(
            value["file_content"]
        )
    if "source_file" in value:
        import capo_codecommit.types.source_file_specifier

        out["sourceFile"] = (
            capo_codecommit.types.source_file_specifier.serialize_aws_json_1_1(
                value["source_file"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFileEntry:
    out: PutFileEntry = {}  # type: ignore[typeddict-item]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    if data.get("fileMode") is not None:
        import capo_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    if data.get("fileContent") is not None:
        import capo_codecommit.types.file_content

        out["file_content"] = (
            capo_codecommit.types.file_content.deserialize_aws_json_1_1(
                data["fileContent"]
            )
        )
    if data.get("sourceFile") is not None:
        import capo_codecommit.types.source_file_specifier

        out["source_file"] = (
            capo_codecommit.types.source_file_specifier.deserialize_aws_json_1_1(
                data["sourceFile"]
            )
        )
    return out
