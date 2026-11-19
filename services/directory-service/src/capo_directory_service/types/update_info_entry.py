"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateInfoEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.initiated_by
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.region_name
    import capo_directory_service.types.start_date_time
    import capo_directory_service.types.update_status
    import capo_directory_service.types.update_status_reason
    import capo_directory_service.types.update_value


class UpdateInfoEntry(TypedDict, closed=True):
    region: NotRequired["capo_directory_service.types.region_name.RegionName"]
    """<p> The name of the Region. </p>"""
    status: NotRequired["capo_directory_service.types.update_status.UpdateStatus"]
    """<p> The status of the update performed on the directory. </p>"""
    status_reason: NotRequired[
        "capo_directory_service.types.update_status_reason.UpdateStatusReason"
    ]
    """<p> The reason for the current status of the update type activity. </p>"""
    initiated_by: NotRequired["capo_directory_service.types.initiated_by.InitiatedBy"]
    """<p> This specifies if the update was initiated by the customer or by the service team. </p>"""
    new_value: NotRequired["capo_directory_service.types.update_value.UpdateValue"]
    """<p> The new value of the target setting. </p>"""
    previous_value: NotRequired["capo_directory_service.types.update_value.UpdateValue"]
    """<p> The old value of the target setting. </p>"""
    start_time: NotRequired[
        "capo_directory_service.types.start_date_time.StartDateTime"
    ]
    """<p> The start time of the <code>UpdateDirectorySetup</code> for the particular type. </p>"""
    last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p> The last updated date and time of a particular directory setting. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInfoEntry) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
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
        import capo_directory_service.types.update_value

        out["NewValue"] = (
            capo_directory_service.types.update_value.serialize_aws_json_1_1(
                value["new_value"]
            )
        )
    if "previous_value" in value:
        import capo_directory_service.types.update_value

        out["PreviousValue"] = (
            capo_directory_service.types.update_value.serialize_aws_json_1_1(
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInfoEntry:
    out: UpdateInfoEntry = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
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
        import capo_directory_service.types.update_value

        out["new_value"] = (
            capo_directory_service.types.update_value.deserialize_aws_json_1_1(
                data["NewValue"]
            )
        )
    if data.get("PreviousValue") is not None:
        import capo_directory_service.types.update_value

        out["previous_value"] = (
            capo_directory_service.types.update_value.deserialize_aws_json_1_1(
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateInfoEntry) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
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
        import capo_directory_service.types.update_value

        out["NewValue"] = capo_directory_service.types.update_value.serialize_cbor(
            value["new_value"]
        )
    if "previous_value" in value:
        import capo_directory_service.types.update_value

        out["PreviousValue"] = capo_directory_service.types.update_value.serialize_cbor(
            value["previous_value"]
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
    return out


def deserialize_cbor(data: dict) -> UpdateInfoEntry:
    out: UpdateInfoEntry = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
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
        import capo_directory_service.types.update_value

        out["new_value"] = capo_directory_service.types.update_value.deserialize_cbor(
            data["NewValue"]
        )
    if data.get("PreviousValue") is not None:
        import capo_directory_service.types.update_value

        out["previous_value"] = (
            capo_directory_service.types.update_value.deserialize_cbor(
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
    return out
