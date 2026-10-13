"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAnalysisDefinitionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_definition
    import capo_quicksight.types.analysis_error_list
    import capo_quicksight.types.analysis_name
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeAnalysisDefinitionResponse(TypedDict, closed=True):
    analysis_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis described.</p>"""
    name: NotRequired["capo_quicksight.types.analysis_name.AnalysisName"]
    """<p>The descriptive name of the analysis.</p>"""
    errors: NotRequired["capo_quicksight.types.analysis_error_list.AnalysisErrorList"]
    """<p>Errors associated with the analysis.</p>"""
    resource_status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>Status associated with the analysis.</p> <ul> <li> <p> <code>CREATION_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATION_SUCCESSFUL</code> </p> </li> <li> <p> <code>CREATION_FAILED</code> </p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> </p> </li> <li> <p> <code>UPDATE_FAILED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme of the analysis.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.analysis_definition.AnalysisDefinition"
    ]
    """<p>The definition of an analysis.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnalysisDefinitionResponse) -> dict:
    out: dict = {}
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "errors" in value:
        import capo_quicksight.types.analysis_error_list

        out["Errors"] = capo_quicksight.types.analysis_error_list.serialize_json(
            value["errors"]
        )
    if "resource_status" in value:
        import capo_quicksight.types.resource_status

        out["ResourceStatus"] = capo_quicksight.types.resource_status.serialize_json(
            value["resource_status"]
        )
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "definition" in value:
        import capo_quicksight.types.analysis_definition

        out["Definition"] = capo_quicksight.types.analysis_definition.serialize_json(
            value["definition"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAnalysisDefinitionResponse:
    out: DescribeAnalysisDefinitionResponse = {}  # type: ignore[typeddict-item]
    if data.get("AnalysisId") is not None:
        out["analysis_id"] = data["AnalysisId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Errors") is not None:
        import capo_quicksight.types.analysis_error_list

        out["errors"] = capo_quicksight.types.analysis_error_list.deserialize_json(
            data["Errors"]
        )
    if data.get("ResourceStatus") is not None:
        import capo_quicksight.types.resource_status

        out["resource_status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["ResourceStatus"]
        )
    if data.get("ThemeArn") is not None:
        out["theme_arn"] = data["ThemeArn"]
    if data.get("Definition") is not None:
        import capo_quicksight.types.analysis_definition

        out["definition"] = capo_quicksight.types.analysis_definition.deserialize_json(
            data["Definition"]
        )
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeAnalysisDefinitionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "definition" in value:
        import capo_quicksight.types.analysis_definition

        out["definition"] = capo_quicksight.types.analysis_definition.redact_sensitive(
            value["definition"]
        )
    return out
