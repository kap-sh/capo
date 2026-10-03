"""Generated from Smithy shape ``com.amazonaws.appsync#PutGraphqlApiEnvironmentVariablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.environment_variable_map
    import capo_appsync.types.string


class PutGraphqlApiEnvironmentVariablesRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The ID of the API to which the environmental variable list will be written.</p>"""
    environment_variables: (
        "capo_appsync.types.environment_variable_map.EnvironmentVariableMap"
    )
    """<p>The list of environmental variables to add to the API.</p> <p>When creating an environmental variable key-value pair, it must follow the additional constraints below:</p> <ul> <li> <p>Keys must begin with a letter.</p> </li> <li> <p>Keys must be at least two characters long.</p> </li> <li> <p>Keys can only contain letters, numbers, and the underscore character (_).</p> </li> <li> <p>Values can be up to 512 characters long.</p> </li> <li> <p>You can configure up to 50 key-value pairs in a GraphQL API.</p> </li> </ul> <p>You can create a list of environmental variables by adding it to the <code>environmentVariables</code> payload as a list in the format <code>{"key1":"value1","key2":"value2", …}</code>. Note that each call of the <code>PutGraphqlApiEnvironmentVariables</code> action will result in the overwriting of the existing environmental variable list of that API. This means the existing environmental variables will be lost. To avoid this, you must include all existing and new environmental variables in the list each time you call this action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutGraphqlApiEnvironmentVariablesRequest) -> dict:
    out: dict = {}
    import capo_appsync.types.environment_variable_map

    out["environmentVariables"] = (
        capo_appsync.types.environment_variable_map.serialize_json(
            value["environment_variables"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutGraphqlApiEnvironmentVariablesRequest:
    out: PutGraphqlApiEnvironmentVariablesRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentVariables") is not None:
        import capo_appsync.types.environment_variable_map

        out["environment_variables"] = (
            capo_appsync.types.environment_variable_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    else:
        raise DeserializationError(
            "PutGraphqlApiEnvironmentVariablesRequest.environment_variables required"
        )
    return out
