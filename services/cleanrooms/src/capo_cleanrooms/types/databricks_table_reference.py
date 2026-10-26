"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DatabricksTableReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.databricks_connection_type
    import capo_cleanrooms.types.databricks_object
    import capo_cleanrooms.types.databricks_workspace_url


class DatabricksTableReference(TypedDict, closed=True):
    schema_name: "capo_cleanrooms.types.databricks_object.DatabricksObject"
    """<p>Name of the Schema within Databricks.</p>"""
    table_name: "capo_cleanrooms.types.databricks_object.DatabricksObject"
    """<p>Name of the Table within Databricks.</p>"""
    workspace_url: (
        "capo_cleanrooms.types.databricks_workspace_url.DatabricksWorkspaceUrl"
    )
    """<p>URL for the Databricks Workspace.</p>"""
    connection_type: (
        "capo_cleanrooms.types.databricks_connection_type.DatabricksConnectionType"
    )
    """<p>Type of the connector to be used for connecting to Databricks. Supported connector: Delta Sharing</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabricksTableReference) -> dict:
    out: dict = {}
    out["schemaName"] = value["schema_name"]
    out["tableName"] = value["table_name"]
    out["workspaceUrl"] = value["workspace_url"]
    import capo_cleanrooms.types.databricks_connection_type

    out["connectionType"] = (
        capo_cleanrooms.types.databricks_connection_type.serialize_json(
            value["connection_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> DatabricksTableReference:
    out: DatabricksTableReference = {}  # type: ignore[typeddict-item]
    if data.get("schemaName") is not None:
        out["schema_name"] = data["schemaName"]
    else:
        out["schema_name"] = ""
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("workspaceUrl") is not None:
        out["workspace_url"] = data["workspaceUrl"]
    else:
        out["workspace_url"] = ""
    if data.get("connectionType") is not None:
        import capo_cleanrooms.types.databricks_connection_type

        out["connection_type"] = (
            capo_cleanrooms.types.databricks_connection_type.deserialize_json(
                data["connectionType"]
            )
        )
    else:
        out["connection_type"] = {"$unknown": {"name": ""}}
    return out
