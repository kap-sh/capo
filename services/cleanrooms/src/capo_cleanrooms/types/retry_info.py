"""Generated from Smithy shape ``com.amazonaws.cleanrooms#RetryInfo``."""

from typing_extensions import NotRequired, TypedDict


class RetryInfo(TypedDict, closed=True):
    retryable: NotRequired["bool"]
    """<p>Specifies whether running the same request again might succeed. <code>true</code> means that the failure was transient. <code>false</code> means that running the same request again is not expected to succeed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetryInfo) -> dict:
    out: dict = {}
    if "retryable" in value:
        out["retryable"] = value["retryable"]
    return out


def deserialize_json(data: dict) -> RetryInfo:
    out: RetryInfo = {}  # type: ignore[typeddict-item]
    if data.get("retryable") is not None:
        out["retryable"] = data["retryable"]
    return out
