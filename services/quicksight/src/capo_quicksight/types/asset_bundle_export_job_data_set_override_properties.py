"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSetOverrideProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list


class AssetBundleExportJobDataSetOverrideProperties(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The ARN of the specific <code>DataSet</code> resource whose override properties are configured in this structure.</p>"""
    properties: "capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list.AssetBundleExportJobDataSetPropertyToOverrideList"
    """<p>A list of <code>DataSet</code> resource properties to generate variables for in the returned CloudFormation template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDataSetOverrideProperties) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list

    out["Properties"] = (
        capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list.serialize_json(
            value["properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobDataSetOverrideProperties:
    out: AssetBundleExportJobDataSetOverrideProperties = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Properties") is not None:
        import capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list

        out["properties"] = (
            capo_quicksight.types.asset_bundle_export_job_data_set_property_to_override_list.deserialize_json(
                data["Properties"]
            )
        )
    else:
        out["properties"] = []
    return out
