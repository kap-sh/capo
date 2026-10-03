"""Generated from Smithy shape ``com.amazonaws.backup#RestoreTestingRecoveryPointSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.integer
    import capo_backup.types.restore_testing_recovery_point_selection_algorithm
    import capo_backup.types.restore_testing_recovery_point_type_list
    import capo_backup.types.string_list


class RestoreTestingRecoveryPointSelection(TypedDict, closed=True):
    algorithm: NotRequired[
        "capo_backup.types.restore_testing_recovery_point_selection_algorithm.RestoreTestingRecoveryPointSelectionAlgorithm"
    ]
    """<p>Acceptable values include "LATEST_WITHIN_WINDOW" or "RANDOM_WITHIN_WINDOW"</p>"""
    exclude_vaults: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>Accepted values include specific ARNs or list of selectors. Defaults to empty list if not listed.</p>"""
    include_vaults: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>Accepted values include wildcard ["*"] or by specific ARNs or ARN wilcard replacement ["arn:aws:backup:us-west-2:123456789012:backup-vault:asdf", ...] ["arn:aws:backup:*:*:backup-vault:asdf-*", ...]</p>"""
    recovery_point_types: NotRequired[
        "capo_backup.types.restore_testing_recovery_point_type_list.RestoreTestingRecoveryPointTypeList"
    ]
    """<p>These are the types of recovery points.</p> <p>Include <code>SNAPSHOT</code> to restore only snapshot recovery points; include <code>CONTINUOUS</code> to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for <code>Algorithm</code>.</p>"""
    selection_window_days: "capo_backup.types.integer.integer"
    """<p>Accepted values are integers from 1 to 365. If not included, the value defaults to 30. The selection window is calculated from the actual job execution time, not the plan's scheduled start time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreTestingRecoveryPointSelection) -> dict:
    out: dict = {}
    if "algorithm" in value:
        import capo_backup.types.restore_testing_recovery_point_selection_algorithm

        out["Algorithm"] = (
            capo_backup.types.restore_testing_recovery_point_selection_algorithm.serialize_json(
                value["algorithm"]
            )
        )
    if "exclude_vaults" in value:
        import capo_backup.types.string_list

        out["ExcludeVaults"] = capo_backup.types.string_list.serialize_json(
            value["exclude_vaults"]
        )
    if "include_vaults" in value:
        import capo_backup.types.string_list

        out["IncludeVaults"] = capo_backup.types.string_list.serialize_json(
            value["include_vaults"]
        )
    if "recovery_point_types" in value:
        import capo_backup.types.restore_testing_recovery_point_type_list

        out["RecoveryPointTypes"] = (
            capo_backup.types.restore_testing_recovery_point_type_list.serialize_json(
                value["recovery_point_types"]
            )
        )
    out["SelectionWindowDays"] = value.get("selection_window_days", 0)
    return out


def deserialize_json(data: dict) -> RestoreTestingRecoveryPointSelection:
    out: RestoreTestingRecoveryPointSelection = {}  # type: ignore[typeddict-item]
    if data.get("Algorithm") is not None:
        import capo_backup.types.restore_testing_recovery_point_selection_algorithm

        out["algorithm"] = (
            capo_backup.types.restore_testing_recovery_point_selection_algorithm.deserialize_json(
                data["Algorithm"]
            )
        )
    if data.get("ExcludeVaults") is not None:
        import capo_backup.types.string_list

        out["exclude_vaults"] = capo_backup.types.string_list.deserialize_json(
            data["ExcludeVaults"]
        )
    if data.get("IncludeVaults") is not None:
        import capo_backup.types.string_list

        out["include_vaults"] = capo_backup.types.string_list.deserialize_json(
            data["IncludeVaults"]
        )
    if data.get("RecoveryPointTypes") is not None:
        import capo_backup.types.restore_testing_recovery_point_type_list

        out["recovery_point_types"] = (
            capo_backup.types.restore_testing_recovery_point_type_list.deserialize_json(
                data["RecoveryPointTypes"]
            )
        )
    if data.get("SelectionWindowDays") is not None:
        out["selection_window_days"] = data["SelectionWindowDays"]
    else:
        out["selection_window_days"] = 0
    return out
