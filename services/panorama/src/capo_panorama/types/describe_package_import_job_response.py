"""Generated from Smithy shape ``com.amazonaws.panorama#DescribePackageImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.client_token
    import capo_panorama.types.created_time
    import capo_panorama.types.job_id
    import capo_panorama.types.job_tags_list
    import capo_panorama.types.last_updated_time
    import capo_panorama.types.package_import_job_input_config
    import capo_panorama.types.package_import_job_output
    import capo_panorama.types.package_import_job_output_config
    import capo_panorama.types.package_import_job_status
    import capo_panorama.types.package_import_job_status_message
    import capo_panorama.types.package_import_job_type


class DescribePackageImportJobResponse(TypedDict, closed=True):
    job_id: "capo_panorama.types.job_id.JobId"
    """<p>The job's ID.</p>"""
    client_token: NotRequired["capo_panorama.types.client_token.ClientToken"]
    """<p>The job's client token.</p>"""
    job_type: "capo_panorama.types.package_import_job_type.PackageImportJobType"
    """<p>The job's type.</p>"""
    input_config: "capo_panorama.types.package_import_job_input_config.PackageImportJobInputConfig"
    """<p>The job's input config.</p>"""
    output_config: "capo_panorama.types.package_import_job_output_config.PackageImportJobOutputConfig"
    """<p>The job's output config.</p>"""
    output: "capo_panorama.types.package_import_job_output.PackageImportJobOutput"
    """<p>The job's output.</p>"""
    created_time: "capo_panorama.types.created_time.CreatedTime"
    """<p>When the job was created.</p>"""
    last_updated_time: "capo_panorama.types.last_updated_time.LastUpdatedTime"
    """<p>When the job was updated.</p>"""
    status: "capo_panorama.types.package_import_job_status.PackageImportJobStatus"
    """<p>The job's status.</p>"""
    status_message: "capo_panorama.types.package_import_job_status_message.PackageImportJobStatusMessage"
    """<p>The job's status message.</p>"""
    job_tags: NotRequired["capo_panorama.types.job_tags_list.JobTagsList"]
    """<p>The job's tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackageImportJobResponse) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["JobType"] = value["job_type"]
    import capo_panorama.types.package_import_job_input_config

    out["InputConfig"] = (
        capo_panorama.types.package_import_job_input_config.serialize_json(
            value["input_config"]
        )
    )
    import capo_panorama.types.package_import_job_output_config

    out["OutputConfig"] = (
        capo_panorama.types.package_import_job_output_config.serialize_json(
            value["output_config"]
        )
    )
    import capo_panorama.types.package_import_job_output

    out["Output"] = capo_panorama.types.package_import_job_output.serialize_json(
        value["output"]
    )
    import capo_panorama.types.created_time

    out["CreatedTime"] = capo_panorama.types.created_time.serialize_json(
        value["created_time"]
    )
    import capo_panorama.types.last_updated_time

    out["LastUpdatedTime"] = capo_panorama.types.last_updated_time.serialize_json(
        value["last_updated_time"]
    )
    out["Status"] = value["status"]
    out["StatusMessage"] = value["status_message"]
    if "job_tags" in value:
        import capo_panorama.types.job_tags_list

        out["JobTags"] = capo_panorama.types.job_tags_list.serialize_json(
            value["job_tags"]
        )
    return out


def deserialize_json(data: dict) -> DescribePackageImportJobResponse:
    out: DescribePackageImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("JobType") is not None:
        out["job_type"] = data["JobType"]
    else:
        out["job_type"] = ""
    if data.get("InputConfig") is not None:
        import capo_panorama.types.package_import_job_input_config

        out["input_config"] = (
            capo_panorama.types.package_import_job_input_config.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePackageImportJobResponse.input_config required"
        )
    if data.get("OutputConfig") is not None:
        import capo_panorama.types.package_import_job_output_config

        out["output_config"] = (
            capo_panorama.types.package_import_job_output_config.deserialize_json(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePackageImportJobResponse.output_config required"
        )
    if data.get("Output") is not None:
        import capo_panorama.types.package_import_job_output

        out["output"] = capo_panorama.types.package_import_job_output.deserialize_json(
            data["Output"]
        )
    else:
        raise DeserializationError("DescribePackageImportJobResponse.output required")
    if data.get("CreatedTime") is not None:
        import capo_panorama.types.created_time

        out["created_time"] = capo_panorama.types.created_time.deserialize_json(
            data["CreatedTime"]
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_panorama.types.last_updated_time

        out["last_updated_time"] = (
            capo_panorama.types.last_updated_time.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    else:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    else:
        out["status_message"] = ""
    if data.get("JobTags") is not None:
        import capo_panorama.types.job_tags_list

        out["job_tags"] = capo_panorama.types.job_tags_list.deserialize_json(
            data["JobTags"]
        )
    return out
