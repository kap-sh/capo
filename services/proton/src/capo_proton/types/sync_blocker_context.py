"""Generated from Smithy shape ``com.amazonaws.proton#SyncBlockerContext``."""

from typing_extensions import TypedDict


class SyncBlockerContext(TypedDict, closed=True):
    key: "str"
    """<p>The key for the sync blocker context.</p>"""
    value: "str"
    """<p>The value of the sync blocker context.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerContext) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlockerContext:
    out: SyncBlockerContext = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
