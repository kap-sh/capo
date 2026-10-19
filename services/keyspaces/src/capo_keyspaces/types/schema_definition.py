"""Generated from Smithy shape ``com.amazonaws.keyspaces#SchemaDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.clustering_key_list
    import capo_keyspaces.types.column_definition_list
    import capo_keyspaces.types.partition_key_list
    import capo_keyspaces.types.static_column_list


class SchemaDefinition(TypedDict, closed=True):
    all_columns: "capo_keyspaces.types.column_definition_list.ColumnDefinitionList"
    """<p>The regular columns of the table.</p>"""
    partition_keys: "capo_keyspaces.types.partition_key_list.PartitionKeyList"
    """<p>The columns that are part of the partition key of the table .</p>"""
    clustering_keys: NotRequired[
        "capo_keyspaces.types.clustering_key_list.ClusteringKeyList"
    ]
    """<p>The columns that are part of the clustering key of the table.</p>"""
    static_columns: NotRequired[
        "capo_keyspaces.types.static_column_list.StaticColumnList"
    ]
    """<p>The columns that have been defined as <code>STATIC</code>. Static columns store values that are shared by all rows in the same partition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SchemaDefinition) -> dict:
    out: dict = {}
    import capo_keyspaces.types.column_definition_list

    out["allColumns"] = (
        capo_keyspaces.types.column_definition_list.serialize_aws_json_1_0(
            value["all_columns"]
        )
    )
    import capo_keyspaces.types.partition_key_list

    out["partitionKeys"] = (
        capo_keyspaces.types.partition_key_list.serialize_aws_json_1_0(
            value["partition_keys"]
        )
    )
    if "clustering_keys" in value:
        import capo_keyspaces.types.clustering_key_list

        out["clusteringKeys"] = (
            capo_keyspaces.types.clustering_key_list.serialize_aws_json_1_0(
                value["clustering_keys"]
            )
        )
    if "static_columns" in value:
        import capo_keyspaces.types.static_column_list

        out["staticColumns"] = (
            capo_keyspaces.types.static_column_list.serialize_aws_json_1_0(
                value["static_columns"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SchemaDefinition:
    out: SchemaDefinition = {}  # type: ignore[typeddict-item]
    if data.get("allColumns") is not None:
        import capo_keyspaces.types.column_definition_list

        out["all_columns"] = (
            capo_keyspaces.types.column_definition_list.deserialize_aws_json_1_0(
                data["allColumns"]
            )
        )
    else:
        out["all_columns"] = []
    if data.get("partitionKeys") is not None:
        import capo_keyspaces.types.partition_key_list

        out["partition_keys"] = (
            capo_keyspaces.types.partition_key_list.deserialize_aws_json_1_0(
                data["partitionKeys"]
            )
        )
    else:
        out["partition_keys"] = []
    if data.get("clusteringKeys") is not None:
        import capo_keyspaces.types.clustering_key_list

        out["clustering_keys"] = (
            capo_keyspaces.types.clustering_key_list.deserialize_aws_json_1_0(
                data["clusteringKeys"]
            )
        )
    if data.get("staticColumns") is not None:
        import capo_keyspaces.types.static_column_list

        out["static_columns"] = (
            capo_keyspaces.types.static_column_list.deserialize_aws_json_1_0(
                data["staticColumns"]
            )
        )
    return out
