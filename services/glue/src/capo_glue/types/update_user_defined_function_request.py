"""Generated from Smithy shape ``com.amazonaws.glue#UpdateUserDefinedFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.user_defined_function_input


class UpdateUserDefinedFunctionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the function to be updated is located. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the function to be updated is located.</p>"""
    function_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the function.</p>"""
    function_input: (
        "capo_glue.types.user_defined_function_input.UserDefinedFunctionInput"
    )
    """<p>A <code>FunctionInput</code> object that redefines the function in the Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserDefinedFunctionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["FunctionName"] = value["function_name"]
    import capo_glue.types.user_defined_function_input

    out["FunctionInput"] = (
        capo_glue.types.user_defined_function_input.serialize_aws_json_1_1(
            value["function_input"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserDefinedFunctionRequest:
    out: UpdateUserDefinedFunctionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("FunctionName") is not None:
        out["function_name"] = data["FunctionName"]
    else:
        out["function_name"] = ""
    if data.get("FunctionInput") is not None:
        import capo_glue.types.user_defined_function_input

        out["function_input"] = (
            capo_glue.types.user_defined_function_input.deserialize_aws_json_1_1(
                data["FunctionInput"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateUserDefinedFunctionRequest.function_input required"
        )
    return out
