"""Generated from Smithy shape ``com.amazonaws.voiceid#StartFraudsterRegistrationJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.fraudster_registration_job


class StartFraudsterRegistrationJobResponse(TypedDict, closed=True):
    job: NotRequired[
        "capo_voice_id.types.fraudster_registration_job.FraudsterRegistrationJob"
    ]
    """<p>Details about the started fraudster registration job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFraudsterRegistrationJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import capo_voice_id.types.fraudster_registration_job

        out["Job"] = (
            capo_voice_id.types.fraudster_registration_job.serialize_aws_json_1_0(
                value["job"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFraudsterRegistrationJobResponse:
    out: StartFraudsterRegistrationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("Job") is not None:
        import capo_voice_id.types.fraudster_registration_job

        out["job"] = (
            capo_voice_id.types.fraudster_registration_job.deserialize_aws_json_1_0(
                data["Job"]
            )
        )
    return out


def redact_sensitive(value: StartFraudsterRegistrationJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job" in value:
        import capo_voice_id.types.fraudster_registration_job

        out["job"] = capo_voice_id.types.fraudster_registration_job.redact_sensitive(
            value["job"]
        )
    return out
