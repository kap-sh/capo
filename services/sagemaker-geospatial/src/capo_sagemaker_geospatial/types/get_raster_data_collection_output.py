"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#GetRasterDataCollectionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.data_collection_arn
    import capo_sagemaker_geospatial.types.data_collection_type
    import capo_sagemaker_geospatial.types.filter_list
    import capo_sagemaker_geospatial.types.image_source_band_list
    import capo_sagemaker_geospatial.types.tags


class GetRasterDataCollectionOutput(TypedDict, closed=True):
    name: "str"
    """<p>The name of the raster data collection.</p>"""
    arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn"
    """<p>The Amazon Resource Name (ARN) of the raster data collection.</p>"""
    type: "capo_sagemaker_geospatial.types.data_collection_type.DataCollectionType"
    """<p>The raster data collection type.</p>"""
    description: "str"
    """<p>A description of the raster data collection.</p>"""
    description_page_url: "str"
    """<p>The URL of the description page.</p>"""
    supported_filters: "capo_sagemaker_geospatial.types.filter_list.FilterList"
    """<p>The filters supported by the raster data collection.</p>"""
    image_source_bands: (
        "capo_sagemaker_geospatial.types.image_source_band_list.ImageSourceBandList"
    )
    """<p>The list of image source bands in the raster data collection.</p>"""
    tags: NotRequired["capo_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRasterDataCollectionOutput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    out["Type"] = value["type"]
    out["Description"] = value["description"]
    out["DescriptionPageUrl"] = value["description_page_url"]
    import capo_sagemaker_geospatial.types.filter_list

    out["SupportedFilters"] = (
        capo_sagemaker_geospatial.types.filter_list.serialize_json(
            value["supported_filters"]
        )
    )
    import capo_sagemaker_geospatial.types.image_source_band_list

    out["ImageSourceBands"] = (
        capo_sagemaker_geospatial.types.image_source_band_list.serialize_json(
            value["image_source_bands"]
        )
    )
    if "tags" in value:
        import capo_sagemaker_geospatial.types.tags

        out["Tags"] = capo_sagemaker_geospatial.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetRasterDataCollectionOutput:
    out: GetRasterDataCollectionOutput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("DescriptionPageUrl") is not None:
        out["description_page_url"] = data["DescriptionPageUrl"]
    else:
        out["description_page_url"] = ""
    if data.get("SupportedFilters") is not None:
        import capo_sagemaker_geospatial.types.filter_list

        out["supported_filters"] = (
            capo_sagemaker_geospatial.types.filter_list.deserialize_json(
                data["SupportedFilters"]
            )
        )
    else:
        out["supported_filters"] = []
    if data.get("ImageSourceBands") is not None:
        import capo_sagemaker_geospatial.types.image_source_band_list

        out["image_source_bands"] = (
            capo_sagemaker_geospatial.types.image_source_band_list.deserialize_json(
                data["ImageSourceBands"]
            )
        )
    else:
        out["image_source_bands"] = []
    if data.get("Tags") is not None:
        import capo_sagemaker_geospatial.types.tags

        out["tags"] = capo_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
