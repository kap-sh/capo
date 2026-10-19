"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#AddKeyEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.add_key_value
    import capo_cloudwatch_logs.types.key
    import capo_cloudwatch_logs.types.overwrite_if_exists


class AddKeyEntry(TypedDict, closed=True):
    key: "capo_cloudwatch_logs.types.key.Key"
    """<p>The key of the new entry to be added to the log event</p>"""
    value: "capo_cloudwatch_logs.types.add_key_value.AddKeyValue"
    """<p>The value of the new entry to be added to the log event</p>"""
    overwrite_if_exists: (
        "capo_cloudwatch_logs.types.overwrite_if_exists.OverwriteIfExists"
    )
    """<p>Specifies whether to overwrite the value if the key already exists in the log event. If you omit this, the default is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddKeyEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    out["overwriteIfExists"] = value.get("overwrite_if_exists", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> AddKeyEntry:
    out: AddKeyEntry = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("overwriteIfExists") is not None:
        out["overwrite_if_exists"] = data["overwriteIfExists"]
    else:
        out["overwrite_if_exists"] = False
    return out
