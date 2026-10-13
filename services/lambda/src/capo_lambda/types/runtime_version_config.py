"""Generated from Smithy shape ``com.amazonaws.lambda#RuntimeVersionConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.runtime_version_arn
    import capo_lambda.types.runtime_version_error


class RuntimeVersionConfig(TypedDict, closed=True):
    runtime_version_arn: NotRequired[
        "capo_lambda.types.runtime_version_arn.RuntimeVersionArn"
    ]
    """<p>The ARN of the runtime version you want the function to use.</p>"""
    error: NotRequired["capo_lambda.types.runtime_version_error.RuntimeVersionError"]
    """<p>Error response when Lambda is unable to retrieve the runtime version for a function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeVersionConfig) -> dict:
    out: dict = {}
    if "runtime_version_arn" in value:
        out["RuntimeVersionArn"] = value["runtime_version_arn"]
    if "error" in value:
        import capo_lambda.types.runtime_version_error

        out["Error"] = capo_lambda.types.runtime_version_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> RuntimeVersionConfig:
    out: RuntimeVersionConfig = {}  # type: ignore[typeddict-item]
    if data.get("RuntimeVersionArn") is not None:
        out["runtime_version_arn"] = data["RuntimeVersionArn"]
    if data.get("Error") is not None:
        import capo_lambda.types.runtime_version_error

        out["error"] = capo_lambda.types.runtime_version_error.deserialize_json(
            data["Error"]
        )
    return out


def redact_sensitive(value: RuntimeVersionConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "error" in value:
        import capo_lambda.types.runtime_version_error

        out["error"] = capo_lambda.types.runtime_version_error.redact_sensitive(
            value["error"]
        )
    return out
