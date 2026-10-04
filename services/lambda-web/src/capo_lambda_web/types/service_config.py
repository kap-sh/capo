"""Generated from Smithy shape ``com.amazonaws.lambdaweb#ServiceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.environment_variables
    import capo_lambda_web.types.role_arn
    import capo_lambda_web.types.telemetry_config


class ServiceConfig(TypedDict, closed=True):
    execution_role_arn: "capo_lambda_web.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that the web function assumes when it runs. This role provides permissions to access AWS services and resources.</p>"""
    timeout_seconds: "int"
    """<p>The amount of time (in seconds) that Lambda allows the web function to run before stopping it. Minimum value of 3, maximum value of 900. If you don't specify a value, the default is 30, and this default is returned in the response.</p>"""
    max_concurrency_per_environment: "int"
    """<p>The maximum number of concurrent requests handled per execution environment. Minimum value of 1, maximum value of 128. If you don't specify a value, the default is 64, and this default is returned in the response.</p>"""
    environment_variables: NotRequired[
        "capo_lambda_web.types.environment_variables.EnvironmentVariables"
    ]
    """<p>A map of environment variable key-value pairs available to the web function at runtime. Environment variable values are sensitive.</p>"""
    telemetry_config: NotRequired[
        "capo_lambda_web.types.telemetry_config.TelemetryConfig"
    ]
    """<p>The telemetry configuration for the web function, including logging settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceConfig) -> dict:
    out: dict = {}
    out["executionRoleArn"] = value["execution_role_arn"]
    out["timeoutSeconds"] = value.get("timeout_seconds", 30)
    out["maxConcurrencyPerEnvironment"] = value.get(
        "max_concurrency_per_environment", 64
    )
    if "environment_variables" in value:
        import capo_lambda_web.types.environment_variables

        out["environmentVariables"] = (
            capo_lambda_web.types.environment_variables.serialize_json(
                value["environment_variables"]
            )
        )
    if "telemetry_config" in value:
        import capo_lambda_web.types.telemetry_config

        out["telemetryConfig"] = capo_lambda_web.types.telemetry_config.serialize_json(
            value["telemetry_config"]
        )
    return out


def deserialize_json(data: dict) -> ServiceConfig:
    out: ServiceConfig = {}  # type: ignore[typeddict-item]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("ServiceConfig.execution_role_arn required")
    if data.get("timeoutSeconds") is not None:
        out["timeout_seconds"] = data["timeoutSeconds"]
    else:
        out["timeout_seconds"] = 30
    if data.get("maxConcurrencyPerEnvironment") is not None:
        out["max_concurrency_per_environment"] = data["maxConcurrencyPerEnvironment"]
    else:
        out["max_concurrency_per_environment"] = 64
    if data.get("environmentVariables") is not None:
        import capo_lambda_web.types.environment_variables

        out["environment_variables"] = (
            capo_lambda_web.types.environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("telemetryConfig") is not None:
        import capo_lambda_web.types.telemetry_config

        out["telemetry_config"] = (
            capo_lambda_web.types.telemetry_config.deserialize_json(
                data["telemetryConfig"]
            )
        )
    return out
