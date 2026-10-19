"""Generated from Smithy shape ``com.amazonaws.quicksight#SnowflakeParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.authentication_type
    import capo_quicksight.types.database
    import capo_quicksight.types.database_access_control_role
    import capo_quicksight.types.host
    import capo_quicksight.types.o_auth_parameters
    import capo_quicksight.types.warehouse


class SnowflakeParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>Host.</p>"""
    database: "capo_quicksight.types.database.Database"
    """<p>Database.</p>"""
    warehouse: "capo_quicksight.types.warehouse.Warehouse"
    """<p>Warehouse.</p>"""
    authentication_type: NotRequired[
        "capo_quicksight.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.</p>"""
    database_access_control_role: NotRequired[
        "capo_quicksight.types.database_access_control_role.DatabaseAccessControlRole"
    ]
    """<p>The database access control role.</p>"""
    o_auth_parameters: NotRequired[
        "capo_quicksight.types.o_auth_parameters.OAuthParameters"
    ]
    """<p>An object that contains information needed to create a data source connection between an Quick Sight account and Snowflake.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Database"] = value["database"]
    out["Warehouse"] = value["warehouse"]
    if "authentication_type" in value:
        import capo_quicksight.types.authentication_type

        out["AuthenticationType"] = (
            capo_quicksight.types.authentication_type.serialize_json(
                value["authentication_type"]
            )
        )
    if "database_access_control_role" in value:
        out["DatabaseAccessControlRole"] = value["database_access_control_role"]
    if "o_auth_parameters" in value:
        import capo_quicksight.types.o_auth_parameters

        out["OAuthParameters"] = capo_quicksight.types.o_auth_parameters.serialize_json(
            value["o_auth_parameters"]
        )
    return out


def deserialize_json(data: dict) -> SnowflakeParameters:
    out: SnowflakeParameters = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        out["host"] = ""
    if data.get("Database") is not None:
        out["database"] = data["Database"]
    else:
        out["database"] = ""
    if data.get("Warehouse") is not None:
        out["warehouse"] = data["Warehouse"]
    else:
        out["warehouse"] = ""
    if data.get("AuthenticationType") is not None:
        import capo_quicksight.types.authentication_type

        out["authentication_type"] = (
            capo_quicksight.types.authentication_type.deserialize_json(
                data["AuthenticationType"]
            )
        )
    if data.get("DatabaseAccessControlRole") is not None:
        out["database_access_control_role"] = data["DatabaseAccessControlRole"]
    if data.get("OAuthParameters") is not None:
        import capo_quicksight.types.o_auth_parameters

        out["o_auth_parameters"] = (
            capo_quicksight.types.o_auth_parameters.deserialize_json(
                data["OAuthParameters"]
            )
        )
    return out
