"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ListServiceLevelObjectiveExclusionWindowsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.exclusion_windows
    import capo_application_signals.types.next_token


class ListServiceLevelObjectiveExclusionWindowsOutput(TypedDict, closed=True):
    exclusion_windows: (
        "capo_application_signals.types.exclusion_windows.ExclusionWindows"
    )
    """<p>A list of exclusion windows configured for the SLO.</p>"""
    next_token: NotRequired["capo_application_signals.types.next_token.NextToken"]
    """<p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceLevelObjectiveExclusionWindowsOutput) -> dict:
    out: dict = {}
    import capo_application_signals.types.exclusion_windows

    out["ExclusionWindows"] = (
        capo_application_signals.types.exclusion_windows.serialize_json(
            value["exclusion_windows"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceLevelObjectiveExclusionWindowsOutput:
    out: ListServiceLevelObjectiveExclusionWindowsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ExclusionWindows") is not None:
        import capo_application_signals.types.exclusion_windows

        out["exclusion_windows"] = (
            capo_application_signals.types.exclusion_windows.deserialize_json(
                data["ExclusionWindows"]
            )
        )
    else:
        out["exclusion_windows"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
