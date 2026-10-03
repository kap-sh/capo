"""Generated from Smithy shape ``com.amazonaws.appsync#GetGraphqlApiEnvironmentVariablesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.environment_variable_map


class GetGraphqlApiEnvironmentVariablesResponse(TypedDict, closed=True):
    environment_variables: NotRequired[
        "capo_appsync.types.environment_variable_map.EnvironmentVariableMap"
    ]
    """<p>The payload containing each environmental variable in the <code>"key" : "value"</code> format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphqlApiEnvironmentVariablesResponse) -> dict:
    out: dict = {}
    if "environment_variables" in value:
        import capo_appsync.types.environment_variable_map

        out["environmentVariables"] = (
            capo_appsync.types.environment_variable_map.serialize_json(
                value["environment_variables"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGraphqlApiEnvironmentVariablesResponse:
    out: GetGraphqlApiEnvironmentVariablesResponse = {}  # type: ignore[typeddict-item]
    if data.get("environmentVariables") is not None:
        import capo_appsync.types.environment_variable_map

        out["environment_variables"] = (
            capo_appsync.types.environment_variable_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    return out
