"""Generated from Smithy shape ``com.amazonaws.lakeformation#UserDefinedFunctionResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.user_defined_function_wildcard


class UserDefinedFunctionResource(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The ID of the Data Catalog. By default, it's your account ID.</p>"""
    database_name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the database that contains the function.</p>"""
    name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>The name of the function.</p> <p>Exactly one of <code>UserDefinedFunctionResource$Name</code> or <code>UserDefinedFunctionResource$UserDefinedFunctionWildcard</code> is required.</p>"""
    user_defined_function_wildcard: NotRequired[
        "capo_lakeformation.types.user_defined_function_wildcard.UserDefinedFunctionWildcard"
    ]
    """<p>A wildcard object representing every user-defined function in the database, including functions created after the grant.</p> <p>Exactly one of <code>UserDefinedFunctionResource$Name</code> or <code>UserDefinedFunctionResource$UserDefinedFunctionWildcard</code> is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserDefinedFunctionResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "user_defined_function_wildcard" in value:
        import capo_lakeformation.types.user_defined_function_wildcard

        out["UserDefinedFunctionWildcard"] = (
            capo_lakeformation.types.user_defined_function_wildcard.serialize_json(
                value["user_defined_function_wildcard"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserDefinedFunctionResource:
    out: UserDefinedFunctionResource = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("UserDefinedFunctionWildcard") is not None:
        import capo_lakeformation.types.user_defined_function_wildcard

        out["user_defined_function_wildcard"] = (
            capo_lakeformation.types.user_defined_function_wildcard.deserialize_json(
                data["UserDefinedFunctionWildcard"]
            )
        )
    return out
