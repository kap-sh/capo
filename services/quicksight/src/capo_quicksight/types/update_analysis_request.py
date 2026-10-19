"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAnalysisRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.analysis_definition
    import capo_quicksight.types.analysis_name
    import capo_quicksight.types.analysis_source_entity
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.parameters
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.validation_strategy


class UpdateAnalysisRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the analysis that you're updating.</p>"""
    analysis_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the analysis that you're updating. This ID displays in the URL of the analysis.</p>"""
    name: "capo_quicksight.types.analysis_name.AnalysisName"
    """<p>A descriptive name for the analysis that you're updating. This name displays for the analysis in the Amazon Quick Sight console.</p>"""
    parameters: NotRequired["capo_quicksight.types.parameters.Parameters"]
    """<p>The parameter names and override values that you want to use. An analysis can have any parameter type, and some parameters might accept multiple values. </p>"""
    source_entity: NotRequired[
        "capo_quicksight.types.analysis_source_entity.AnalysisSourceEntity"
    ]
    """<p>A source entity to use for the analysis that you're updating. This metadata structure contains details that describe a source template and one or more datasets or topics.</p>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the theme to apply to the analysis that you're creating. To see the theme in the Amazon Quick Sight console, make sure that you have access to it.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.analysis_definition.AnalysisDefinition"
    ]
    """<p>The definition of an analysis.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p>"""
    validation_strategy: NotRequired[
        "capo_quicksight.types.validation_strategy.ValidationStrategy"
    ]
    """<p>The option to relax the validation needed to update an analysis with definition objects. This skips the validation step for specific errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnalysisRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "parameters" in value:
        import capo_quicksight.types.parameters

        out["Parameters"] = capo_quicksight.types.parameters.serialize_json(
            value["parameters"]
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
    return out


def deserialize_json(data: dict) -> UpdateAnalysisRequest:
    out: UpdateAnalysisRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Parameters") is not None:
        import capo_quicksight.types.parameters

        out["parameters"] = capo_quicksight.types.parameters.deserialize_json(
            data["Parameters"]
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
    return out


def redact_sensitive(value: UpdateAnalysisRequest) -> dict[str, Any]:
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
