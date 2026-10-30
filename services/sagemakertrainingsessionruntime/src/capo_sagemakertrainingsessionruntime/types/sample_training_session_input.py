"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleTrainingSessionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.inference_body
    import capo_sagemakertrainingsessionruntime.types.training_session_name


class SampleTrainingSessionInput(TypedDict, closed=True):
    training_session_name: "capo_sagemakertrainingsessionruntime.types.training_session_name.TrainingSessionName"
    """<p>The name of the training session whose model to invoke.</p>"""
    content_type: NotRequired["str"]
    """<p>The MIME type of the input data in the request body.</p>"""
    accept: NotRequired["str"]
    """<p>The desired MIME type of the inference body in the response.</p>"""
    model_package_arn: NotRequired["str"]
    """<p>The ARN of the model package whose checkpoint to invoke.</p>"""
    body: NotRequired[
        "capo_sagemakertrainingsessionruntime.types.inference_body.InferenceBody"
    ]
    """<p>The raw inference request body.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleTrainingSessionInput) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_sagemakertrainingsessionruntime.types.inference_body

        out["body"] = (
            capo_sagemakertrainingsessionruntime.types.inference_body.serialize_json(
                value["body"]
            )
        )
    return out


def deserialize_json(data: dict) -> SampleTrainingSessionInput:
    out: SampleTrainingSessionInput = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_sagemakertrainingsessionruntime.types.inference_body

        out["body"] = (
            capo_sagemakertrainingsessionruntime.types.inference_body.deserialize_json(
                data["body"]
            )
        )
    return out


def redact_sensitive(value: SampleTrainingSessionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
