"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PreferenceUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.preference_key
    import capo_wellarchitected.types.preference_state


class PreferenceUpdate(TypedDict, closed=True):
    key: "capo_wellarchitected.types.preference_key.PreferenceKey"
    """<p>Which preference to update.</p>"""
    state: "capo_wellarchitected.types.preference_state.PreferenceState"
    """<p>State to set the preference to. FAILED is an observed state only and cannot be requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreferenceUpdate) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.preference_key

    out["key"] = capo_wellarchitected.types.preference_key.serialize_json(value["key"])
    import capo_wellarchitected.types.preference_state

    out["state"] = capo_wellarchitected.types.preference_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> PreferenceUpdate:
    out: PreferenceUpdate = {}  # type: ignore[typeddict-item]
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
    if data.get("state") is not None:
        import capo_wellarchitected.types.preference_state

        out["state"] = capo_wellarchitected.types.preference_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_wellarchitected.types.preference_state.PreferenceState", ""
        )
    return out
