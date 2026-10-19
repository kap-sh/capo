"""Generated from Smithy shape ``com.amazonaws.emrcontainers#RetryPolicyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.java_integer


class RetryPolicyConfiguration(TypedDict, closed=True):
    max_attempts: "capo_emr_containers.types.java_integer.JavaInteger"
    """<p>The maximum number of attempts on the job's driver.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryPolicyConfiguration) -> dict:
    out: dict = {}
    out["maxAttempts"] = value["max_attempts"]
    return out


def deserialize_json(data: dict) -> RetryPolicyConfiguration:
    out: RetryPolicyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("maxAttempts") is not None:
        out["max_attempts"] = data["maxAttempts"]
    else:
        out["max_attempts"] = 0
    return out
