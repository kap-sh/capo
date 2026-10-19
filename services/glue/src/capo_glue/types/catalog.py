"""Generated from Smithy shape ``com.amazonaws.glue#Catalog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.allow_full_table_external_data_access_enum
    import capo_glue.types.catalog_id_string
    import capo_glue.types.catalog_name_string
    import capo_glue.types.catalog_properties_output
    import capo_glue.types.description_string
    import capo_glue.types.federated_catalog
    import capo_glue.types.parameters_map
    import capo_glue.types.principal_permissions_list
    import capo_glue.types.resource_arn_string
    import capo_glue.types.target_redshift_catalog
    import capo_glue.types.timestamp


class Catalog(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the catalog. To grant access to the default catalog, this field should not be provided.</p>"""
    name: "capo_glue.types.catalog_name_string.CatalogNameString"
    """<p>The name of the catalog. Cannot be the same as the account ID.</p>"""
    resource_arn: NotRequired["capo_glue.types.resource_arn_string.ResourceArnString"]
    """<p>The Amazon Resource Name (ARN) assigned to the catalog resource.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>Description string, not more than 2048 bytes long, matching the URI address multi-line string pattern. A description of the catalog.</p>"""
    parameters: NotRequired["capo_glue.types.parameters_map.ParametersMap"]
    """<p> A map array of key-value pairs that define parameters and properties of the catalog.</p>"""
    create_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the catalog was created.</p>"""
    update_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the catalog was last updated.</p>"""
    target_redshift_catalog: NotRequired[
        "capo_glue.types.target_redshift_catalog.TargetRedshiftCatalog"
    ]
    """<p>A <code>TargetRedshiftCatalog</code> object that describes a target catalog for database resource linking.</p>"""
    federated_catalog: NotRequired["capo_glue.types.federated_catalog.FederatedCatalog"]
    """<p>A <code>FederatedCatalog</code> object that points to an entity outside the Glue Data Catalog.</p>"""
    catalog_properties: NotRequired[
        "capo_glue.types.catalog_properties_output.CatalogPropertiesOutput"
    ]
    """<p>A <code>CatalogProperties</code> object that specifies data lake access properties and other custom properties.</p>"""
    create_table_default_permissions: NotRequired[
        "capo_glue.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>An array of <code>PrincipalPermissions</code> objects. Creates a set of default permissions on the table(s) for principals. Used by Amazon Web Services Lake Formation. Not used in the normal course of Glue operations.</p>"""
    create_database_default_permissions: NotRequired[
        "capo_glue.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>An array of <code>PrincipalPermissions</code> objects. Creates a set of default permissions on the database(s) for principals. Used by Amazon Web Services Lake Formation. Not used in the normal course of Glue operations.</p>"""
    allow_full_table_external_data_access: NotRequired[
        "capo_glue.types.allow_full_table_external_data_access_enum.AllowFullTableExternalDataAccessEnum"
    ]
    """<p> Allows third-party engines to access data in Amazon S3 locations that are registered with Lake Formation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Catalog) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "parameters" in value:
        import capo_glue.types.parameters_map

        out["Parameters"] = capo_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "create_time" in value:
        import capo_glue.types.timestamp

        out["CreateTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "update_time" in value:
        import capo_glue.types.timestamp

        out["UpdateTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["update_time"]
        )
    if "target_redshift_catalog" in value:
        import capo_glue.types.target_redshift_catalog

        out["TargetRedshiftCatalog"] = (
            capo_glue.types.target_redshift_catalog.serialize_aws_json_1_1(
                value["target_redshift_catalog"]
            )
        )
    if "federated_catalog" in value:
        import capo_glue.types.federated_catalog

        out["FederatedCatalog"] = (
            capo_glue.types.federated_catalog.serialize_aws_json_1_1(
                value["federated_catalog"]
            )
        )
    if "catalog_properties" in value:
        import capo_glue.types.catalog_properties_output

        out["CatalogProperties"] = (
            capo_glue.types.catalog_properties_output.serialize_aws_json_1_1(
                value["catalog_properties"]
            )
        )
    if "create_table_default_permissions" in value:
        import capo_glue.types.principal_permissions_list

        out["CreateTableDefaultPermissions"] = (
            capo_glue.types.principal_permissions_list.serialize_aws_json_1_1(
                value["create_table_default_permissions"]
            )
        )
    if "create_database_default_permissions" in value:
        import capo_glue.types.principal_permissions_list

        out["CreateDatabaseDefaultPermissions"] = (
            capo_glue.types.principal_permissions_list.serialize_aws_json_1_1(
                value["create_database_default_permissions"]
            )
        )
    if "allow_full_table_external_data_access" in value:
        import capo_glue.types.allow_full_table_external_data_access_enum

        out["AllowFullTableExternalDataAccess"] = (
            capo_glue.types.allow_full_table_external_data_access_enum.serialize_aws_json_1_1(
                value["allow_full_table_external_data_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Catalog:
    out: Catalog = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Parameters") is not None:
        import capo_glue.types.parameters_map

        out["parameters"] = capo_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if data.get("CreateTime") is not None:
        import capo_glue.types.timestamp

        out["create_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if data.get("UpdateTime") is not None:
        import capo_glue.types.timestamp

        out["update_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["UpdateTime"]
        )
    if data.get("TargetRedshiftCatalog") is not None:
        import capo_glue.types.target_redshift_catalog

        out["target_redshift_catalog"] = (
            capo_glue.types.target_redshift_catalog.deserialize_aws_json_1_1(
                data["TargetRedshiftCatalog"]
            )
        )
    if data.get("FederatedCatalog") is not None:
        import capo_glue.types.federated_catalog

        out["federated_catalog"] = (
            capo_glue.types.federated_catalog.deserialize_aws_json_1_1(
                data["FederatedCatalog"]
            )
        )
    if data.get("CatalogProperties") is not None:
        import capo_glue.types.catalog_properties_output

        out["catalog_properties"] = (
            capo_glue.types.catalog_properties_output.deserialize_aws_json_1_1(
                data["CatalogProperties"]
            )
        )
    if data.get("CreateTableDefaultPermissions") is not None:
        import capo_glue.types.principal_permissions_list

        out["create_table_default_permissions"] = (
            capo_glue.types.principal_permissions_list.deserialize_aws_json_1_1(
                data["CreateTableDefaultPermissions"]
            )
        )
    if data.get("CreateDatabaseDefaultPermissions") is not None:
        import capo_glue.types.principal_permissions_list

        out["create_database_default_permissions"] = (
            capo_glue.types.principal_permissions_list.deserialize_aws_json_1_1(
                data["CreateDatabaseDefaultPermissions"]
            )
        )
    if data.get("AllowFullTableExternalDataAccess") is not None:
        import capo_glue.types.allow_full_table_external_data_access_enum

        out["allow_full_table_external_data_access"] = (
            capo_glue.types.allow_full_table_external_data_access_enum.deserialize_aws_json_1_1(
                data["AllowFullTableExternalDataAccess"]
            )
        )
    return out
