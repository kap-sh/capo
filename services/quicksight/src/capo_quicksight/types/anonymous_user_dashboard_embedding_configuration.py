"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserDashboardEmbeddingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_features
    import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_features
    import capo_quicksight.types.anonymous_user_dashboard_feature_configurations
    import capo_quicksight.types.short_restrictive_resource_id


class AnonymousUserDashboardEmbeddingConfiguration(TypedDict, closed=True):
    initial_dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The dashboard ID for the dashboard that you want the user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon Quick Sight renders this dashboard.</p> <p>The Amazon Resource Name (ARN) of this dashboard must be included in the <code>AuthorizedResourceArns</code> parameter. Otherwise, the request will fail with <code>InvalidParameterValueException</code>.</p>"""
    enabled_features: NotRequired[
        "capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_features.AnonymousUserDashboardEmbeddingConfigurationEnabledFeatures"
    ]
    """<p>A list of all enabled features of a specified anonymous dashboard.</p>"""
    disabled_features: NotRequired[
        "capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_features.AnonymousUserDashboardEmbeddingConfigurationDisabledFeatures"
    ]
    """<p>A list of all disabled features of a specified anonymous dashboard.</p>"""
    feature_configurations: NotRequired[
        "capo_quicksight.types.anonymous_user_dashboard_feature_configurations.AnonymousUserDashboardFeatureConfigurations"
    ]
    """<p>The feature configuration for an embedded dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnonymousUserDashboardEmbeddingConfiguration) -> dict:
    out: dict = {}
    out["InitialDashboardId"] = value["initial_dashboard_id"]
    if "enabled_features" in value:
        import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_features

        out["EnabledFeatures"] = (
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_features.serialize_json(
                value["enabled_features"]
            )
        )
    if "disabled_features" in value:
        import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_features

        out["DisabledFeatures"] = (
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_features.serialize_json(
                value["disabled_features"]
            )
        )
    if "feature_configurations" in value:
        import capo_quicksight.types.anonymous_user_dashboard_feature_configurations

        out["FeatureConfigurations"] = (
            capo_quicksight.types.anonymous_user_dashboard_feature_configurations.serialize_json(
                value["feature_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnonymousUserDashboardEmbeddingConfiguration:
    out: AnonymousUserDashboardEmbeddingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InitialDashboardId") is not None:
        out["initial_dashboard_id"] = data["InitialDashboardId"]
    else:
        out["initial_dashboard_id"] = ""
    if data.get("EnabledFeatures") is not None:
        import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_features

        out["enabled_features"] = (
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_enabled_features.deserialize_json(
                data["EnabledFeatures"]
            )
        )
    if data.get("DisabledFeatures") is not None:
        import capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_features

        out["disabled_features"] = (
            capo_quicksight.types.anonymous_user_dashboard_embedding_configuration_disabled_features.deserialize_json(
                data["DisabledFeatures"]
            )
        )
    if data.get("FeatureConfigurations") is not None:
        import capo_quicksight.types.anonymous_user_dashboard_feature_configurations

        out["feature_configurations"] = (
            capo_quicksight.types.anonymous_user_dashboard_feature_configurations.deserialize_json(
                data["FeatureConfigurations"]
            )
        )
    return out
