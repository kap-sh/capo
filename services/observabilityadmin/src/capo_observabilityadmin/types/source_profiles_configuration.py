"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SourceProfilesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.profiles_filter_string


class SourceProfilesConfiguration(TypedDict, closed=True):
    profiles_selection_criteria: NotRequired[
        "capo_observabilityadmin.types.profiles_filter_string.ProfilesFilterString"
    ]
    """<p>The filter expression that selects which source profiles to centralize.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceProfilesConfiguration) -> dict:
    out: dict = {}
    if "profiles_selection_criteria" in value:
        out["ProfilesSelectionCriteria"] = value["profiles_selection_criteria"]
    return out


def deserialize_json(data: dict) -> SourceProfilesConfiguration:
    out: SourceProfilesConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ProfilesSelectionCriteria") is not None:
        out["profiles_selection_criteria"] = data["ProfilesSelectionCriteria"]
    return out
