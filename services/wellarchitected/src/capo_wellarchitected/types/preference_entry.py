"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PreferenceEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.preference_key
    import capo_wellarchitected.types.preference_status


class PreferenceEntry(TypedDict, closed=True):
    key: "capo_wellarchitected.types.preference_key.PreferenceKey"
    """<p>Which preference this entry describes.</p>"""
    status: "capo_wellarchitected.types.preference_status.PreferenceStatus"
    """<p>Current state of the preference. ENABLED and DISABLED reflect the result of the most recent successful change. FAILED reflects a stored failure surfaced on a read and is accompanied by a detail message.</p>"""
    detail: NotRequired["str"]
    """<p>A human-readable explanation present only when status is FAILED, describing what went wrong and how to recover.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreferenceEntry) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.preference_key

    out["key"] = capo_wellarchitected.types.preference_key.serialize_json(value["key"])
    import capo_wellarchitected.types.preference_status

    out["status"] = capo_wellarchitected.types.preference_status.serialize_json(
        value["status"]
    )
    if "detail" in value:
        out["detail"] = value["detail"]
    return out


def deserialize_json(data: dict) -> PreferenceEntry:
    out: PreferenceEntry = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_wellarchitected.types.preference_key

        out["key"] = capo_wellarchitected.types.preference_key.deserialize_json(
            data["key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_wellarchitected.types.preference_key.PreferenceKey", ""
        )
    if data.get("status") is not None:
        import capo_wellarchitected.types.preference_status

        out["status"] = capo_wellarchitected.types.preference_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_wellarchitected.types.preference_status.PreferenceStatus", ""
        )
    if data.get("detail") is not None:
        out["detail"] = data["detail"]
    return out
