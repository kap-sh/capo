"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ChangeProgressStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.change_progress_stage_list
    import capo_elasticsearch_service.types.cloned_blue_green_upgrade_details
    import capo_elasticsearch_service.types.config_change_status
    import capo_elasticsearch_service.types.guid
    import capo_elasticsearch_service.types.initiated_by
    import capo_elasticsearch_service.types.overall_change_status
    import capo_elasticsearch_service.types.string_list
    import capo_elasticsearch_service.types.total_number_of_stages
    import capo_elasticsearch_service.types.update_timestamp


class ChangeProgressStatusDetails(TypedDict, closed=True):
    change_id: NotRequired["capo_elasticsearch_service.types.guid.GUID"]
    """<p>The unique change identifier associated with a specific domain configuration change.</p>"""
    start_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The time at which the configuration change is made on the domain.</p>"""
    status: NotRequired[
        "capo_elasticsearch_service.types.overall_change_status.OverallChangeStatus"
    ]
    """<p>The overall status of the domain configuration change. This field can take the following values: <code>PENDING</code>, <code>PROCESSING</code>, <code>COMPLETED</code> and <code>FAILED</code></p>"""
    pending_properties: NotRequired[
        "capo_elasticsearch_service.types.string_list.StringList"
    ]
    """<p>The list of properties involved in the domain configuration change that are still in pending.</p>"""
    completed_properties: NotRequired[
        "capo_elasticsearch_service.types.string_list.StringList"
    ]
    """<p>The list of properties involved in the domain configuration change that are completed.</p>"""
    total_number_of_stages: (
        "capo_elasticsearch_service.types.total_number_of_stages.TotalNumberOfStages"
    )
    """<p>The total number of stages required for the configuration change.</p>"""
    change_progress_stages: NotRequired[
        "capo_elasticsearch_service.types.change_progress_stage_list.ChangeProgressStageList"
    ]
    """<p>The specific stages that the domain is going through to perform the configuration change.</p>"""
    config_change_status: NotRequired[
        "capo_elasticsearch_service.types.config_change_status.ConfigChangeStatus"
    ]
    """<p>The current status of the configuration change.</p>"""
    last_updated_time: NotRequired[
        "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The last time that the status of the configuration change was updated.</p>"""
    initiated_by: NotRequired[
        "capo_elasticsearch_service.types.initiated_by.InitiatedBy"
    ]
    """<p>The IAM principal who initiated the configuration change.</p>"""
    cloned_blue_green_upgrade_details: NotRequired[
        "capo_elasticsearch_service.types.cloned_blue_green_upgrade_details.ClonedBlueGreenUpgradeDetails"
    ]
    """<p>Details about a cloned blue/green upgrade, when the change is one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStatusDetails) -> dict:
    out: dict = {}
    if "change_id" in value:
        out["ChangeId"] = value["change_id"]
    if "start_time" in value:
        import capo_elasticsearch_service.types.update_timestamp

        out["StartTime"] = (
            capo_elasticsearch_service.types.update_timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "status" in value:
        import capo_elasticsearch_service.types.overall_change_status

        out["Status"] = (
            capo_elasticsearch_service.types.overall_change_status.serialize_json(
                value["status"]
            )
        )
    if "pending_properties" in value:
        import capo_elasticsearch_service.types.string_list

        out["PendingProperties"] = (
            capo_elasticsearch_service.types.string_list.serialize_json(
                value["pending_properties"]
            )
        )
    if "completed_properties" in value:
        import capo_elasticsearch_service.types.string_list

        out["CompletedProperties"] = (
            capo_elasticsearch_service.types.string_list.serialize_json(
                value["completed_properties"]
            )
        )
    out["TotalNumberOfStages"] = value.get("total_number_of_stages", 0)
    if "change_progress_stages" in value:
        import capo_elasticsearch_service.types.change_progress_stage_list

        out["ChangeProgressStages"] = (
            capo_elasticsearch_service.types.change_progress_stage_list.serialize_json(
                value["change_progress_stages"]
            )
        )
    if "config_change_status" in value:
        import capo_elasticsearch_service.types.config_change_status

        out["ConfigChangeStatus"] = (
            capo_elasticsearch_service.types.config_change_status.serialize_json(
                value["config_change_status"]
            )
        )
    if "last_updated_time" in value:
        import capo_elasticsearch_service.types.update_timestamp

        out["LastUpdatedTime"] = (
            capo_elasticsearch_service.types.update_timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    if "initiated_by" in value:
        import capo_elasticsearch_service.types.initiated_by

        out["InitiatedBy"] = (
            capo_elasticsearch_service.types.initiated_by.serialize_json(
                value["initiated_by"]
            )
        )
    if "cloned_blue_green_upgrade_details" in value:
        import capo_elasticsearch_service.types.cloned_blue_green_upgrade_details

        out["ClonedBlueGreenUpgradeDetails"] = (
            capo_elasticsearch_service.types.cloned_blue_green_upgrade_details.serialize_json(
                value["cloned_blue_green_upgrade_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChangeProgressStatusDetails:
    out: ChangeProgressStatusDetails = {}  # type: ignore[typeddict-item]
    if data.get("ChangeId") is not None:
        out["change_id"] = data["ChangeId"]
    if data.get("StartTime") is not None:
        import capo_elasticsearch_service.types.update_timestamp

        out["start_time"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if data.get("Status") is not None:
        import capo_elasticsearch_service.types.overall_change_status

        out["status"] = (
            capo_elasticsearch_service.types.overall_change_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("PendingProperties") is not None:
        import capo_elasticsearch_service.types.string_list

        out["pending_properties"] = (
            capo_elasticsearch_service.types.string_list.deserialize_json(
                data["PendingProperties"]
            )
        )
    if data.get("CompletedProperties") is not None:
        import capo_elasticsearch_service.types.string_list

        out["completed_properties"] = (
            capo_elasticsearch_service.types.string_list.deserialize_json(
                data["CompletedProperties"]
            )
        )
    if data.get("TotalNumberOfStages") is not None:
        out["total_number_of_stages"] = data["TotalNumberOfStages"]
    else:
        out["total_number_of_stages"] = 0
    if data.get("ChangeProgressStages") is not None:
        import capo_elasticsearch_service.types.change_progress_stage_list

        out["change_progress_stages"] = (
            capo_elasticsearch_service.types.change_progress_stage_list.deserialize_json(
                data["ChangeProgressStages"]
            )
        )
    if data.get("ConfigChangeStatus") is not None:
        import capo_elasticsearch_service.types.config_change_status

        out["config_change_status"] = (
            capo_elasticsearch_service.types.config_change_status.deserialize_json(
                data["ConfigChangeStatus"]
            )
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_elasticsearch_service.types.update_timestamp

        out["last_updated_time"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if data.get("InitiatedBy") is not None:
        import capo_elasticsearch_service.types.initiated_by

        out["initiated_by"] = (
            capo_elasticsearch_service.types.initiated_by.deserialize_json(
                data["InitiatedBy"]
            )
        )
    if data.get("ClonedBlueGreenUpgradeDetails") is not None:
        import capo_elasticsearch_service.types.cloned_blue_green_upgrade_details

        out["cloned_blue_green_upgrade_details"] = (
            capo_elasticsearch_service.types.cloned_blue_green_upgrade_details.deserialize_json(
                data["ClonedBlueGreenUpgradeDetails"]
            )
        )
    return out
