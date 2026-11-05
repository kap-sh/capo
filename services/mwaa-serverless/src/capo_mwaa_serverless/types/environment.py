"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#Environment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.environment_variables_map


class Environment(TypedDict, closed=True):
    variables: NotRequired[
        "capo_mwaa_serverless.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>A map of environment variable names to values. Your workflow tasks use these variables while they run. You can specify up to 50 environment variables. Each name must be between 1 and 128 characters, start with a letter, and contain only letters, numbers, and underscores. Each value can be up to 255 characters.</p> <p>Names that start with <code>AWS_</code> or <code>AIRFLOW__</code> are reserved. You can use the following Apache Airflow secrets backend settings, which are exceptions:</p> <ul> <li> <p> <code>AIRFLOW__WORKERS__SECRETS_BACKEND</code> – The secrets backend class that workers use.</p> </li> <li> <p> <code>AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS</code> – The keyword arguments for the secrets backend, as a JSON string.</p> </li> <li> <p> <code>AIRFLOW__WORKERS__SECRETS_BACKEND_KWARG__*</code> – Names with this prefix, for additional secrets backend configuration.</p> </li> </ul> <p>If you set <code>EncryptionConfiguration</code> to use a customer managed AWS KMS key, we encrypt the environment variables with that key. Otherwise, we store them with default encryption at rest.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Environment) -> dict:
    out: dict = {}
    if "variables" in value:
        import capo_mwaa_serverless.types.environment_variables_map

        out["Variables"] = (
            capo_mwaa_serverless.types.environment_variables_map.serialize_aws_json_1_0(
                value["variables"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if data.get("Variables") is not None:
        import capo_mwaa_serverless.types.environment_variables_map

        out["variables"] = (
            capo_mwaa_serverless.types.environment_variables_map.deserialize_aws_json_1_0(
                data["Variables"]
            )
        )
    return out


def redact_sensitive(value: Environment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "variables" in value:
        import capo_mwaa_serverless.types.environment_variables_map

        out["variables"] = (
            capo_mwaa_serverless.types.environment_variables_map.redact_sensitive(
                value["variables"]
            )
        )
    return out
