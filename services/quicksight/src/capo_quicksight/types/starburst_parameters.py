"""Generated from Smithy shape ``com.amazonaws.quicksight#StarburstParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.authentication_type
    import capo_quicksight.types.catalog
    import capo_quicksight.types.database_access_control_role
    import capo_quicksight.types.host
    import capo_quicksight.types.o_auth_parameters
    import capo_quicksight.types.port
    import capo_quicksight.types.starburst_product_type


class StarburstParameters(TypedDict, closed=True):
    host: "capo_quicksight.types.host.Host"
    """<p>The host name of the Starburst data source.</p>"""
    port: "capo_quicksight.types.port.Port"
    """<p>The port for the Starburst data source.</p>"""
    catalog: "capo_quicksight.types.catalog.Catalog"
    """<p>The catalog name for the Starburst data source.</p>"""
    product_type: NotRequired[
        "capo_quicksight.types.starburst_product_type.StarburstProductType"
    ]
    """<p>The product type for the Starburst data source.</p>"""
    database_access_control_role: NotRequired[
        "capo_quicksight.types.database_access_control_role.DatabaseAccessControlRole"
    ]
    """<p>The database access control role.</p>"""
    authentication_type: NotRequired[
        "capo_quicksight.types.authentication_type.AuthenticationType"
    ]
    """<p>The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.</p>"""
    o_auth_parameters: NotRequired[
        "capo_quicksight.types.o_auth_parameters.OAuthParameters"
    ]
    """<p>An object that contains information needed to create a data source connection between an Quick Sight account and Starburst.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StarburstParameters) -> dict:
    out: dict = {}
    out["Host"] = value["host"]
    out["Port"] = value["port"]
    out["Catalog"] = value["catalog"]
    if "product_type" in value:
        import capo_quicksight.types.starburst_product_type

        out["ProductType"] = (
            capo_quicksight.types.starburst_product_type.serialize_json(
                value["product_type"]
            )
        )
    if "database_access_control_role" in value:
        out["DatabaseAccessControlRole"] = value["database_access_control_role"]
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


def deserialize_json(data: dict) -> StarburstParameters:
    out: StarburstParameters = {}  # type: ignore[typeddict-item]
    if data.get("Host") is not None:
        out["host"] = data["Host"]
    else:
        out["host"] = ""
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ProductType") is not None:
        import capo_quicksight.types.starburst_product_type

        out["product_type"] = (
            capo_quicksight.types.starburst_product_type.deserialize_json(
                data["ProductType"]
            )
        )
    if data.get("DatabaseAccessControlRole") is not None:
        out["database_access_control_role"] = data["DatabaseAccessControlRole"]
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
