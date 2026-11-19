"""Generated from Smithy shape ``com.amazonaws.wellarchitected#PreferenceStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The observed state of a preference. Because enabling and disabling are performed synchronously by <code>PutAgentPreferences</code>, this value is both what the caller requested and what the system achieved. <code>FAILED</code> is never an accepted input; it reflects a stored failure (for example, an onboarding-time auto-creation that failed) surfaced on a read, and is accompanied by a <code>statusMessage</code>.</p>"""
PreferenceStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PreferenceStatus) -> str:
    return value


def deserialize_json(data: str) -> PreferenceStatus:
    return cast(PreferenceStatus, data)
