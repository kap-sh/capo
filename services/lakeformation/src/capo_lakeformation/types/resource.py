"""Generated from Smithy shape ``com.amazonaws.lakeformation#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_resource
    import capo_lakeformation.types.data_cells_filter_resource
    import capo_lakeformation.types.data_location_resource
    import capo_lakeformation.types.database_resource
    import capo_lakeformation.types.lf_tag_expression_resource
    import capo_lakeformation.types.lf_tag_key_resource
    import capo_lakeformation.types.lf_tag_policy_resource
    import capo_lakeformation.types.table_resource
    import capo_lakeformation.types.table_with_columns_resource


class Resource(TypedDict, closed=True):
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


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
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
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
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
    return out
