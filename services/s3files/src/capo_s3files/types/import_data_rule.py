"""Generated from Smithy shape ``com.amazonaws.s3files#ImportDataRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.import_trigger


class ImportDataRule(TypedDict, closed=True):
    prefix: "str"
    """<p>The S3 key prefix that scopes this import rule. Only objects with keys beginning with this prefix are subject to the rule.</p>"""
    trigger: "capo_s3files.types.import_trigger.ImportTrigger"
    """<p>The event that triggers data import. Valid values are <code>ON_DIRECTORY_FIRST_ACCESS</code> (import when a directory is first accessed) and <code>ON_FILE_ACCESS</code> (import when a file is accessed).</p>"""
    size_less_than: "int"
    """<p>The upper size limit in bytes for this import rule. Only objects with a size strictly less than this value will have data imported into the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDataRule) -> dict:
    out: dict = {}
    out["prefix"] = value["prefix"]
    import capo_s3files.types.import_trigger

    out["trigger"] = capo_s3files.types.import_trigger.serialize_json(value["trigger"])
    out["sizeLessThan"] = value["size_less_than"]
    return out


def deserialize_json(data: dict) -> ImportDataRule:
    out: ImportDataRule = {}  # type: ignore[typeddict-item]
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    if data.get("trigger") is not None:
        import capo_s3files.types.import_trigger

        out["trigger"] = capo_s3files.types.import_trigger.deserialize_json(
            data["trigger"]
        )
    else:
        import typing

        out["trigger"] = typing.cast(
            "capo_s3files.types.import_trigger.ImportTrigger", ""
        )
    if data.get("sizeLessThan") is not None:
        out["size_less_than"] = data["sizeLessThan"]
    else:
        out["size_less_than"] = 0
    return out
