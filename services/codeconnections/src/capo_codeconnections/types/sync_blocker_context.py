"""Generated from Smithy shape ``com.amazonaws.codeconnections#SyncBlockerContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeconnections.types.sync_blocker_context_key
    import capo_codeconnections.types.sync_blocker_context_value


class SyncBlockerContext(TypedDict, closed=True):
    key: "capo_codeconnections.types.sync_blocker_context_key.SyncBlockerContextKey"
    """<p>The key provided for a context key-value pair for a specific sync blocker.</p>"""
    value: (
        "capo_codeconnections.types.sync_blocker_context_value.SyncBlockerContextValue"
    )
    """<p>The value provided for a context key-value pair for a specific sync blocker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerContext) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlockerContext:
    out: SyncBlockerContext = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
