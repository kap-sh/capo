"""Generated from Smithy shape ``com.amazonaws.mailmanager#ImportJob``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.address_list_id
    import capo_mailmanager.types.error_message
    import capo_mailmanager.types.import_data_format
    import capo_mailmanager.types.import_job_status
    import capo_mailmanager.types.job_id
    import capo_mailmanager.types.job_items_count
    import capo_mailmanager.types.job_name
    import capo_mailmanager.types.pre_signed_url


class ImportJob(TypedDict, closed=True):
    job_id: "capo_mailmanager.types.job_id.JobId"
    """<p>The identifier of the import job.</p>"""
    name: "capo_mailmanager.types.job_name.JobName"
    """<p>A user-friendly name for the import job.</p>"""
    status: "capo_mailmanager.types.import_job_status.ImportJobStatus"
    """<p>The status of the import job.</p>"""
    pre_signed_url: "capo_mailmanager.types.pre_signed_url.PreSignedUrl"
    """<p>The pre-signed URL target for uploading the input file.</p>"""
    imported_items_count: NotRequired[
        "capo_mailmanager.types.job_items_count.JobItemsCount"
    ]
    """<p>The number of addresses in the input that were successfully imported into the address list.</p>"""
    failed_items_count: NotRequired[
        "capo_mailmanager.types.job_items_count.JobItemsCount"
    ]
    """<p>The number of addresses in the input that failed to get imported into address list.</p>"""
    import_data_format: "capo_mailmanager.types.import_data_format.ImportDataFormat"
    """<p>The format of the input for the import job.</p>"""
    address_list_id: "capo_mailmanager.types.address_list_id.AddressListId"
    """<p>The unique identifier of the address list the import job was created for.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The timestamp of when the import job was created.</p>"""
    start_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the import job was started.</p>"""
    completed_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the import job was completed.</p>"""
    error: NotRequired["capo_mailmanager.types.error_message.ErrorMessage"]
    """<p>The reason for failure of an import job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportJob) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    out["Name"] = value["name"]
    import capo_mailmanager.types.import_job_status

    out["Status"] = capo_mailmanager.types.import_job_status.serialize_aws_json_1_0(
        value["status"]
    )
    out["PreSignedUrl"] = value["pre_signed_url"]
    if "imported_items_count" in value:
        out["ImportedItemsCount"] = value["imported_items_count"]
    if "failed_items_count" in value:
        out["FailedItemsCount"] = value["failed_items_count"]
    import capo_mailmanager.types.import_data_format

    out["ImportDataFormat"] = (
        capo_mailmanager.types.import_data_format.serialize_aws_json_1_0(
            value["import_data_format"]
        )
    )
    out["AddressListId"] = value["address_list_id"]
    import capo_mailmanager.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    if "start_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["StartTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start_timestamp"]
            )
        )
    if "completed_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CompletedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["completed_timestamp"]
            )
        )
    if "error" in value:
        out["Error"] = value["error"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportJob:
    out: ImportJob = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("ImportJob.job_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ImportJob.name required")
    if data.get("Status") is not None:
        import capo_mailmanager.types.import_job_status

        out["status"] = (
            capo_mailmanager.types.import_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ImportJob.status required")
    if data.get("PreSignedUrl") is not None:
        out["pre_signed_url"] = data["PreSignedUrl"]
    else:
        raise DeserializationError("ImportJob.pre_signed_url required")
    if data.get("ImportedItemsCount") is not None:
        out["imported_items_count"] = data["ImportedItemsCount"]
    if data.get("FailedItemsCount") is not None:
        out["failed_items_count"] = data["FailedItemsCount"]
    if data.get("ImportDataFormat") is not None:
        import capo_mailmanager.types.import_data_format

        out["import_data_format"] = (
            capo_mailmanager.types.import_data_format.deserialize_aws_json_1_0(
                data["ImportDataFormat"]
            )
        )
    else:
        raise DeserializationError("ImportJob.import_data_format required")
    if data.get("AddressListId") is not None:
        out["address_list_id"] = data["AddressListId"]
    else:
        raise DeserializationError("ImportJob.address_list_id required")
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("ImportJob.created_timestamp required")
    if data.get("StartTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["start_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["StartTimestamp"]
            )
        )
    if data.get("CompletedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["completed_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CompletedTimestamp"]
            )
        )
    if data.get("Error") is not None:
        out["error"] = data["Error"]
    return out


def redact_sensitive(value: ImportJob) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pre_signed_url" in value:
        out["pre_signed_url"] = "*** Sensitive Data Redacted ***"
    return out
