"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ScalarProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.profile_identifier


class ScalarProfileRequest(TypedDict, closed=True):
    profile_id: "capo_rolesanywhere.types.profile_identifier.ProfileIdentifier"
    """<p>The profile to act on. You can specify one of the following:</p> <ul> <li> <p>The profile ID.</p> </li> <li> <p>The profile ARN.</p> </li> <li> <p>The alias ARN of the profile.</p> </li> </ul> <p>An ARN must be for a profile in your account and Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScalarProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ScalarProfileRequest:
    out: ScalarProfileRequest = {}  # type: ignore[typeddict-item]
    return out
