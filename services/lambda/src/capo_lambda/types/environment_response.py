"""Generated from Smithy shape ``com.amazonaws.lambda#EnvironmentResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.environment_error
    import capo_lambda.types.environment_variables


class EnvironmentResponse(TypedDict, closed=True):
    variables: NotRequired[
        "capo_lambda.types.environment_variables.EnvironmentVariables"
    ]
    """<p>Environment variable key-value pairs. Omitted from CloudTrail logs.</p>"""
    error: NotRequired["capo_lambda.types.environment_error.EnvironmentError"]
    """<p>Error messages for environment variables that couldn't be applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentResponse) -> dict:
    out: dict = {}
    if "variables" in value:
        import capo_lambda.types.environment_variables

        out["Variables"] = capo_lambda.types.environment_variables.serialize_json(
            value["variables"]
        )
    if "error" in value:
        import capo_lambda.types.environment_error

        out["Error"] = capo_lambda.types.environment_error.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> EnvironmentResponse:
    out: EnvironmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("Variables") is not None:
        import capo_lambda.types.environment_variables

        out["variables"] = capo_lambda.types.environment_variables.deserialize_json(
            data["Variables"]
        )
    if data.get("Error") is not None:
        import capo_lambda.types.environment_error

        out["error"] = capo_lambda.types.environment_error.deserialize_json(
            data["Error"]
        )
    return out


def redact_sensitive(value: EnvironmentResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "variables" in value:
        out["variables"] = "*** Sensitive Data Redacted ***"
    if "error" in value:
        import capo_lambda.types.environment_error

        out["error"] = capo_lambda.types.environment_error.redact_sensitive(
            value["error"]
        )
    return out
