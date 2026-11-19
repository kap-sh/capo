"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PreferenceState``."""

from typing import Literal, TypeAlias, cast

"""<note> <p>This is the writable subset of <code>PreferenceStatus</code>: you can set a preference to <code>ENABLED</code> or <code>DISABLED</code>, but you cannot set <code>FAILED</code>, which is an observed state only.</p> </note> <p>The settable state of a preference, supplied to <code>PutAgentPreferences</code>.</p>"""
PreferenceState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PreferenceState) -> str:
    return value


def deserialize_json(data: str) -> PreferenceState:
    return cast(PreferenceState, data)
