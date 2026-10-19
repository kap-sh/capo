"""Generated from Smithy shape ``com.amazonaws.keyspaces#GetTypeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.arn
    import capo_keyspaces.types.depth
    import capo_keyspaces.types.field_list
    import capo_keyspaces.types.keyspace_name
    import capo_keyspaces.types.table_name_list
    import capo_keyspaces.types.timestamp
    import capo_keyspaces.types.type_name
    import capo_keyspaces.types.type_name_list
    import capo_keyspaces.types.type_status


class GetTypeResponse(TypedDict, closed=True):
    keyspace_name: "capo_keyspaces.types.keyspace_name.KeyspaceName"
    """<p> The name of the keyspace that contains this type. </p>"""
    type_name: "capo_keyspaces.types.type_name.TypeName"
    """<p> The name of the type. </p>"""
    field_definitions: NotRequired["capo_keyspaces.types.field_list.FieldList"]
    """<p> The names and types that define this type. </p>"""
    last_modified_timestamp: NotRequired["capo_keyspaces.types.timestamp.Timestamp"]
    """<p> The timestamp that shows when this type was last modified. </p>"""
    status: NotRequired["capo_keyspaces.types.type_status.TypeStatus"]
    """<p> The status of this type. </p>"""
    direct_referring_tables: NotRequired[
        "capo_keyspaces.types.table_name_list.TableNameList"
    ]
    """<p> The tables that use this type. </p>"""
    direct_parent_types: NotRequired["capo_keyspaces.types.type_name_list.TypeNameList"]
    """<p> The types that use this type. </p>"""
    max_nesting_depth: "capo_keyspaces.types.depth.Depth"
    """<p> The level of nesting implemented for this type. </p>"""
    keyspace_arn: "capo_keyspaces.types.arn.ARN"
    """<p> The unique identifier of the keyspace that contains this type in the format of an Amazon Resource Name (ARN). </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTypeResponse) -> dict:
    out: dict = {}
    out["keyspaceName"] = value["keyspace_name"]
    out["typeName"] = value["type_name"]
    if "field_definitions" in value:
        import capo_keyspaces.types.field_list

        out["fieldDefinitions"] = (
            capo_keyspaces.types.field_list.serialize_aws_json_1_0(
                value["field_definitions"]
            )
        )
    if "last_modified_timestamp" in value:
        import capo_keyspaces.types.timestamp

        out["lastModifiedTimestamp"] = (
            capo_keyspaces.types.timestamp.serialize_aws_json_1_0(
                value["last_modified_timestamp"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "direct_referring_tables" in value:
        import capo_keyspaces.types.table_name_list

        out["directReferringTables"] = (
            capo_keyspaces.types.table_name_list.serialize_aws_json_1_0(
                value["direct_referring_tables"]
            )
        )
    if "direct_parent_types" in value:
        import capo_keyspaces.types.type_name_list

        out["directParentTypes"] = (
            capo_keyspaces.types.type_name_list.serialize_aws_json_1_0(
                value["direct_parent_types"]
            )
        )
    out["maxNestingDepth"] = value.get("max_nesting_depth", 0)
    out["keyspaceArn"] = value["keyspace_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTypeResponse:
    out: GetTypeResponse = {}  # type: ignore[typeddict-item]
    if data.get("keyspaceName") is not None:
        out["keyspace_name"] = data["keyspaceName"]
    else:
        out["keyspace_name"] = ""
    if data.get("typeName") is not None:
        out["type_name"] = data["typeName"]
    else:
        out["type_name"] = ""
    if data.get("fieldDefinitions") is not None:
        import capo_keyspaces.types.field_list

        out["field_definitions"] = (
            capo_keyspaces.types.field_list.deserialize_aws_json_1_0(
                data["fieldDefinitions"]
            )
        )
    if data.get("lastModifiedTimestamp") is not None:
        import capo_keyspaces.types.timestamp

        out["last_modified_timestamp"] = (
            capo_keyspaces.types.timestamp.deserialize_aws_json_1_0(
                data["lastModifiedTimestamp"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("directReferringTables") is not None:
        import capo_keyspaces.types.table_name_list

        out["direct_referring_tables"] = (
            capo_keyspaces.types.table_name_list.deserialize_aws_json_1_0(
                data["directReferringTables"]
            )
        )
    if data.get("directParentTypes") is not None:
        import capo_keyspaces.types.type_name_list

        out["direct_parent_types"] = (
            capo_keyspaces.types.type_name_list.deserialize_aws_json_1_0(
                data["directParentTypes"]
            )
        )
    if data.get("maxNestingDepth") is not None:
        out["max_nesting_depth"] = data["maxNestingDepth"]
    else:
        out["max_nesting_depth"] = 0
    if data.get("keyspaceArn") is not None:
        out["keyspace_arn"] = data["keyspaceArn"]
    else:
        out["keyspace_arn"] = ""
    return out
