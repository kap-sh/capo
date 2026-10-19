"""Generated from Smithy shape ``com.amazonaws.codecommit#ReplaceContentEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_content
    import capo_codecommit.types.file_mode_type_enum
    import capo_codecommit.types.path
    import capo_codecommit.types.replacement_type_enum


class ReplaceContentEntry(TypedDict, closed=True):
    file_path: "capo_codecommit.types.path.Path"
    """<p>The path of the conflicting file.</p>"""
    replacement_type: "capo_codecommit.types.replacement_type_enum.ReplacementTypeEnum"
    """<p>The replacement type to use when determining how to resolve the conflict.</p>"""
    content: NotRequired["capo_codecommit.types.file_content.FileContent"]
    """<p>The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.</p>"""
    file_mode: NotRequired["capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The file mode to apply during conflict resoltion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplaceContentEntry) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    import capo_codecommit.types.replacement_type_enum

    out["replacementType"] = (
        capo_codecommit.types.replacement_type_enum.serialize_aws_json_1_1(
            value["replacement_type"]
        )
    )
    if "content" in value:
        import capo_codecommit.types.file_content

        out["content"] = capo_codecommit.types.file_content.serialize_aws_json_1_1(
            value["content"]
        )
    if "file_mode" in value:
        import capo_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplaceContentEntry:
    out: ReplaceContentEntry = {}  # type: ignore[typeddict-item]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    if data.get("replacementType") is not None:
        import capo_codecommit.types.replacement_type_enum

        out["replacement_type"] = (
            capo_codecommit.types.replacement_type_enum.deserialize_aws_json_1_1(
                data["replacementType"]
            )
        )
    else:
        import typing

        out["replacement_type"] = typing.cast(
            "capo_codecommit.types.replacement_type_enum.ReplacementTypeEnum", ""
        )
    if data.get("content") is not None:
        import capo_codecommit.types.file_content

        out["content"] = capo_codecommit.types.file_content.deserialize_aws_json_1_1(
            data["content"]
        )
    if data.get("fileMode") is not None:
        import capo_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    return out
