"""Generated from Smithy shape ``com.amazonaws.networkmanager#ContextChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_change_type
    import capo_networkmanager.types.context_entry


class ContextChange(TypedDict, closed=True):
    change_type: NotRequired[
        "capo_networkmanager.types.context_change_type.ContextChangeType"
    ]
    """<p>The type of change. The possible values are the following:</p> <ul> <li> <p> <code>ADDED</code>: The context entry was added to the context store.</p> </li> <li> <p> <code>REMOVED</code>: The context entry was removed from the context store.</p> </li> </ul>"""
    context: NotRequired["capo_networkmanager.types.context_entry.ContextEntry"]
    """<p>The context entry that was added or removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextChange) -> dict:
    out: dict = {}
    if "change_type" in value:
        import capo_networkmanager.types.context_change_type

        out["ChangeType"] = (
            capo_networkmanager.types.context_change_type.serialize_json(
                value["change_type"]
            )
        )
    if "context" in value:
        import capo_networkmanager.types.context_entry

        out["Context"] = capo_networkmanager.types.context_entry.serialize_json(
            value["context"]
        )
    return out


def deserialize_json(data: dict) -> ContextChange:
    out: ContextChange = {}  # type: ignore[typeddict-item]
    if data.get("ChangeType") is not None:
        import capo_networkmanager.types.context_change_type

        out["change_type"] = (
            capo_networkmanager.types.context_change_type.deserialize_json(
                data["ChangeType"]
            )
        )
    if data.get("Context") is not None:
        import capo_networkmanager.types.context_entry

        out["context"] = capo_networkmanager.types.context_entry.deserialize_json(
            data["Context"]
        )
    return out
