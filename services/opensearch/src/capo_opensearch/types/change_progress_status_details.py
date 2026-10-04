"""Generated from Smithy shape ``com.amazonaws.opensearch#ChangeProgressStatusDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.accepted_warnings_list
    import capo_opensearch.types.change_progress_stage_list
    import capo_opensearch.types.config_change_status
    import capo_opensearch.types.guid
    import capo_opensearch.types.initiated_by
    import capo_opensearch.types.overall_change_status
    import capo_opensearch.types.string_list
    import capo_opensearch.types.total_number_of_stages
    import capo_opensearch.types.update_timestamp
    import capo_opensearch.types.validation_failures


class ChangeProgressStatusDetails(TypedDict, closed=True):
    change_id: NotRequired["capo_opensearch.types.guid.GUID"]
    """<p>The unique change identifier associated with a specific domain configuration change.</p>"""
    start_time: NotRequired["capo_opensearch.types.update_timestamp.UpdateTimestamp"]
    """<p>The time at which the configuration change is made on the domain.</p>"""
    status: NotRequired[
        "capo_opensearch.types.overall_change_status.OverallChangeStatus"
    ]
    """<p>The overall status of the domain configuration change.</p>"""
    pending_properties: NotRequired["capo_opensearch.types.string_list.StringList"]
    """<p>The list of properties in the domain configuration change that are still pending.</p>"""
    completed_properties: NotRequired["capo_opensearch.types.string_list.StringList"]
    """<p>The list of properties in the domain configuration change that have completed.</p>"""
    total_number_of_stages: (
        "capo_opensearch.types.total_number_of_stages.TotalNumberOfStages"
    )
    """<p>The total number of stages required for the configuration change.</p>"""
    change_progress_stages: NotRequired[
        "capo_opensearch.types.change_progress_stage_list.ChangeProgressStageList"
    ]
    """<p>The specific stages that the domain is going through to perform the configuration change.</p>"""
    last_updated_time: NotRequired[
        "capo_opensearch.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The last time that the status of the configuration change was updated.</p>"""
    config_change_status: NotRequired[
        "capo_opensearch.types.config_change_status.ConfigChangeStatus"
    ]
    """<p>The current status of the configuration change.</p>"""
    initiated_by: NotRequired["capo_opensearch.types.initiated_by.InitiatedBy"]
    """<p>The IAM principal who initiated the configuration change.</p>"""
    validation_failures: NotRequired[
        "capo_opensearch.types.validation_failures.ValidationFailures"
    ]
    """<p>The validation failures that occurred as a result of the configuration change.</p>"""
    accepted_warnings: NotRequired[
        "capo_opensearch.types.accepted_warnings_list.AcceptedWarningsList"
    ]
    """<p>The list of advisory warning codes that were accepted for the configuration change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeProgressStatusDetails) -> dict:
    out: dict = {}
    if "change_id" in value:
        out["ChangeId"] = value["change_id"]
    if "start_time" in value:
        import capo_opensearch.types.update_timestamp

        out["StartTime"] = capo_opensearch.types.update_timestamp.serialize_json(
            value["start_time"]
        )
    if "status" in value:
        import capo_opensearch.types.overall_change_status

        out["Status"] = capo_opensearch.types.overall_change_status.serialize_json(
            value["status"]
        )
    if "pending_properties" in value:
        import capo_opensearch.types.string_list

        out["PendingProperties"] = capo_opensearch.types.string_list.serialize_json(
            value["pending_properties"]
        )
    if "completed_properties" in value:
        import capo_opensearch.types.string_list

        out["CompletedProperties"] = capo_opensearch.types.string_list.serialize_json(
            value["completed_properties"]
        )
    out["TotalNumberOfStages"] = value.get("total_number_of_stages", 0)
    if "change_progress_stages" in value:
        import capo_opensearch.types.change_progress_stage_list

        out["ChangeProgressStages"] = (
            capo_opensearch.types.change_progress_stage_list.serialize_json(
                value["change_progress_stages"]
            )
        )
    if "last_updated_time" in value:
        import capo_opensearch.types.update_timestamp

        out["LastUpdatedTime"] = capo_opensearch.types.update_timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "config_change_status" in value:
        import capo_opensearch.types.config_change_status

        out["ConfigChangeStatus"] = (
            capo_opensearch.types.config_change_status.serialize_json(
                value["config_change_status"]
            )
        )
    if "initiated_by" in value:
        import capo_opensearch.types.initiated_by

        out["InitiatedBy"] = capo_opensearch.types.initiated_by.serialize_json(
            value["initiated_by"]
        )
    if "validation_failures" in value:
        import capo_opensearch.types.validation_failures

        out["ValidationFailures"] = (
            capo_opensearch.types.validation_failures.serialize_json(
                value["validation_failures"]
            )
        )
    if "accepted_warnings" in value:
        import capo_opensearch.types.accepted_warnings_list

        out["AcceptedWarnings"] = (
            capo_opensearch.types.accepted_warnings_list.serialize_json(
                value["accepted_warnings"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChangeProgressStatusDetails:
    out: ChangeProgressStatusDetails = {}  # type: ignore[typeddict-item]
    if data.get("ChangeId") is not None:
        out["change_id"] = data["ChangeId"]
    if data.get("StartTime") is not None:
        import capo_opensearch.types.update_timestamp

        out["start_time"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["StartTime"]
        )
    if data.get("Status") is not None:
        import capo_opensearch.types.overall_change_status

        out["status"] = capo_opensearch.types.overall_change_status.deserialize_json(
            data["Status"]
        )
    if data.get("PendingProperties") is not None:
        import capo_opensearch.types.string_list

        out["pending_properties"] = capo_opensearch.types.string_list.deserialize_json(
            data["PendingProperties"]
        )
    if data.get("CompletedProperties") is not None:
        import capo_opensearch.types.string_list

        out["completed_properties"] = (
            capo_opensearch.types.string_list.deserialize_json(
                data["CompletedProperties"]
            )
        )
    if data.get("TotalNumberOfStages") is not None:
        out["total_number_of_stages"] = data["TotalNumberOfStages"]
    else:
        out["total_number_of_stages"] = 0
    if data.get("ChangeProgressStages") is not None:
        import capo_opensearch.types.change_progress_stage_list

        out["change_progress_stages"] = (
            capo_opensearch.types.change_progress_stage_list.deserialize_json(
                data["ChangeProgressStages"]
            )
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_opensearch.types.update_timestamp

        out["last_updated_time"] = (
            capo_opensearch.types.update_timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if data.get("ConfigChangeStatus") is not None:
        import capo_opensearch.types.config_change_status

        out["config_change_status"] = (
            capo_opensearch.types.config_change_status.deserialize_json(
                data["ConfigChangeStatus"]
            )
        )
    if data.get("InitiatedBy") is not None:
        import capo_opensearch.types.initiated_by

        out["initiated_by"] = capo_opensearch.types.initiated_by.deserialize_json(
            data["InitiatedBy"]
        )
    if data.get("ValidationFailures") is not None:
        import capo_opensearch.types.validation_failures

        out["validation_failures"] = (
            capo_opensearch.types.validation_failures.deserialize_json(
                data["ValidationFailures"]
            )
        )
    if data.get("AcceptedWarnings") is not None:
        import capo_opensearch.types.accepted_warnings_list

        out["accepted_warnings"] = (
            capo_opensearch.types.accepted_warnings_list.deserialize_json(
                data["AcceptedWarnings"]
            )
        )
    return out
