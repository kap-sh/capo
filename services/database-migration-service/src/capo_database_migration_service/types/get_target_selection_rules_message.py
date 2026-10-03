"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#GetTargetSelectionRulesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.string


class GetTargetSelectionRulesMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A JSON string that contains the source selection rules to convert into their target counterparts. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only source selection rules, where <code>server-name</code> in the object locator matches the source data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> <li> <p>Does not support <code>category-name</code> in the object locator.</p> </li> <li> <p>Up to 10 rules are allowed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTargetSelectionRulesMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTargetSelectionRulesMessage:
    out: GetTargetSelectionRulesMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "GetTargetSelectionRulesMessage.migration_project_identifier required"
        )
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "GetTargetSelectionRulesMessage.selection_rules required"
        )
    return out
