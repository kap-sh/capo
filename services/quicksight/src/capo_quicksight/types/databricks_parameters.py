"""Generated from Smithy shape ``com.amazonaws.quicksight#DatabricksParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.authentication_type
    import capo_quicksight.types.host
    import capo_quicksight.types.o_auth_parameters
    import capo_quicksight.types.port
    import capo_quicksight.types.sql_endpoint_path


class DatabricksParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>The host name of the Databricks data source.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>The port for the Databricks data source.</p>"""
    sql_endpoint_path: "capo_quicksight.types.sql_endpoint_path.SqlEndpointPath"
    """<p>The HTTP path of the Databricks data source.</p>"""
    authentication_type: NotRequired[
        "capo_quicksight.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.</p>"""
    o_auth_parameters: NotRequired[
        "capo_quicksight.types.o_auth_parameters.OAuthParameters"
    ]
    """<p>An object that contains information needed to create a data source connection between an Quick Sight account and Databricks.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabricksParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["SqlEndpointPath"] = value["sql_endpoint_path"]
    if "authentication_type" in value:
        import capo_quicksight.types.authentication_type

        out["AuthenticationType"] = (
            capo_quicksight.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "o_auth_parameters" in value:
        import capo_quicksight.types.o_auth_parameters

        out["OAuthParameters"] = capo_quicksight.types.o_auth_parameters.serialize_json(
            value["o_auth_parameters"]
        )
    return out


def deserialize_json(data: dict) -> DatabricksParameters:
    out: DatabricksParameters = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        raise DeserializationError("DatabricksParameters.host required")
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("DatabricksParameters.port required")
    if data.get("SqlEndpointPath") is not None:
        out["sql_endpoint_path"] = data["SqlEndpointPath"]
    else:
        raise DeserializationError("DatabricksParameters.sql_endpoint_path required")
    if data.get("AuthenticationType") is not None:
        import capo_quicksight.types.authentication_type

        out["authentication_type"] = (
            capo_quicksight.types.authentication_type.deserialize_json(
                data["AuthenticationType"]
            )
        )
    if data.get("OAuthParameters") is not None:
        import capo_quicksight.types.o_auth_parameters

        out["o_auth_parameters"] = (
            capo_quicksight.types.o_auth_parameters.deserialize_json(
                data["OAuthParameters"]
            )
        )
    return out
