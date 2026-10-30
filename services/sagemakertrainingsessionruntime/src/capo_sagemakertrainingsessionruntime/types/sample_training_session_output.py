"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleTrainingSessionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.inference_body


class SampleTrainingSessionOutput(TypedDict, closed=True):
    content_type: NotRequired["str"]
    """<p>The MIME type of the inference result in the response body.</p>"""
    body: "capo_sagemakertrainingsessionruntime.types.inference_body.InferenceBody"
    """<p>The raw inference response body from the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleTrainingSessionOutput) -> dict:
    out: dict = {}
    import capo_sagemakertrainingsessionruntime.types.inference_body

    out["body"] = (
        capo_sagemakertrainingsessionruntime.types.inference_body.serialize_json(
            value["body"]
        )
    )
    return out


def deserialize_json(data: dict) -> SampleTrainingSessionOutput:
    out: SampleTrainingSessionOutput = {}  # type: ignore[typeddict-item]
    if data.get("body") is not None:
        import capo_sagemakertrainingsessionruntime.types.inference_body

        out["body"] = (
            capo_sagemakertrainingsessionruntime.types.inference_body.deserialize_json(
                data["body"]
            )
        )
    else:
        out["body"] = b""
    return out


def redact_sensitive(value: SampleTrainingSessionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
