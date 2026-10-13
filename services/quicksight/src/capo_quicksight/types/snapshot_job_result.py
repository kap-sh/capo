"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.anonymous_user_snapshot_job_result_list
    import capo_quicksight.types.registered_user_snapshot_job_result_list


class SnapshotJobResult(TypedDict, closed=True):
    anonymous_users: NotRequired[
        "capo_quicksight.types.anonymous_user_snapshot_job_result_list.AnonymousUserSnapshotJobResultList"
    ]
    """<p> A list of <code>AnonymousUserSnapshotJobResult</code> objects that contain information on anonymous users and their user configurations. This data provided by you when you make a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    registered_users: NotRequired[
        "capo_quicksight.types.registered_user_snapshot_job_result_list.RegisteredUserSnapshotJobResultList"
    ]
    """<p>A list of <code>RegisteredUserSnapshotJobResult</code> objects that contain information about files that are requested for registered user during a <code>StartDashboardSnapshotJob</code> API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobResult) -> dict:
    out: dict = {}
    if "anonymous_users" in value:
        import capo_quicksight.types.anonymous_user_snapshot_job_result_list

        out["AnonymousUsers"] = (
            capo_quicksight.types.anonymous_user_snapshot_job_result_list.serialize_json(
                value["anonymous_users"]
            )
        )
    if "registered_users" in value:
        import capo_quicksight.types.registered_user_snapshot_job_result_list

        out["RegisteredUsers"] = (
            capo_quicksight.types.registered_user_snapshot_job_result_list.serialize_json(
                value["registered_users"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotJobResult:
    out: SnapshotJobResult = {}  # type: ignore[typeddict-item]
    if data.get("AnonymousUsers") is not None:
        import capo_quicksight.types.anonymous_user_snapshot_job_result_list

        out["anonymous_users"] = (
            capo_quicksight.types.anonymous_user_snapshot_job_result_list.deserialize_json(
                data["AnonymousUsers"]
            )
        )
    if data.get("RegisteredUsers") is not None:
        import capo_quicksight.types.registered_user_snapshot_job_result_list

        out["registered_users"] = (
            capo_quicksight.types.registered_user_snapshot_job_result_list.deserialize_json(
                data["RegisteredUsers"]
            )
        )
    return out


def redact_sensitive(value: SnapshotJobResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "anonymous_users" in value:
        import capo_quicksight.types.anonymous_user_snapshot_job_result_list

        out["anonymous_users"] = (
            capo_quicksight.types.anonymous_user_snapshot_job_result_list.redact_sensitive(
                value["anonymous_users"]
            )
        )
    if "registered_users" in value:
        import capo_quicksight.types.registered_user_snapshot_job_result_list

        out["registered_users"] = (
            capo_quicksight.types.registered_user_snapshot_job_result_list.redact_sensitive(
                value["registered_users"]
            )
        )
    return out
