"""Generated from Smithy shape ``com.amazonaws.endusermessaging#Job``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_endusermessaging.types.brand_profile_id_or_arn
    import capo_endusermessaging.types.job_error_code
    import capo_endusermessaging.types.job_error_message
    import capo_endusermessaging.types.job_id
    import capo_endusermessaging.types.job_operation_type
    import capo_endusermessaging.types.job_resource_list
    import capo_endusermessaging.types.job_status


class Job(TypedDict, closed=True):
    job_id: "capo_endusermessaging.types.job_id.JobId"
    """<p>The unique identifier of the asynchronous job. Use the GetJob operation to check the status of the job and to retrieve its results.</p>"""
    status: "capo_endusermessaging.types.job_status.JobStatus"
    """<p>The current lifecycle status of the job.</p>"""
    operation_type: "capo_endusermessaging.types.job_operation_type.JobOperationType"
    """<p>The type of mutating operation that created the job.</p>"""
    created_at: "datetime.datetime"
    """<p>The time when the resource was created, in Unix epoch time.</p>"""
    updated_at: "datetime.datetime"
    """<p>The time when the resource was last updated, in Unix epoch time.</p>"""
    brand_profile_id: NotRequired[
        "capo_endusermessaging.types.brand_profile_id_or_arn.BrandProfileIdOrArn"
    ]
    """<p>The brand profile that the job operates on. This value is absent for operations that create a brand profile.</p>"""
    error_code: NotRequired["capo_endusermessaging.types.job_error_code.JobErrorCode"]
    """<p>A machine-readable code that identifies why the job failed. This value is present only when the job status is FAILED.</p>"""
    error_message: NotRequired[
        "capo_endusermessaging.types.job_error_message.JobErrorMessage"
    ]
    """<p>A human-readable description of why the job failed. This value is present only when the job status is FAILED.</p>"""
    resources: NotRequired[
        "capo_endusermessaging.types.job_resource_list.JobResourceList"
    ]
    """<p>The resources that were created or updated by the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    import capo_endusermessaging.types.job_status

    out["status"] = capo_endusermessaging.types.job_status.serialize_json(
        value["status"]
    )
    out["operationType"] = value["operation_type"]
    import capo_endusermessaging.types._prelude.timestamp

    out["createdAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_endusermessaging.types._prelude.timestamp

    out["updatedAt"] = capo_endusermessaging.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "brand_profile_id" in value:
        out["brandProfileId"] = value["brand_profile_id"]
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "resources" in value:
        import capo_endusermessaging.types.job_resource_list

        out["resources"] = capo_endusermessaging.types.job_resource_list.serialize_json(
            value["resources"]
        )
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        raise DeserializationError("Job.job_id required")
    if data.get("status") is not None:
        import capo_endusermessaging.types.job_status

        out["status"] = capo_endusermessaging.types.job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("Job.status required")
    if data.get("operationType") is not None:
        out["operation_type"] = data["operationType"]
    else:
        raise DeserializationError("Job.operation_type required")
    if data.get("createdAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["created_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Job.created_at required")
    if data.get("updatedAt") is not None:
        import capo_endusermessaging.types._prelude.timestamp

        out["updated_at"] = (
            capo_endusermessaging.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Job.updated_at required")
    if data.get("brandProfileId") is not None:
        out["brand_profile_id"] = data["brandProfileId"]
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("resources") is not None:
        import capo_endusermessaging.types.job_resource_list

        out["resources"] = (
            capo_endusermessaging.types.job_resource_list.deserialize_json(
                data["resources"]
            )
        )
    return out
