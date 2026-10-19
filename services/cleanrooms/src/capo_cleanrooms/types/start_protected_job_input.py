"""Generated from Smithy shape ``com.amazonaws.cleanrooms#StartProtectedJobInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.protected_job_compute_configuration
    import capo_cleanrooms.types.protected_job_parameters
    import capo_cleanrooms.types.protected_job_result_configuration_input
    import capo_cleanrooms.types.protected_job_type


class StartProtectedJobInput(TypedDict, closed=True):
    type: "capo_cleanrooms.types.protected_job_type.ProtectedJobType"
    """<p> The type of protected job to start.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership to run this job against. Currently accepts a membership ID.</p>"""
    job_parameters: (
        "capo_cleanrooms.types.protected_job_parameters.ProtectedJobParameters"
    )
    """<p> The job parameters.</p>"""
    result_configuration: NotRequired[
        "capo_cleanrooms.types.protected_job_result_configuration_input.ProtectedJobResultConfigurationInput"
    ]
    """<p>The details needed to write the job results.</p>"""
    compute_configuration: NotRequired[
        "capo_cleanrooms.types.protected_job_compute_configuration.ProtectedJobComputeConfiguration"
    ]
    """<p>The compute configuration for the protected job.</p>"""
    job_compute_payer_account_id: NotRequired[
        "capo_cleanrooms.types.account_id.AccountId"
    ]
    """<p>The account ID of the member that pays for the job compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartProtectedJobInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_job_type

    out["type"] = capo_cleanrooms.types.protected_job_type.serialize_json(value["type"])
    import capo_cleanrooms.types.protected_job_parameters

    out["jobParameters"] = (
        capo_cleanrooms.types.protected_job_parameters.serialize_json(
            value["job_parameters"]
        )
    )
    if "result_configuration" in value:
        import capo_cleanrooms.types.protected_job_result_configuration_input

        out["resultConfiguration"] = (
            capo_cleanrooms.types.protected_job_result_configuration_input.serialize_json(
                value["result_configuration"]
            )
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


def deserialize_json(data: dict) -> StartProtectedJobInput:
    out: StartProtectedJobInput = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_cleanrooms.types.protected_job_type

        out["type"] = capo_cleanrooms.types.protected_job_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.protected_job_type.ProtectedJobType", ""
        )
    if data.get("jobParameters") is not None:
        import capo_cleanrooms.types.protected_job_parameters

        out["job_parameters"] = (
            capo_cleanrooms.types.protected_job_parameters.deserialize_json(
                data["jobParameters"]
            )
        )
    else:
        raise DeserializationError("StartProtectedJobInput.job_parameters required")
    if data.get("resultConfiguration") is not None:
        import capo_cleanrooms.types.protected_job_result_configuration_input

        out["result_configuration"] = (
            capo_cleanrooms.types.protected_job_result_configuration_input.deserialize_json(
                data["resultConfiguration"]
            )
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


def redact_sensitive(value: StartProtectedJobInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_parameters" in value:
        import capo_cleanrooms.types.protected_job_parameters

        out["job_parameters"] = (
            capo_cleanrooms.types.protected_job_parameters.redact_sensitive(
                value["job_parameters"]
            )
        )
    return out
