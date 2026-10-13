"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateTemplateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.tag_list
    import capo_quicksight.types.template_name
    import capo_quicksight.types.template_source_entity
    import capo_quicksight.types.template_version_definition
    import capo_quicksight.types.validation_strategy
    import capo_quicksight.types.version_description


class CreateTemplateRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. You use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    template_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An ID for the template that you want to create. This template is unique per Amazon Web Services Region; in each Amazon Web Services account.</p>"""
    name: NotRequired["capo_quicksight.types.template_name.TemplateName"]
    """<p>A display name for the template.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A list of resource permissions to be set on the template. </p>"""
    source_entity: NotRequired[
        "capo_quicksight.types.template_source_entity.TemplateSourceEntity"
    ]
    """<p>The entity that you are using as a source when you create the template. In <code>SourceEntity</code>, you specify the type of object you're using as source: <code>SourceTemplate</code> for a template or <code>SourceAnalysis</code> for an analysis. Both of these require an Amazon Resource Name (ARN). For <code>SourceTemplate</code>, specify the ARN of the source template. For <code>SourceAnalysis</code>, specify the ARN of the source analysis. The <code>SourceTemplate</code> ARN can contain any Amazon Web Services account and any Quick Sight-supported Amazon Web Services Region. </p> <p>Use the <code>DataSetReferences</code> entity within <code>SourceTemplate</code> or <code>SourceAnalysis</code> to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder. Use the <code>TopicReferences</code> entity to list the replacement topics for the topic placeholders listed in the original. The schema in each topic must match its placeholder.</p> <p>Either a <code>SourceEntity</code> or a <code>Definition</code> must be provided in order for the request to be valid.</p>"""
    tags: NotRequired["capo_quicksight.types.tag_list.TagList"]
    """<p>Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.</p>"""
    version_description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>A description of the current template version being created. This API operation creates the first version of the template. Every time <code>UpdateTemplate</code> is called, a new version is created. Each version of the template maintains a description of the version in the <code>VersionDescription</code> field.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.template_version_definition.TemplateVersionDefinition"
    ]
    """<p>The definition of a template.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p> <p>Either a <code>SourceEntity</code> or a <code>Definition</code> must be provided in order for the request to be valid.</p>"""
    validation_strategy: NotRequired[
        "capo_quicksight.types.validation_strategy.ValidationStrategy"
    ]
    """<p>TThe option to relax the validation needed to create a template with definition objects. This skips the validation step for specific errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "source_entity" in value:
        import capo_quicksight.types.template_source_entity

        out["SourceEntity"] = (
            capo_quicksight.types.template_source_entity.serialize_json(
                value["source_entity"]
            )
        )
    if "tags" in value:
        import capo_quicksight.types.tag_list

        out["Tags"] = capo_quicksight.types.tag_list.serialize_json(value["tags"])
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
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


def deserialize_json(data: dict) -> CreateTemplateRequest:
    out: CreateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Permissions") is not None:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if data.get("SourceEntity") is not None:
        import capo_quicksight.types.template_source_entity

        out["source_entity"] = (
            capo_quicksight.types.template_source_entity.deserialize_json(
                data["SourceEntity"]
            )
        )
    if data.get("Tags") is not None:
        import capo_quicksight.types.tag_list

        out["tags"] = capo_quicksight.types.tag_list.deserialize_json(data["Tags"])
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
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


def redact_sensitive(value: CreateTemplateRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "definition" in value:
        import capo_quicksight.types.template_version_definition

        out["definition"] = (
            capo_quicksight.types.template_version_definition.redact_sensitive(
                value["definition"]
            )
        )
    return out
