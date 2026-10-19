"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserDashboardEmbeddingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.registered_user_dashboard_feature_configurations
    import capo_quicksight.types.short_restrictive_resource_id


class RegisteredUserDashboardEmbeddingConfiguration(TypedDict, closed=True):
    initial_dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The dashboard ID for the dashboard that you want the user to see first. This ID is included in the output URL. When the URL in response is accessed, Amazon Quick Sight renders this dashboard if the user has permissions to view it.</p> <p>If the user does not have permission to view this dashboard, they see a permissions error message.</p>"""
    feature_configurations: NotRequired[
        "capo_quicksight.types.registered_user_dashboard_feature_configurations.RegisteredUserDashboardFeatureConfigurations"
    ]
    """<p>The feature configurations of an embbedded Amazon Quick Sight dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserDashboardEmbeddingConfiguration) -> dict:
    out: dict = {}
    out["InitialDashboardId"] = value["initial_dashboard_id"]
    if "feature_configurations" in value:
        import capo_quicksight.types.registered_user_dashboard_feature_configurations

        out["FeatureConfigurations"] = (
            capo_quicksight.types.registered_user_dashboard_feature_configurations.serialize_json(
                value["feature_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisteredUserDashboardEmbeddingConfiguration:
    out: RegisteredUserDashboardEmbeddingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("InitialDashboardId") is not None:
        out["initial_dashboard_id"] = data["InitialDashboardId"]
    else:
        out["initial_dashboard_id"] = ""
    if data.get("FeatureConfigurations") is not None:
        import capo_quicksight.types.registered_user_dashboard_feature_configurations

        out["feature_configurations"] = (
            capo_quicksight.types.registered_user_dashboard_feature_configurations.deserialize_json(
                data["FeatureConfigurations"]
            )
        )
    return out
