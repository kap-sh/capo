"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.policy_event_metadata


class PolicyEventDetails(TypedDict, closed=True):
    title: "str"
    """<p>A short summary of the event.</p>"""
    description: "str"
    """<p>A description of the event.</p>"""
    event_metadata: NotRequired[
        "capo_resiliencehubv2.types.policy_event_metadata.PolicyEventMetadata"
    ]
    """<p>The event-specific metadata, with one member populated according to the event type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEventDetails) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["description"] = value["description"]
    if "event_metadata" in value:
        import capo_resiliencehubv2.types.policy_event_metadata

        out["eventMetadata"] = (
            capo_resiliencehubv2.types.policy_event_metadata.serialize_json(
                value["event_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> PolicyEventDetails:
    out: PolicyEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("eventMetadata") is not None:
        import capo_resiliencehubv2.types.policy_event_metadata

        out["event_metadata"] = (
            capo_resiliencehubv2.types.policy_event_metadata.deserialize_json(
                data["eventMetadata"]
            )
        )
    return out
