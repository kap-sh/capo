"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#SampleRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemakerjobruntime.types.inference_request_body
    import capo_sagemakerjobruntime.types.job_arn
    import capo_sagemakerjobruntime.types.trajectory_id


class SampleRequest(TypedDict, closed=True):
    job_arn: "capo_sagemakerjobruntime.types.job_arn.JobArn"
    """The job ARN that identifies which model session to route the inference request to."""
    trajectory_id: "capo_sagemakerjobruntime.types.trajectory_id.TrajectoryId"
    """The trajectory ID for grouping turns into a single rollout. Each turn (prompt and response) is captured for later use."""
    body: "capo_sagemakerjobruntime.types.inference_request_body.InferenceRequestBody"
    """The raw inference request body in OpenAI-compatible JSON format."""


# --- restJson1 ser/de ---
def serialize_json(value: SampleRequest) -> dict:
    out: dict = {}
    import capo_sagemakerjobruntime.types.inference_request_body

    out["Body"] = capo_sagemakerjobruntime.types.inference_request_body.serialize_json(
        value["body"]
    )
    return out


def deserialize_json(data: dict) -> SampleRequest:
    out: SampleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_sagemakerjobruntime.types.inference_request_body

        out["body"] = (
            capo_sagemakerjobruntime.types.inference_request_body.deserialize_json(
                data["Body"]
            )
        )
    else:
        out["body"] = b""
    return out


def redact_sensitive(value: SampleRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
