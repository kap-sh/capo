"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchUpdateExclusionWindowsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.exclusion_windows
    import capo_application_signals.types.service_level_objective_ids


class BatchUpdateExclusionWindowsInput(TypedDict, closed=True):
    slo_ids: "capo_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds"
    """<p>The list of SLO IDs to add or remove exclusion windows from.</p>"""
    add_exclusion_windows: NotRequired[
        "capo_application_signals.types.exclusion_windows.ExclusionWindows"
    ]
    """<p>A list of exclusion windows to add to the specified SLOs. You can add up to 10 exclusion windows per SLO.</p>"""
    remove_exclusion_windows: NotRequired[
        "capo_application_signals.types.exclusion_windows.ExclusionWindows"
    ]
    """<p>A list of exclusion windows to remove from the specified SLOs. The window configuration must match an existing exclusion window.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateExclusionWindowsInput) -> dict:
    out: dict = {}
    import capo_application_signals.types.service_level_objective_ids

    out["SloIds"] = (
        capo_application_signals.types.service_level_objective_ids.serialize_json(
            value["slo_ids"]
        )
    )
    if "add_exclusion_windows" in value:
        import capo_application_signals.types.exclusion_windows

        out["AddExclusionWindows"] = (
            capo_application_signals.types.exclusion_windows.serialize_json(
                value["add_exclusion_windows"]
            )
        )
    if "remove_exclusion_windows" in value:
        import capo_application_signals.types.exclusion_windows

        out["RemoveExclusionWindows"] = (
            capo_application_signals.types.exclusion_windows.serialize_json(
                value["remove_exclusion_windows"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateExclusionWindowsInput:
    out: BatchUpdateExclusionWindowsInput = {}  # type: ignore[typeddict-item]
    if data.get("SloIds") is not None:
        import capo_application_signals.types.service_level_objective_ids

        out["slo_ids"] = (
            capo_application_signals.types.service_level_objective_ids.deserialize_json(
                data["SloIds"]
            )
        )
    else:
        out["slo_ids"] = []
    if data.get("AddExclusionWindows") is not None:
        import capo_application_signals.types.exclusion_windows

        out["add_exclusion_windows"] = (
            capo_application_signals.types.exclusion_windows.deserialize_json(
                data["AddExclusionWindows"]
            )
        )
    if data.get("RemoveExclusionWindows") is not None:
        import capo_application_signals.types.exclusion_windows

        out["remove_exclusion_windows"] = (
            capo_application_signals.types.exclusion_windows.deserialize_json(
                data["RemoveExclusionWindows"]
            )
        )
    return out
