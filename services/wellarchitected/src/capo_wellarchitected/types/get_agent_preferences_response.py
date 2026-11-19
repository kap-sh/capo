"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentPreferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.preference_entries


class GetAgentPreferencesResponse(TypedDict, closed=True):
    preferences: "capo_wellarchitected.types.preference_entries.PreferenceEntries"
    """<p>The caller's complete set of preferences.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentPreferencesResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.preference_entries

    out["preferences"] = capo_wellarchitected.types.preference_entries.serialize_json(
        value["preferences"]
    )
    return out


def deserialize_json(data: dict) -> GetAgentPreferencesResponse:
    out: GetAgentPreferencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("preferences") is not None:
        import capo_wellarchitected.types.preference_entries

        out["preferences"] = (
            capo_wellarchitected.types.preference_entries.deserialize_json(
                data["preferences"]
            )
        )
    else:
        out["preferences"] = []
    return out
