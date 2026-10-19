"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobDataSetOverrideParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_refresh_properties
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_name


class AssetBundleImportJobDataSetOverrideParameters(TypedDict, closed=True):
    data_set_id: "capo_quicksight.types.resource_id.ResourceId"
    """<p>The ID of the dataset to apply overrides to.</p>"""
    name: NotRequired["capo_quicksight.types.resource_name.ResourceName"]
    """<p>A new name for the dataset.</p>"""
    data_set_refresh_properties: NotRequired[
        "capo_quicksight.types.data_set_refresh_properties.DataSetRefreshProperties"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobDataSetOverrideParameters) -> dict:
    out: dict = {}
    out["DataSetId"] = value["data_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "data_set_refresh_properties" in value:
        import capo_quicksight.types.data_set_refresh_properties

        out["DataSetRefreshProperties"] = (
            capo_quicksight.types.data_set_refresh_properties.serialize_json(
                value["data_set_refresh_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobDataSetOverrideParameters:
    out: AssetBundleImportJobDataSetOverrideParameters = {}  # type: ignore[typeddict-item]
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DataSetRefreshProperties") is not None:
        import capo_quicksight.types.data_set_refresh_properties

        out["data_set_refresh_properties"] = (
            capo_quicksight.types.data_set_refresh_properties.deserialize_json(
                data["DataSetRefreshProperties"]
            )
        )
    return out
