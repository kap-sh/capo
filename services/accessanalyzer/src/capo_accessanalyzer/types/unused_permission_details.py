"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedPermissionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.timestamp
    import capo_accessanalyzer.types.unused_action_list


class UnusedPermissionDetails(TypedDict, closed=True):
    actions: NotRequired[
        "capo_accessanalyzer.types.unused_action_list.UnusedActionList"
    ]
    """<p>A list of unused actions for which the unused access finding was generated.</p>"""
    service_namespace: "str"
    """<p>The namespace of the Amazon Web Services service that contains the unused actions.</p>"""
    last_accessed: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the permission was last accessed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedPermissionDetails) -> dict:
    out: dict = {}
    if "actions" in value:
        import capo_accessanalyzer.types.unused_action_list

        out["actions"] = capo_accessanalyzer.types.unused_action_list.serialize_json(
            value["actions"]
        )
    out["serviceNamespace"] = value["service_namespace"]
    if "last_accessed" in value:
        import capo_accessanalyzer.types.timestamp

        out["lastAccessed"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["last_accessed"]
        )
    return out


def deserialize_json(data: dict) -> UnusedPermissionDetails:
    out: UnusedPermissionDetails = {}  # type: ignore[typeddict-item]
    if data.get("actions") is not None:
        import capo_accessanalyzer.types.unused_action_list

        out["actions"] = capo_accessanalyzer.types.unused_action_list.deserialize_json(
            data["actions"]
        )
    if data.get("serviceNamespace") is not None:
        out["service_namespace"] = data["serviceNamespace"]
    else:
        out["service_namespace"] = ""
    if data.get("lastAccessed") is not None:
        import capo_accessanalyzer.types.timestamp

        out["last_accessed"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["lastAccessed"]
        )
    return out
