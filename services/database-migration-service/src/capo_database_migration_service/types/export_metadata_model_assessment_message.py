"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ExportMetadataModelAssessmentMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.assessment_report_types_list
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.string


class ExportMetadataModelAssessmentMessage(TypedDict, closed=True):
    migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier"
    """<p>The migration project name or Amazon Resource Name (ARN).</p>"""
    selection_rules: "capo_database_migration_service.types.string.String"
    """<p>A JSON string that identifies the metadata models to export a conversion assessment report for. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only source selection rules, where <code>server-name</code> in the object locator matches the source data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> </ul>"""
    file_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name of the assessment file to create in your Amazon S3 bucket.</p>"""
    assessment_report_types: NotRequired[
        "capo_database_migration_service.types.assessment_report_types_list.AssessmentReportTypesList"
    ]
    """<p>The file format of the assessment file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportMetadataModelAssessmentMessage) -> dict:
    out: dict = {}
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    out["SelectionRules"] = value["selection_rules"]
    if "file_name" in value:
        out["FileName"] = value["file_name"]
    if "assessment_report_types" in value:
        import capo_database_migration_service.types.assessment_report_types_list

        out["AssessmentReportTypes"] = (
            capo_database_migration_service.types.assessment_report_types_list.serialize_aws_json_1_1(
                value["assessment_report_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportMetadataModelAssessmentMessage:
    out: ExportMetadataModelAssessmentMessage = {}  # type: ignore[typeddict-item]
    if data.get("MigrationProjectIdentifier") is not None:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "ExportMetadataModelAssessmentMessage.migration_project_identifier required"
        )
    if data.get("SelectionRules") is not None:
        out["selection_rules"] = data["SelectionRules"]
    else:
        raise DeserializationError(
            "ExportMetadataModelAssessmentMessage.selection_rules required"
        )
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    if data.get("AssessmentReportTypes") is not None:
        import capo_database_migration_service.types.assessment_report_types_list

        out["assessment_report_types"] = (
            capo_database_migration_service.types.assessment_report_types_list.deserialize_aws_json_1_1(
                data["AssessmentReportTypes"]
            )
        )
    return out
