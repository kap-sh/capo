"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.dashboard_name
    import capo_quicksight.types.dashboard_publish_options
    import capo_quicksight.types.dashboard_source_entity
    import capo_quicksight.types.dashboard_version_definition
    import capo_quicksight.types.parameters
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.validation_strategy
    import capo_quicksight.types.version_description


class UpdateDashboardRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard that you're updating.</p>"""
    dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the dashboard.</p>"""
    name: "capo_quicksight.types.dashboard_name.DashboardName"
    """<p>The display name of the dashboard.</p>"""
    source_entity: NotRequired[
        "capo_quicksight.types.dashboard_source_entity.DashboardSourceEntity"
    ]
    """<p>The entity that you are using as a source when you update the dashboard. In <code>SourceEntity</code>, you specify the type of object you're using as source. You can only update a dashboard from a template, so you use a <code>SourceTemplate</code> entity. If you need to update a dashboard from an analysis, first convert the analysis to a template by using the <code> <a href="https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a> </code> API operation. For <code>SourceTemplate</code>, specify the Amazon Resource Name (ARN) of the source template. The <code>SourceTemplate</code> ARN can contain any Amazon Web Services account and any Amazon Quick Sight-supported Amazon Web Services Region. </p> <p>Use the <code>DataSetReferences</code> entity within <code>SourceTemplate</code> to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder. Use the <code>TopicReferences</code> entity to list the replacement topics for the topic placeholders listed in the original. The schema in each topic must match its placeholder.</p>"""
    parameters: NotRequired["capo_quicksight.types.parameters.Parameters"]
    """<p>A structure that contains the parameters of the dashboard. These are parameter overrides for a dashboard. A dashboard can have any type of parameters, and some parameters might accept multiple values.</p>"""
    version_description: NotRequired[
        "capo_quicksight.types.version_description.VersionDescription"
    ]
    """<p>A description for the first version of the dashboard being created.</p>"""
    dashboard_publish_options: NotRequired[
        "capo_quicksight.types.dashboard_publish_options.DashboardPublishOptions"
    ]
    """<p>Options for publishing the dashboard when you create it:</p> <ul> <li> <p> <code>AvailabilityStatus</code> for <code>AdHocFilteringOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. When this is set to <code>DISABLED</code>, Amazon Quick Sight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is <code>ENABLED</code> by default. </p> </li> <li> <p> <code>AvailabilityStatus</code> for <code>ExportToCSVOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. The visual option to export data to .CSV format isn't enabled when this is set to <code>DISABLED</code>. This option is <code>ENABLED</code> by default. </p> </li> <li> <p> <code>VisibilityState</code> for <code>SheetControlsOption</code> - This visibility state can be either <code>COLLAPSED</code> or <code>EXPANDED</code>. This option is <code>COLLAPSED</code> by default. </p> </li> <li> <p> <code>AvailabilityStatus</code> for <code>QuickSuiteActionsOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. Features related to Actions in Amazon Quick Suite on dashboards are disabled when this is set to <code>DISABLED</code>. This option is <code>DISABLED</code> by default.</p> </li> <li> <p> <code>AvailabilityStatus</code> for <code>ExecutiveSummaryOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. The option to build an executive summary is disabled when this is set to <code>DISABLED</code>. This option is <code>ENABLED</code> by default.</p> </li> <li> <p> <code>AvailabilityStatus</code> for <code>DataStoriesSharingOption</code> - This status can be either <code>ENABLED</code> or <code>DISABLED</code>. The option to share a data story is disabled when this is set to <code>DISABLED</code>. This option is <code>ENABLED</code> by default.</p> </li> </ul>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the theme that is being used for this dashboard. If you add a value for this field, it overrides the value that was originally associated with the entity. The theme ARN must exist in the same Amazon Web Services account where you create the dashboard.</p>"""
    definition: NotRequired[
        "capo_quicksight.types.dashboard_version_definition.DashboardVersionDefinition"
    ]
    """<p>The definition of a dashboard.</p> <p>A definition is the data model of all features in a Dashboard, Template, or Analysis.</p>"""
    validation_strategy: NotRequired[
        "capo_quicksight.types.validation_strategy.ValidationStrategy"
    ]
    """<p>The option to relax the validation needed to update a dashboard with definition objects. This skips the validation step for specific errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "source_entity" in value:
        import capo_quicksight.types.dashboard_source_entity

        out["SourceEntity"] = (
            capo_quicksight.types.dashboard_source_entity.serialize_json(
                value["source_entity"]
            )
        )
    if "parameters" in value:
        import capo_quicksight.types.parameters

        out["Parameters"] = capo_quicksight.types.parameters.serialize_json(
            value["parameters"]
        )
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "dashboard_publish_options" in value:
        import capo_quicksight.types.dashboard_publish_options

        out["DashboardPublishOptions"] = (
            capo_quicksight.types.dashboard_publish_options.serialize_json(
                value["dashboard_publish_options"]
            )
        )
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "definition" in value:
        import capo_quicksight.types.dashboard_version_definition

        out["Definition"] = (
            capo_quicksight.types.dashboard_version_definition.serialize_json(
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


def deserialize_json(data: dict) -> UpdateDashboardRequest:
    out: UpdateDashboardRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateDashboardRequest.name required")
    if data.get("SourceEntity") is not None:
        import capo_quicksight.types.dashboard_source_entity

        out["source_entity"] = (
            capo_quicksight.types.dashboard_source_entity.deserialize_json(
                data["SourceEntity"]
            )
        )
    if data.get("Parameters") is not None:
        import capo_quicksight.types.parameters

        out["parameters"] = capo_quicksight.types.parameters.deserialize_json(
            data["Parameters"]
        )
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("DashboardPublishOptions") is not None:
        import capo_quicksight.types.dashboard_publish_options

        out["dashboard_publish_options"] = (
            capo_quicksight.types.dashboard_publish_options.deserialize_json(
                data["DashboardPublishOptions"]
            )
        )
    if data.get("ThemeArn") is not None:
        out["theme_arn"] = data["ThemeArn"]
    if data.get("Definition") is not None:
        import capo_quicksight.types.dashboard_version_definition

        out["definition"] = (
            capo_quicksight.types.dashboard_version_definition.deserialize_json(
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
