"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RenameKeyEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.key
    import capo_cloudwatch_logs.types.overwrite_if_exists
    import capo_cloudwatch_logs.types.rename_to


class RenameKeyEntry(TypedDict, closed=True):
    key: "capo_cloudwatch_logs.types.key.Key"
    """<p>The key to rename</p>"""
    rename_to: "capo_cloudwatch_logs.types.rename_to.RenameTo"
    """<p>The string to use for the new key name</p>"""
    overwrite_if_exists: (
        "capo_cloudwatch_logs.types.overwrite_if_exists.OverwriteIfExists"
    )
    """<p>Specifies whether to overwrite the existing value if the destination key already exists. The default is <code>false</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenameKeyEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["renameTo"] = value["rename_to"]
    out["overwriteIfExists"] = value.get("overwrite_if_exists", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RenameKeyEntry:
    out: RenameKeyEntry = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("renameTo") is not None:
        out["rename_to"] = data["renameTo"]
    else:
        out["rename_to"] = ""
    if data.get("overwriteIfExists") is not None:
        out["overwrite_if_exists"] = data["overwriteIfExists"]
    else:
        out["overwrite_if_exists"] = False
    return out
