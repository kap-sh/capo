"""Generated from Smithy shape ``com.amazonaws.codecommit#SetFileModeEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_mode_type_enum
    import capo_codecommit.types.path


class SetFileModeEntry(TypedDict, closed=True):
    file_path: "capo_codecommit.types.path.Path"
    """<p>The full path to the file, including the name of the file.</p>"""
    file_mode: "capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    """<p>The file mode for the file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetFileModeEntry) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    import capo_codecommit.types.file_mode_type_enum

    out["fileMode"] = capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
        value["file_mode"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetFileModeEntry:
    out: SetFileModeEntry = {}  # type: ignore[typeddict-item]
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
    else:
        import typing

        out["file_mode"] = typing.cast(
            "capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum", ""
        )
    return out
