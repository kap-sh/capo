"""Generated from Smithy shape ``com.amazonaws.glue#DatabaseInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.database_identifier
    import capo_glue.types.description_string
    import capo_glue.types.federated_database
    import capo_glue.types.name_string
    import capo_glue.types.parameters_map
    import capo_glue.types.principal_permissions_list
    import capo_glue.types.uri


class DatabaseInput(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.</p>"""
    description: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>A description of the database.</p>"""
    location_uri: NotRequired["capo_glue.types.uri.URI"]
    """<p>The location of the database (for example, an HDFS path). </p>"""
    parameters: NotRequired["capo_glue.types.parameters_map.ParametersMap"]
    """<p>These key-value pairs define parameters and properties of the database.</p> <p>These key-value pairs define parameters and properties of the database.</p>"""
    create_table_default_permissions: NotRequired[
        "capo_glue.types.principal_permissions_list.PrincipalPermissionsList"
    ]
    """<p>Creates a set of default permissions on the table for principals. Used by Lake Formation. Not used in the normal course of Glue operations.</p>"""
    target_database: NotRequired[
        "capo_glue.types.database_identifier.DatabaseIdentifier"
    ]
    """<p>A <code>DatabaseIdentifier</code> structure that describes a target database for resource linking.</p>"""
    federated_database: NotRequired[
        "capo_glue.types.federated_database.FederatedDatabase"
    ]
    """<p>A <code>FederatedDatabase</code> structure that references an entity outside the Glue Data Catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "parameters" in value:
        import capo_glue.types.parameters_map

        out["Parameters"] = capo_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "create_table_default_permissions" in value:
        import capo_glue.types.principal_permissions_list

        out["CreateTableDefaultPermissions"] = (
            capo_glue.types.principal_permissions_list.serialize_aws_json_1_1(
                value["create_table_default_permissions"]
            )
        )
    if "target_database" in value:
        import capo_glue.types.database_identifier

        out["TargetDatabase"] = (
            capo_glue.types.database_identifier.serialize_aws_json_1_1(
                value["target_database"]
            )
        )
    if "federated_database" in value:
        import capo_glue.types.federated_database

        out["FederatedDatabase"] = (
            capo_glue.types.federated_database.serialize_aws_json_1_1(
                value["federated_database"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseInput:
    out: DatabaseInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("Parameters") is not None:
        import capo_glue.types.parameters_map

        out["parameters"] = capo_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if data.get("CreateTableDefaultPermissions") is not None:
        import capo_glue.types.principal_permissions_list

        out["create_table_default_permissions"] = (
            capo_glue.types.principal_permissions_list.deserialize_aws_json_1_1(
                data["CreateTableDefaultPermissions"]
            )
        )
    if data.get("TargetDatabase") is not None:
        import capo_glue.types.database_identifier

        out["target_database"] = (
            capo_glue.types.database_identifier.deserialize_aws_json_1_1(
                data["TargetDatabase"]
            )
        )
    if data.get("FederatedDatabase") is not None:
        import capo_glue.types.federated_database

        out["federated_database"] = (
            capo_glue.types.federated_database.deserialize_aws_json_1_1(
                data["FederatedDatabase"]
            )
        )
    return out
