"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAnalysisRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_definition
    import capo_quicksight.types.analysis_name
    import capo_quicksight.types.analysis_source_entity
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.folder_arn_list
    import capo_quicksight.types.parameters
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.tag_list
    import capo_quicksight.types.validation_strategy


class CreateAnalysisRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account where you are creating an analysis.</p>"""
    analysis_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the analysis that you're creating. This ID displays in the URL of the analysis.</p>"""
    name: "capo_quicksight.types.analysis_name.AnalysisName"
    """<p>A descriptive name for the analysis that you're creating. This name displays for the analysis in the Amazon Quick Sight console. </p>"""
    parameters: NotRequired["capo_quicksight.types.parameters.Parameters"]
    """<p>The parameter names and override values that you want to use. An analysis can have any parameter type, and some parameters might accept multiple values. </p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A structure that describes the principals and the resource-level permissions on an analysis. You can use the <code>Permissions</code> structure to grant permissions by providing a list of Identity and Access Management (IAM) action information for each principal listed by Amazon Resource Name (ARN). </p> <p>To specify no permissions, omit <code>Permissions</code>.</p>"""
    source_entity: NotRequired[
        "capo_quicksight.types.analysis_source_entity.AnalysisSourceEntity"
    ]
    """<p>A source entity to use for the analysis that you're creating. This metadata structure contains details that describe a source template and one or more datasets or topics.</p> <p>Either a <code>SourceEntity</code> or a <code>Definition</code> must be provided in order for the request to be valid.</p>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN for the theme to apply to the analysis that you're creating. To see the theme in the Amazon Quick Sight console, make sure that you have access to it.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>Contains a map of the key-value pairs for the resource tag or tags assigned to the analysis.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.analysis_definition.AnalysisDefinition"
    ]
    """<p>The definition of an analysis.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p> <p>Either a <code>SourceEntity</code> or a <code>Definition</code> must be provided in order for the request to be valid.</p>"""
    validation_strategy: NotRequired[
        "capo_quicksight.types.validation_strategy.ValidationStrategy"
    ]
    """<p>The option to relax the validation needed to create an analysis with definition objects. This skips the validation step for specific errors.</p>"""
    folder_arns: NotRequired["capo_quicksight.types.folder_arn_list.FolderArnList"]
    """<p>When you create the analysis, Amazon Quick Sight adds the analysis to these folders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalysisRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "parameters" in value:
        import capo_quicksight.types.parameters

        out["Parameters"] = capo_quicksight.types.parameters.serialize_json(
            value["parameters"]
        )
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "source_entity" in value:
        import capo_quicksight.types.analysis_source_entity

        out["SourceEntity"] = (
            capo_quicksight.types.analysis_source_entity.serialize_json(
                value["source_entity"]
            )
        )
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    if "definition" in value:
        import capo_quicksight.types.analysis_definition

        out["Definition"] = capo_quicksight.types.analysis_definition.serialize_json(
            value["definition"]
        )
    if "validation_strategy" in value:
        import capo_quicksight.types.validation_strategy

        out["ValidationStrategy"] = (
            capo_quicksight.types.validation_strategy.serialize_json(
                value["validation_strategy"]
            )
        )
    if "folder_arns" in value:
        import capo_quicksight.types.folder_arn_list

        out["FolderArns"] = capo_quicksight.types.folder_arn_list.serialize_json(
            value["folder_arns"]
        )
    return out


def deserialize_json(data: dict) -> CreateAnalysisRequest:
    out: CreateAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Parameters") is not None:
        import capo_quicksight.types.parameters

        out["parameters"] = capo_quicksight.types.parameters.deserialize_json(
            data["Parameters"]
        )
    if data.get("Permissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if data.get("SourceEntity") is not None:
        import capo_quicksight.types.analysis_source_entity

        out["source_entity"] = (
            capo_quicksight.types.analysis_source_entity.deserialize_json(
                data["SourceEntity"]
            )
        )
    if data.get("ThemeArn") is not None:
        out["theme_arn"] = data["ThemeArn"]
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    if data.get("Definition") is not None:
        import capo_quicksight.types.analysis_definition

        out["definition"] = capo_quicksight.types.analysis_definition.deserialize_json(
            data["Definition"]
        )
    if data.get("ValidationStrategy") is not None:
        import capo_quicksight.types.validation_strategy

        out["validation_strategy"] = (
            capo_quicksight.types.validation_strategy.deserialize_json(
                data["ValidationStrategy"]
            )
        )
    if data.get("FolderArns") is not None:
        import capo_quicksight.types.folder_arn_list

        out["folder_arns"] = capo_quicksight.types.folder_arn_list.deserialize_json(
            data["FolderArns"]
        )
    return out


def redact_sensitive(value: CreateAnalysisRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        import capo_quicksight.types.parameters

        out["parameters"] = capo_quicksight.types.parameters.redact_sensitive(
            value["parameters"]
        )
    if "definition" in value:
        import capo_quicksight.types.analysis_definition

        out["definition"] = capo_quicksight.types.analysis_definition.redact_sensitive(
            value["definition"]
        )
    return out
