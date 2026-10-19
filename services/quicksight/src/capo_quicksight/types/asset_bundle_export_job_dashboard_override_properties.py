"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDashboardOverrideProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override_list


class AssetBundleExportJobDashboardOverrideProperties(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The ARN of the specific <code>Dashboard</code> resource whose override properties are configured in this structure.</p>"""
    properties: "capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override_list.AssetBundleExportJobDashboardPropertyToOverrideList"
    """<p>A list of <code>Dashboard</code> resource properties to generate variables for in the returned CloudFormation template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDashboardOverrideProperties) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override_list

    out["Properties"] = (
        capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override_list.serialize_json(
            value["properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobDashboardOverrideProperties:
    out: AssetBundleExportJobDashboardOverrideProperties = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Properties") is not None:
        import capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override_list

        out["properties"] = (
            capo_quicksight.types.asset_bundle_export_job_dashboard_property_to_override_list.deserialize_json(
                data["Properties"]
            )
        )
    else:
        out["properties"] = []
    return out
