"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedIamUserAccessKeyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.timestamp


class UnusedIamUserAccessKeyDetails(TypedDict, closed=True):
    access_key_id: "str"
    """<p>The ID of the access key for which the unused access finding was generated.</p>"""
    last_accessed: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the access key was last accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedIamUserAccessKeyDetails) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    if "last_accessed" in value:
        import capo_accessanalyzer.types.timestamp

        out["lastAccessed"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["last_accessed"]
        )
    return out


def deserialize_json(data: dict) -> UnusedIamUserAccessKeyDetails:
    out: UnusedIamUserAccessKeyDetails = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    else:
        out["access_key_id"] = ""
    if data.get("lastAccessed") is not None:
        import capo_accessanalyzer.types.timestamp

        out["last_accessed"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["lastAccessed"]
        )
    return out
