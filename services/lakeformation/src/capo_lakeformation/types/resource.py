"""Generated from Smithy shape ``com.amazonaws.lakeformation#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.any_resource
    import capo_lakeformation.types.catalog_resource
    import capo_lakeformation.types.data_cells_filter_resource
    import capo_lakeformation.types.data_location_resource
    import capo_lakeformation.types.database_resource
    import capo_lakeformation.types.lf_tag_expression_resource
    import capo_lakeformation.types.lf_tag_key_resource
    import capo_lakeformation.types.lf_tag_policy_resource
    import capo_lakeformation.types.rls_policy_resource
    import capo_lakeformation.types.table_resource
    import capo_lakeformation.types.table_with_columns_resource
    import capo_lakeformation.types.user_defined_function_resource


class Resource(TypedDict, closed=True):
    any_resource: NotRequired["capo_lakeformation.types.any_resource.AnyResource"]
    """<p>All resources of the specified type in a Data Catalog. When you grant or revoke permissions on this resource, the principal must be a user-defined function whose <code>GovernanceMode</code> is <code>LAKE_FORMATION</code>, and the Data Catalog must be in your account.</p>"""
    catalog: NotRequired["capo_lakeformation.types.catalog_resource.CatalogResource"]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    database: NotRequired["capo_lakeformation.types.database_resource.DatabaseResource"]
    """<p>The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal. </p>"""
    table: NotRequired["capo_lakeformation.types.table_resource.TableResource"]
    """<p>The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal. </p>"""
    table_with_columns: NotRequired[
        "capo_lakeformation.types.table_with_columns_resource.TableWithColumnsResource"
    ]
    """<p>The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.</p>"""
    data_location: NotRequired[
        "capo_lakeformation.types.data_location_resource.DataLocationResource"
    ]
    """<p>The location of an Amazon S3 path where permissions are granted or revoked. </p>"""
    data_cells_filter: NotRequired[
        "capo_lakeformation.types.data_cells_filter_resource.DataCellsFilterResource"
    ]
    """<p>A data cell filter.</p>"""
    lf_tag: NotRequired["capo_lakeformation.types.lf_tag_key_resource.LFTagKeyResource"]
    """<p>The LF-Tag key and values attached to a resource.</p>"""
    lf_tag_policy: NotRequired[
        "capo_lakeformation.types.lf_tag_policy_resource.LFTagPolicyResource"
    ]
    """<p>A list of LF-tag conditions or saved LF-Tag expressions that define a resource's LF-tag policy.</p>"""
    lf_tag_expression: NotRequired[
        "capo_lakeformation.types.lf_tag_expression_resource.LFTagExpressionResource"
    ]
    """<p>LF-Tag expression resource. A logical expression composed of one or more LF-Tag key:value pairs.</p>"""
    rls_policy: NotRequired[
        "capo_lakeformation.types.rls_policy_resource.RLSPolicyResource"
    ]
    """<p>A row-level security policy resource. Specify this when granting or revoking permissions on a row-level security policy.</p>"""
    user_defined_function: NotRequired[
        "capo_lakeformation.types.user_defined_function_resource.UserDefinedFunctionResource"
    ]
    """<p>The user-defined function that you want to grant or revoke permissions on. The function's <code>GovernanceMode</code> must be <code>LAKE_FORMATION</code>. You can grant the following permissions:</p> <ul> <li> <p> <code>EXECUTE</code> – Use the function in a job, and get credentials to download its artifacts.</p> </li> <li> <p> <code>DESCRIBE</code> – View the function's definition.</p> </li> <li> <p> <code>ALTER</code> – Update the function.</p> </li> <li> <p> <code>DROP</code> – Delete the function.</p> </li> <li> <p> <code>ALL</code> – All of the preceding permissions.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "any_resource" in value:
        import capo_lakeformation.types.any_resource

        out["AnyResource"] = capo_lakeformation.types.any_resource.serialize_json(
            value["any_resource"]
        )
    if "catalog" in value:
        import capo_lakeformation.types.catalog_resource

        out["Catalog"] = capo_lakeformation.types.catalog_resource.serialize_json(
            value["catalog"]
        )
    if "database" in value:
        import capo_lakeformation.types.database_resource

        out["Database"] = capo_lakeformation.types.database_resource.serialize_json(
            value["database"]
        )
    if "table" in value:
        import capo_lakeformation.types.table_resource

        out["Table"] = capo_lakeformation.types.table_resource.serialize_json(
            value["table"]
        )
    if "table_with_columns" in value:
        import capo_lakeformation.types.table_with_columns_resource

        out["TableWithColumns"] = (
            capo_lakeformation.types.table_with_columns_resource.serialize_json(
                value["table_with_columns"]
            )
        )
    if "data_location" in value:
        import capo_lakeformation.types.data_location_resource

        out["DataLocation"] = (
            capo_lakeformation.types.data_location_resource.serialize_json(
                value["data_location"]
            )
        )
    if "data_cells_filter" in value:
        import capo_lakeformation.types.data_cells_filter_resource

        out["DataCellsFilter"] = (
            capo_lakeformation.types.data_cells_filter_resource.serialize_json(
                value["data_cells_filter"]
            )
        )
    if "lf_tag" in value:
        import capo_lakeformation.types.lf_tag_key_resource

        out["LFTag"] = capo_lakeformation.types.lf_tag_key_resource.serialize_json(
            value["lf_tag"]
        )
    if "lf_tag_policy" in value:
        import capo_lakeformation.types.lf_tag_policy_resource

        out["LFTagPolicy"] = (
            capo_lakeformation.types.lf_tag_policy_resource.serialize_json(
                value["lf_tag_policy"]
            )
        )
    if "lf_tag_expression" in value:
        import capo_lakeformation.types.lf_tag_expression_resource

        out["LFTagExpression"] = (
            capo_lakeformation.types.lf_tag_expression_resource.serialize_json(
                value["lf_tag_expression"]
            )
        )
    if "rls_policy" in value:
        import capo_lakeformation.types.rls_policy_resource

        out["RLSPolicy"] = capo_lakeformation.types.rls_policy_resource.serialize_json(
            value["rls_policy"]
        )
    if "user_defined_function" in value:
        import capo_lakeformation.types.user_defined_function_resource

        out["UserDefinedFunction"] = (
            capo_lakeformation.types.user_defined_function_resource.serialize_json(
                value["user_defined_function"]
            )
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("AnyResource") is not None:
        import capo_lakeformation.types.any_resource

        out["any_resource"] = capo_lakeformation.types.any_resource.deserialize_json(
            data["AnyResource"]
        )
    if data.get("Catalog") is not None:
        import capo_lakeformation.types.catalog_resource

        out["catalog"] = capo_lakeformation.types.catalog_resource.deserialize_json(
            data["Catalog"]
        )
    if data.get("Database") is not None:
        import capo_lakeformation.types.database_resource

        out["database"] = capo_lakeformation.types.database_resource.deserialize_json(
            data["Database"]
        )
    if data.get("Table") is not None:
        import capo_lakeformation.types.table_resource

        out["table"] = capo_lakeformation.types.table_resource.deserialize_json(
            data["Table"]
        )
    if data.get("TableWithColumns") is not None:
        import capo_lakeformation.types.table_with_columns_resource

        out["table_with_columns"] = (
            capo_lakeformation.types.table_with_columns_resource.deserialize_json(
                data["TableWithColumns"]
            )
        )
    if data.get("DataLocation") is not None:
        import capo_lakeformation.types.data_location_resource

        out["data_location"] = (
            capo_lakeformation.types.data_location_resource.deserialize_json(
                data["DataLocation"]
            )
        )
    if data.get("DataCellsFilter") is not None:
        import capo_lakeformation.types.data_cells_filter_resource

        out["data_cells_filter"] = (
            capo_lakeformation.types.data_cells_filter_resource.deserialize_json(
                data["DataCellsFilter"]
            )
        )
    if data.get("LFTag") is not None:
        import capo_lakeformation.types.lf_tag_key_resource

        out["lf_tag"] = capo_lakeformation.types.lf_tag_key_resource.deserialize_json(
            data["LFTag"]
        )
    if data.get("LFTagPolicy") is not None:
        import capo_lakeformation.types.lf_tag_policy_resource

        out["lf_tag_policy"] = (
            capo_lakeformation.types.lf_tag_policy_resource.deserialize_json(
                data["LFTagPolicy"]
            )
        )
    if data.get("LFTagExpression") is not None:
        import capo_lakeformation.types.lf_tag_expression_resource

        out["lf_tag_expression"] = (
            capo_lakeformation.types.lf_tag_expression_resource.deserialize_json(
                data["LFTagExpression"]
            )
        )
    if data.get("RLSPolicy") is not None:
        import capo_lakeformation.types.rls_policy_resource

        out["rls_policy"] = (
            capo_lakeformation.types.rls_policy_resource.deserialize_json(
                data["RLSPolicy"]
            )
        )
    if data.get("UserDefinedFunction") is not None:
        import capo_lakeformation.types.user_defined_function_resource

        out["user_defined_function"] = (
            capo_lakeformation.types.user_defined_function_resource.deserialize_json(
                data["UserDefinedFunction"]
            )
        )
    return out
