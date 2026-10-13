"""Generated from Smithy shape ``com.amazonaws.quicksight#StartDashboardSnapshotJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.snapshot_configuration
    import capo_quicksight.types.snapshot_user_configuration


class StartDashboardSnapshotJobRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that the dashboard snapshot job is executed in.</p>"""
    dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the dashboard that you want to start a snapshot job for. </p>"""
    snapshot_job_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An ID for the dashboard snapshot job. This ID is unique to the dashboard while the job is running. This ID can be used to poll the status of a job with a <code>DescribeDashboardSnapshotJob</code> while the job runs. You can reuse this ID for another job 24 hours after the current job is completed.</p>"""
    user_configuration: NotRequired[
        "capo_quicksight.types.snapshot_user_configuration.SnapshotUserConfiguration"
    ]
    """<p>A structure that contains information about the users that the dashboard snapshot is generated for. The users can be either anonymous users or registered users. Anonymous users cannot be used together with registered users.</p> <important> <p>When using identity-enhanced session credentials, set the UserConfiguration request attribute to null. Otherwise, the request will be invalid.</p> </important>"""
    snapshot_configuration: (
        "capo_quicksight.types.snapshot_configuration.SnapshotConfiguration"
    )
    """<p>A structure that describes the configuration of the dashboard snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDashboardSnapshotJobRequest) -> dict:
    out: dict = {}
    out["SnapshotJobId"] = value["snapshot_job_id"]
    if "user_configuration" in value:
        import capo_quicksight.types.snapshot_user_configuration

        out["UserConfiguration"] = (
            capo_quicksight.types.snapshot_user_configuration.serialize_json(
                value["user_configuration"]
            )
        )
    import capo_quicksight.types.snapshot_configuration

    out["SnapshotConfiguration"] = (
        capo_quicksight.types.snapshot_configuration.serialize_json(
            value["snapshot_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartDashboardSnapshotJobRequest:
    out: StartDashboardSnapshotJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("SnapshotJobId") is not None:
        out["snapshot_job_id"] = data["SnapshotJobId"]
    else:
        raise DeserializationError(
            "StartDashboardSnapshotJobRequest.snapshot_job_id required"
        )
    if data.get("UserConfiguration") is not None:
        import capo_quicksight.types.snapshot_user_configuration

        out["user_configuration"] = (
            capo_quicksight.types.snapshot_user_configuration.deserialize_json(
                data["UserConfiguration"]
            )
        )
    if data.get("SnapshotConfiguration") is not None:
        import capo_quicksight.types.snapshot_configuration

        out["snapshot_configuration"] = (
            capo_quicksight.types.snapshot_configuration.deserialize_json(
                data["SnapshotConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartDashboardSnapshotJobRequest.snapshot_configuration required"
        )
    return out


def redact_sensitive(value: StartDashboardSnapshotJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_configuration" in value:
        import capo_quicksight.types.snapshot_user_configuration

        out["user_configuration"] = (
            capo_quicksight.types.snapshot_user_configuration.redact_sensitive(
                value["user_configuration"]
            )
        )
    if "snapshot_configuration" in value:
        import capo_quicksight.types.snapshot_configuration

        out["snapshot_configuration"] = (
            capo_quicksight.types.snapshot_configuration.redact_sensitive(
                value["snapshot_configuration"]
            )
        )
    return out
