"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#SampleResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemakerjobruntime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemakerjobruntime.types.inference_response_body


class SampleResponse(TypedDict, closed=True):
    content_type: NotRequired["str"]
    """MIME type of the inference result."""
    body: "capo_sagemakerjobruntime.types.inference_response_body.InferenceResponseBody"
    """The raw inference response body from the model."""


# --- restJson1 ser/de ---
def serialize_json(value: SampleResponse) -> dict:
    out: dict = {}
    import capo_sagemakerjobruntime.types.inference_response_body

    out["Body"] = capo_sagemakerjobruntime.types.inference_response_body.serialize_json(
        value["body"]
    )
    return out


def deserialize_json(data: dict) -> SampleResponse:
    out: SampleResponse = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        import capo_sagemakerjobruntime.types.inference_response_body

        out["body"] = (
            capo_sagemakerjobruntime.types.inference_response_body.deserialize_json(
                data["Body"]
            )
        )
    else:
        raise DeserializationError("SampleResponse.body required")
    return out


def redact_sensitive(value: SampleResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out
