"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeMetadataModelChildrenMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.origin_type_value
    import capo_database_migration_service.types.string


class DescribeMetadataModelChildrenMessage(TypedDict, closed=True):
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A JSON string that identifies the metadata model whose children to retrieve. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts source or target selection rules depending on the <code>Origin</code> parameter. The <code>server-name</code> in the object locator must match the corresponding data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> <li> <p>Exactly one rule is allowed.</p> </li> </ul>"""
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue"
    """<p>Specifies whether to retrieve metadata from the source or target tree. Valid values: SOURCE | TARGET</p>"""
    marker: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Specifies the unique pagination token that indicates where the next page should start. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>"""
    max_records: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum number of metadata model children to include in the response. If more items exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMetadataModelChildrenMessage) -> dict:
    out: dict = {}
    out["SelectionRules"] = value["selection_rules"]
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    import capo_database_migration_service.types.origin_type_value

    out["Origin"] = (
        capo_database_migration_service.types.origin_type_value.serialize_aws_json_1_1(
            value["origin"]
        )
    )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMetadataModelChildrenMessage:
    out: DescribeMetadataModelChildrenMessage = {}  # type: ignore[typeddict-item]
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "DescribeMetadataModelChildrenMessage.selection_rules required"
        )
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "DescribeMetadataModelChildrenMessage.migration_project_identifier required"
        )
    if data.get("Origin") is not None:
        import capo_database_migration_service.types.origin_type_value

        out["origin"] = (
            capo_database_migration_service.types.origin_type_value.deserialize_aws_json_1_1(
                data["Origin"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeMetadataModelChildrenMessage.origin required"
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxRecords") is not None:
        out["max_records"] = data["MaxRecords"]
    return out
