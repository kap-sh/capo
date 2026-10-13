"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTemplateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.template_name
    import capo_quicksight.types.template_source_entity
    import capo_quicksight.types.template_version_definition
    import capo_quicksight.types.validation_strategy
    import capo_quicksight.types.version_description


class UpdateTemplateRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the template that you're updating.</p>"""
    template_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the template.</p>"""
    source_entity: NotRequired[
        "capo_quicksight.types.template_source_entity.TemplateSourceEntity"
    ]
    """<p>The entity that you are using as a source when you update the template. In <code>SourceEntity</code>, you specify the type of object you're using as source: <code>SourceTemplate</code> for a template or <code>SourceAnalysis</code> for an analysis. Both of these require an Amazon Resource Name (ARN). For <code>SourceTemplate</code>, specify the ARN of the source template. For <code>SourceAnalysis</code>, specify the ARN of the source analysis. The <code>SourceTemplate</code> ARN can contain any Amazon Web Services account and any Quick Sight-supported Amazon Web Services Region;. </p> <p>Use the <code>DataSetReferences</code> entity within <code>SourceTemplate</code> or <code>SourceAnalysis</code> to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder. Use the <code>TopicReferences</code> entity to list the replacement topics for the topic placeholders listed in the original. The schema in each topic must match its placeholder.</p>"""
    version_description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>A description of the current template version that is being updated. Every time you call <code>UpdateTemplate</code>, you create a new version of the template. Each version of the template maintains a description of the version in the <code>VersionDescription</code> field.</p>"""
    name: NotRequired["capo_quicksight.types.template_name.TemplateName"]
    """<p>The name for the template.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.template_version_definition.TemplateVersionDefinition"
    ]
    """<p>The definition of a template.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p>"""
    validation_strategy: NotRequired[
        "capo_quicksight.types.validation_strategy.ValidationStrategy"
    ]
    """<p>The option to relax the validation needed to update a template with definition objects. This skips the validation step for specific errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateRequest) -> dict:
    out: dict = {}
    if "source_entity" in value:
        import capo_quicksight.types.template_source_entity

        out["SourceEntity"] = (
            capo_quicksight.types.template_source_entity.serialize_json(
                value["source_entity"]
            )
        )
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "name" in value:
        out["Name"] = value["name"]
    if "definition" in value:
        import capo_quicksight.types.template_version_definition

        out["Definition"] = (
            capo_quicksight.types.template_version_definition.serialize_json(
                value["definition"]
            )
        )
    if "validation_strategy" in value:
        import capo_quicksight.types.validation_strategy

        out["ValidationStrategy"] = (
            capo_quicksight.types.validation_strategy.serialize_json(
                value["validation_strategy"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateTemplateRequest:
    out: UpdateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceEntity") is not None:
        import capo_quicksight.types.template_source_entity

        out["source_entity"] = (
            capo_quicksight.types.template_source_entity.deserialize_json(
                data["SourceEntity"]
            )
        )
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Definition") is not None:
        import capo_quicksight.types.template_version_definition

        out["definition"] = (
            capo_quicksight.types.template_version_definition.deserialize_json(
                data["Definition"]
            )
        )
    if data.get("ValidationStrategy") is not None:
        import capo_quicksight.types.validation_strategy

        out["validation_strategy"] = (
            capo_quicksight.types.validation_strategy.deserialize_json(
                data["ValidationStrategy"]
            )
        )
    return out


def redact_sensitive(value: UpdateTemplateRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "definition" in value:
        import capo_quicksight.types.template_version_definition

        out["definition"] = (
            capo_quicksight.types.template_version_definition.redact_sensitive(
                value["definition"]
            )
        )
    return out
