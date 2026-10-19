"""Generated from Smithy shape ``com.amazonaws.odb#CloneToRefreshableConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.clone_type
    import capo_odb.types.open_mode
    import capo_odb.types.refreshable_mode
    import capo_odb.types.resource_id_or_arn


class CloneToRefreshableConfiguration(TypedDict, closed=True):
    source_autonomous_database_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the source Autonomous Database to create the refreshable clone from.</p>"""
    refreshable_mode: NotRequired["capo_odb.types.refreshable_mode.RefreshableMode"]
    """<p>The refresh mode of the refreshable clone, either automatic or manual.</p>"""
    auto_refresh_frequency_in_seconds: NotRequired["int"]
    """<p>The frequency, in seconds, at which the refreshable clone is automatically refreshed.</p>"""
    auto_refresh_point_lag_in_seconds: NotRequired["int"]
    """<p>The time lag, in seconds, between the refreshable clone and its source database.</p>"""
    time_of_auto_refresh_start: NotRequired["datetime.datetime"]
    """<p>The date and time at which the automatic refresh of the refreshable clone starts.</p>"""
    open_mode: NotRequired["capo_odb.types.open_mode.OpenMode"]
    """<p>The mode in which to open the refreshable clone, either read-only or read/write.</p>"""
    clone_type: NotRequired["capo_odb.types.clone_type.CloneType"]
    """<p>The type of clone to create.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloneToRefreshableConfiguration) -> dict:
    out: dict = {}
    out["sourceAutonomousDatabaseId"] = value["source_autonomous_database_id"]
    if "refreshable_mode" in value:
        import capo_odb.types.refreshable_mode

        out["refreshableMode"] = capo_odb.types.refreshable_mode.serialize_aws_json_1_0(
            value["refreshable_mode"]
        )
    if "auto_refresh_frequency_in_seconds" in value:
        out["autoRefreshFrequencyInSeconds"] = value[
            "auto_refresh_frequency_in_seconds"
        ]
    if "auto_refresh_point_lag_in_seconds" in value:
        out["autoRefreshPointLagInSeconds"] = value["auto_refresh_point_lag_in_seconds"]
    if "time_of_auto_refresh_start" in value:
        import capo_odb._protocol.serialize

        out["timeOfAutoRefreshStart"] = capo_odb._protocol.serialize.fmt_date_time(
            value["time_of_auto_refresh_start"]
        )
    if "open_mode" in value:
        import capo_odb.types.open_mode

        out["openMode"] = capo_odb.types.open_mode.serialize_aws_json_1_0(
            value["open_mode"]
        )
    if "clone_type" in value:
        import capo_odb.types.clone_type

        out["cloneType"] = capo_odb.types.clone_type.serialize_aws_json_1_0(
            value["clone_type"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CloneToRefreshableConfiguration:
    out: CloneToRefreshableConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceAutonomousDatabaseId") is not None:
        out["source_autonomous_database_id"] = data["sourceAutonomousDatabaseId"]
    else:
        out["source_autonomous_database_id"] = ""
    if data.get("refreshableMode") is not None:
        import capo_odb.types.refreshable_mode

        out["refreshable_mode"] = (
            capo_odb.types.refreshable_mode.deserialize_aws_json_1_0(
                data["refreshableMode"]
            )
        )
    if data.get("autoRefreshFrequencyInSeconds") is not None:
        out["auto_refresh_frequency_in_seconds"] = data["autoRefreshFrequencyInSeconds"]
    if data.get("autoRefreshPointLagInSeconds") is not None:
        out["auto_refresh_point_lag_in_seconds"] = data["autoRefreshPointLagInSeconds"]
    if data.get("timeOfAutoRefreshStart") is not None:
        import datetime

        out["time_of_auto_refresh_start"] = datetime.datetime.fromisoformat(
            data["timeOfAutoRefreshStart"].replace("Z", "+00:00")
        )
    if data.get("openMode") is not None:
        import capo_odb.types.open_mode

        out["open_mode"] = capo_odb.types.open_mode.deserialize_aws_json_1_0(
            data["openMode"]
        )
    if data.get("cloneType") is not None:
        import capo_odb.types.clone_type

        out["clone_type"] = capo_odb.types.clone_type.deserialize_aws_json_1_0(
            data["cloneType"]
        )
    return out
