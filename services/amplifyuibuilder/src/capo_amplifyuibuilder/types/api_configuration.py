"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ApiConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_amplifyuibuilder.errors import DeserializationError, SerializationError
from capo_amplifyuibuilder.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.data_store_render_config
    import capo_amplifyuibuilder.types.graph_ql_render_config
    import capo_amplifyuibuilder.types.no_api_render_config


class _ApiConfiguration_graphQLConfig(TypedDict, closed=True):
    graphQLConfig: (
        "capo_amplifyuibuilder.types.graph_ql_render_config.GraphQLRenderConfig"
    )


class _ApiConfiguration_dataStoreConfig(TypedDict, closed=True):
    dataStoreConfig: (
        "capo_amplifyuibuilder.types.data_store_render_config.DataStoreRenderConfig"
    )


class _ApiConfiguration_noApiConfig(TypedDict, closed=True):
    noApiConfig: "capo_amplifyuibuilder.types.no_api_render_config.NoApiRenderConfig"


ApiConfiguration: TypeAlias = (
    _ApiConfiguration_graphQLConfig
    | _ApiConfiguration_dataStoreConfig
    | _ApiConfiguration_noApiConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ApiConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ApiConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "graphQLConfig" in value:
        import capo_amplifyuibuilder.types.graph_ql_render_config

        return {
            "graphQLConfig": capo_amplifyuibuilder.types.graph_ql_render_config.serialize_json(
                value["graphQLConfig"]
            )
        }
    elif "dataStoreConfig" in value:
        import capo_amplifyuibuilder.types.data_store_render_config

        return {
            "dataStoreConfig": capo_amplifyuibuilder.types.data_store_render_config.serialize_json(
                value["dataStoreConfig"]
            )
        }
    elif "noApiConfig" in value:
        import capo_amplifyuibuilder.types.no_api_render_config

        return {
            "noApiConfig": capo_amplifyuibuilder.types.no_api_render_config.serialize_json(
                value["noApiConfig"]
            )
        }
    else:
        raise SerializationError("ApiConfiguration: no variant present")


def deserialize_json(data: dict) -> ApiConfiguration:
    if data.get("graphQLConfig") is not None:
        import capo_amplifyuibuilder.types.graph_ql_render_config

        return {
            "graphQLConfig": capo_amplifyuibuilder.types.graph_ql_render_config.deserialize_json(
                data["graphQLConfig"]
            )
        }
    elif data.get("dataStoreConfig") is not None:
        import capo_amplifyuibuilder.types.data_store_render_config

        return {
            "dataStoreConfig": capo_amplifyuibuilder.types.data_store_render_config.deserialize_json(
                data["dataStoreConfig"]
            )
        }
    elif data.get("noApiConfig") is not None:
        import capo_amplifyuibuilder.types.no_api_render_config

        return {
            "noApiConfig": capo_amplifyuibuilder.types.no_api_render_config.deserialize_json(
                data["noApiConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ApiConfiguration: no recognized variant key")
