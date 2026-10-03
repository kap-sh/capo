"""Generated from Smithy shape ``com.amazonaws.lambda#Environment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.environment_variables


class Environment(TypedDict, closed=True):
    variables: NotRequired[
        "capo_lambda.types.environment_variables.EnvironmentVariables"
    ]
    """<p>Environment variable key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html">Using Lambda environment variables</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Environment) -> dict:
    out: dict = {}
    if "variables" in value:
        import capo_lambda.types.environment_variables

        out["Variables"] = capo_lambda.types.environment_variables.serialize_json(
            value["variables"]
        )
    return out


def deserialize_json(data: dict) -> Environment:
    out: Environment = {}  # type: ignore[typeddict-item]
    if data.get("Variables") is not None:
        import capo_lambda.types.environment_variables

        out["variables"] = capo_lambda.types.environment_variables.deserialize_json(
            data["Variables"]
        )
    return out
