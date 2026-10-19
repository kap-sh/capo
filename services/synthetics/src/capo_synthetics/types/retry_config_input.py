"""Generated from Smithy shape ``com.amazonaws.synthetics#RetryConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.max_retries


class RetryConfigInput(TypedDict, closed=True):
    max_retries: "capo_synthetics.types.max_retries.MaxRetries"
    """<p>The maximum number of retries. The value must be less than or equal to 2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryConfigInput) -> dict:
    out: dict = {}
    out["MaxRetries"] = value["max_retries"]
    return out


def deserialize_json(data: dict) -> RetryConfigInput:
    out: RetryConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxRetries") is not None:
        out["max_retries"] = data["MaxRetries"]
    else:
        out["max_retries"] = 0
    return out
