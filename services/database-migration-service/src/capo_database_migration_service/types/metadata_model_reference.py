"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MetadataModelReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class MetadataModelReference(TypedDict, closed=True):
    metadata_model_name: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The name of the metadata model.</p>"""
    selection_rules: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>A JSON string that identifies this metadata model in the metadata tree. For the selection rule format, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>You can pass this value as the <code>SelectionRules</code> parameter to any operation that accepts selection rules, such as <code>DescribeMetadataModel</code>, <code>StartMetadataModelConversion</code>, and others.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetadataModelReference) -> dict:
    out: dict = {}
    if "metadata_model_name" in value:
        out["MetadataModelName"] = value["metadata_model_name"]
    if "selection_rules" in value:
        out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetadataModelReference:
    out: MetadataModelReference = {}  # type: ignore[typeddict-item]
    if data.get("MetadataModelName") is not None:
        out["metadata_model_name"] = data["MetadataModelName"]
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    return out
