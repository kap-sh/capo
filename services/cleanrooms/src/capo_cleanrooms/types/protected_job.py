"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJob``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.protected_job_compute_configuration
    import capo_cleanrooms.types.protected_job_error
    import capo_cleanrooms.types.protected_job_identifier
    import capo_cleanrooms.types.protected_job_parameters
    import capo_cleanrooms.types.protected_job_result
    import capo_cleanrooms.types.protected_job_result_configuration_output
    import capo_cleanrooms.types.protected_job_statistics
    import capo_cleanrooms.types.protected_job_status


class ProtectedJob(TypedDict, closed=True):
    id: "capo_cleanrooms.types.protected_job_identifier.ProtectedJobIdentifier"
    """<p>The identifier for a protected job instance.</p>"""
    membership_id: "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    """<p>he identifier for the membership.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The ARN of the membership.</p>"""
    create_time: "datetime.datetime"
    """<p> The creation time of the protected job.</p>"""
    job_parameters: NotRequired[
        "capo_cleanrooms.types.protected_job_parameters.ProtectedJobParameters"
    ]
    """<p> The job parameters for the protected job.</p>"""
    status: "capo_cleanrooms.types.protected_job_status.ProtectedJobStatus"
    """<p> The status of the protected job.</p>"""
    result_configuration: NotRequired[
        "capo_cleanrooms.types.protected_job_result_configuration_output.ProtectedJobResultConfigurationOutput"
    ]
    """<p>Contains any details needed to write the job results.</p>"""
    statistics: NotRequired[
        "capo_cleanrooms.types.protected_job_statistics.ProtectedJobStatistics"
    ]
    """<p> The statistics of the protected job.</p>"""
    result: NotRequired["capo_cleanrooms.types.protected_job_result.ProtectedJobResult"]
    """<p> The result of the protected job.</p>"""
    error: NotRequired["capo_cleanrooms.types.protected_job_error.ProtectedJobError"]
    """<p> The error from the protected job.</p>"""
    compute_configuration: NotRequired[
        "capo_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
    ]
    """<p>The compute configuration for the protected job.</p>"""
    job_compute_payer_account_id: NotRequired[
        "capo_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the job compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJob) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    if "job_parameters" in value:
        import capo_cleanrooms.types.protected_job_parameters

        out["jobParameters"] = (
            capo_cleanrooms.types.protected_job_parameters.serialize_json(
                value["job_parameters"]
            )
        )
    import capo_cleanrooms.types.protected_job_status

    out["status"] = capo_cleanrooms.types.protected_job_status.serialize_json(
        value["status"]
    )
    if "result_configuration" in value:
        import capo_cleanrooms.types.protected_job_result_configuration_output

        out["resultConfiguration"] = (
            capo_cleanrooms.types.protected_job_result_configuration_output.serialize_json(
                value["result_configuration"]
            )
        )
    if "statistics" in value:
        import capo_cleanrooms.types.protected_job_statistics

        out["statistics"] = (
            capo_cleanrooms.types.protected_job_statistics.serialize_json(
                value["statistics"]
            )
        )
    if "result" in value:
        import capo_cleanrooms.types.protected_job_result

        out["result"] = capo_cleanrooms.types.protected_job_result.serialize_json(
            value["result"]
        )
    if "error" in value:
        import capo_cleanrooms.types.protected_job_error

        out["error"] = capo_cleanrooms.types.protected_job_error.serialize_json(
            value["error"]
        )
    if "compute_configuration" in value:
        import capo_cleanrooms.types.protected_job_compute_configuration

        out["computeConfiguration"] = (
            capo_cleanrooms.types.protected_job_compute_configuration.serialize_json(
                value["compute_configuration"]
            )
        )
    if "job_compute_payer_account_id" in value:
        out["jobComputePayerAccountId"] = value["job_compute_payer_account_id"]
    return out


def deserialize_json(data: dict) -> ProtectedJob:
    out: ProtectedJob = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ProtectedJob.id required")
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("ProtectedJob.membership_id required")
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("ProtectedJob.membership_arn required")
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("ProtectedJob.create_time required")
    if data.get("jobParameters") is not None:
        import capo_cleanrooms.types.protected_job_parameters

        out["job_parameters"] = (
            capo_cleanrooms.types.protected_job_parameters.deserialize_json(
                data["jobParameters"]
            )
        )
    if data.get("status") is not None:
        import capo_cleanrooms.types.protected_job_status

        out["status"] = capo_cleanrooms.types.protected_job_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ProtectedJob.status required")
    if data.get("resultConfiguration") is not None:
        import capo_cleanrooms.types.protected_job_result_configuration_output

        out["result_configuration"] = (
            capo_cleanrooms.types.protected_job_result_configuration_output.deserialize_json(
                data["resultConfiguration"]
            )
        )
    if data.get("statistics") is not None:
        import capo_cleanrooms.types.protected_job_statistics

        out["statistics"] = (
            capo_cleanrooms.types.protected_job_statistics.deserialize_json(
                data["statistics"]
            )
        )
    if data.get("result") is not None:
        import capo_cleanrooms.types.protected_job_result

        out["result"] = capo_cleanrooms.types.protected_job_result.deserialize_json(
            data["result"]
        )
    if data.get("error") is not None:
        import capo_cleanrooms.types.protected_job_error

        out["error"] = capo_cleanrooms.types.protected_job_error.deserialize_json(
            data["error"]
        )
    if data.get("computeConfiguration") is not None:
        import capo_cleanrooms.types.protected_job_compute_configuration

        out["compute_configuration"] = (
            capo_cleanrooms.types.protected_job_compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if data.get("jobComputePayerAccountId") is not None:
        out["job_compute_payer_account_id"] = data["jobComputePayerAccountId"]
    return out


def redact_sensitive(value: ProtectedJob) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_parameters" in value:
        import capo_cleanrooms.types.protected_job_parameters

        out["job_parameters"] = (
            capo_cleanrooms.types.protected_job_parameters.redact_sensitive(
                value["job_parameters"]
            )
        )
    return out
