"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PutAgentPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.preference_updates


class PutAgentPreferencesRequest(TypedDict, closed=True):
    preferences: "capo_wellarchitected.types.preference_updates.PreferenceUpdates"
    """<p>Preference updates to apply. A given preference key may appear at most once.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAgentPreferencesRequest) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.preference_updates

    out["preferences"] = capo_wellarchitected.types.preference_updates.serialize_json(
        value["preferences"]
    )
    return out


def deserialize_json(data: dict) -> PutAgentPreferencesRequest:
    out: PutAgentPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("preferences") is not None:
        import capo_wellarchitected.types.preference_updates

        out["preferences"] = (
            capo_wellarchitected.types.preference_updates.deserialize_json(
                data["preferences"]
            )
        )
    else:
        out["preferences"] = []
    return out
