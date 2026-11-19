"""Generated from Smithy shape ``com.amazonaws.directoryservice#HybridUpdateInfoEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_id
    import capo_directory_service.types.hybrid_update_value
    import capo_directory_service.types.initiated_by
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.start_date_time
    import capo_directory_service.types.update_status
    import capo_directory_service.types.update_status_reason


class HybridUpdateInfoEntry(TypedDict, closed=True):
    status: NotRequired["capo_directory_service.types.update_status.UpdateStatus"]
    """<p>The current status of the update activity. Valid values include <code>UPDATED</code>, <code>UPDATING</code>, and <code>UPDATE_FAILED</code>.</p>"""
    status_reason: NotRequired[
        "capo_directory_service.types.update_status_reason.UpdateStatusReason"
    ]
    """<p>A human-readable description of the update status, including any error details or progress information.</p>"""
    initiated_by: NotRequired["capo_directory_service.types.initiated_by.InitiatedBy"]
    """<p>Specifies if the update was initiated by the customer or Amazon Web Services.</p>"""
    new_value: NotRequired[
        "capo_directory_service.types.hybrid_update_value.HybridUpdateValue"
    ]
    """<p>The new configuration values being applied in this update.</p>"""
    previous_value: NotRequired[
        "capo_directory_service.types.hybrid_update_value.HybridUpdateValue"
    ]
    """<p>The previous configuration values before this update was applied.</p>"""
    start_time: NotRequired[
        "capo_directory_service.types.start_date_time.StartDateTime"
    ]
    """<p>The date and time when the update activity was initiated.</p>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time when the update activity status was last updated.</p>"""
    assessment_id: NotRequired[
        "capo_directory_service.types.assessment_id.AssessmentId"
    ]
    """<p>The identifier of the assessment performed to validate this update configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HybridUpdateInfoEntry) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_directory_service.types.update_status

        out["Status"] = (
            capo_directory_service.types.update_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "initiated_by" in value:
        out["InitiatedBy"] = value["initiated_by"]
    if "new_value" in value:
        import capo_directory_service.types.hybrid_update_value

        out["NewValue"] = (
            capo_directory_service.types.hybrid_update_value.serialize_aws_json_1_1(
                value["new_value"]
            )
        )
    if "previous_value" in value:
        import capo_directory_service.types.hybrid_update_value

        out["PreviousValue"] = (
            capo_directory_service.types.hybrid_update_value.serialize_aws_json_1_1(
                value["previous_value"]
            )
        )
    if "start_time" in value:
        import capo_directory_service.types.start_date_time

        out["StartTime"] = (
            capo_directory_service.types.start_date_time.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HybridUpdateInfoEntry:
    out: HybridUpdateInfoEntry = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_directory_service.types.update_status

        out["status"] = (
            capo_directory_service.types.update_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("InitiatedBy") is not None:
        out["initiated_by"] = data["InitiatedBy"]
    if data.get("NewValue") is not None:
        import capo_directory_service.types.hybrid_update_value

        out["new_value"] = (
            capo_directory_service.types.hybrid_update_value.deserialize_aws_json_1_1(
                data["NewValue"]
            )
        )
    if data.get("PreviousValue") is not None:
        import capo_directory_service.types.hybrid_update_value

        out["previous_value"] = (
            capo_directory_service.types.hybrid_update_value.deserialize_aws_json_1_1(
                data["PreviousValue"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_directory_service.types.start_date_time

        out["start_time"] = (
            capo_directory_service.types.start_date_time.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["LastUpdatedDateTime"]
            )
        )
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HybridUpdateInfoEntry) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_directory_service.types.update_status

        out["Status"] = capo_directory_service.types.update_status.serialize_cbor(
            value["status"]
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "initiated_by" in value:
        out["InitiatedBy"] = value["initiated_by"]
    if "new_value" in value:
        import capo_directory_service.types.hybrid_update_value

        out["NewValue"] = (
            capo_directory_service.types.hybrid_update_value.serialize_cbor(
                value["new_value"]
            )
        )
    if "previous_value" in value:
        import capo_directory_service.types.hybrid_update_value

        out["PreviousValue"] = (
            capo_directory_service.types.hybrid_update_value.serialize_cbor(
                value["previous_value"]
            )
        )
    if "start_time" in value:
        import capo_directory_service.types.start_date_time

        out["StartTime"] = capo_directory_service.types.start_date_time.serialize_cbor(
            value["start_time"]
        )
    if "last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["LastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_cbor(
                value["last_updated_date_time"]
            )
        )
    if "assessment_id" in value:
        out["AssessmentId"] = value["assessment_id"]
    return out


def deserialize_cbor(data: dict) -> HybridUpdateInfoEntry:
    out: HybridUpdateInfoEntry = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_directory_service.types.update_status

        out["status"] = capo_directory_service.types.update_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("InitiatedBy") is not None:
        out["initiated_by"] = data["InitiatedBy"]
    if data.get("NewValue") is not None:
        import capo_directory_service.types.hybrid_update_value

        out["new_value"] = (
            capo_directory_service.types.hybrid_update_value.deserialize_cbor(
                data["NewValue"]
            )
        )
    if data.get("PreviousValue") is not None:
        import capo_directory_service.types.hybrid_update_value

        out["previous_value"] = (
            capo_directory_service.types.hybrid_update_value.deserialize_cbor(
                data["PreviousValue"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_directory_service.types.start_date_time

        out["start_time"] = (
            capo_directory_service.types.start_date_time.deserialize_cbor(
                data["StartTime"]
            )
        )
    if data.get("LastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_cbor(
                data["LastUpdatedDateTime"]
            )
        )
    if data.get("AssessmentId") is not None:
        out["assessment_id"] = data["AssessmentId"]
    return out
