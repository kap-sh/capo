"""Generated from Smithy shape ``com.amazonaws.directoryservice#RegionsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.additional_regions
    import capo_directory_service.types.region_name


class RegionsInfo(TypedDict, closed=True):
    primary_region: NotRequired["capo_directory_service.types.region_name.RegionName"]
    """<p>The Region where the Managed Microsoft AD directory was originally created.</p>"""
    additional_regions: NotRequired[
        "capo_directory_service.types.additional_regions.AdditionalRegions"
    ]
    """<p>Lists the Regions where the directory has been replicated, excluding the primary Region.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionsInfo) -> dict:
    out: dict = {}
    if "primary_region" in value:
        out["PrimaryRegion"] = value["primary_region"]
    if "additional_regions" in value:
        import capo_directory_service.types.additional_regions

        out["AdditionalRegions"] = (
            capo_directory_service.types.additional_regions.serialize_aws_json_1_1(
                value["additional_regions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionsInfo:
    out: RegionsInfo = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryRegion") is not None:
        out["primary_region"] = data["PrimaryRegion"]
    if data.get("AdditionalRegions") is not None:
        import capo_directory_service.types.additional_regions

        out["additional_regions"] = (
            capo_directory_service.types.additional_regions.deserialize_aws_json_1_1(
                data["AdditionalRegions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegionsInfo) -> dict:
    out: dict = {}
    if "primary_region" in value:
        out["PrimaryRegion"] = value["primary_region"]
    if "additional_regions" in value:
        import capo_directory_service.types.additional_regions

        out["AdditionalRegions"] = (
            capo_directory_service.types.additional_regions.serialize_cbor(
                value["additional_regions"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RegionsInfo:
    out: RegionsInfo = {}  # type: ignore[typeddict-item]
    if data.get("PrimaryRegion") is not None:
        out["primary_region"] = data["PrimaryRegion"]
    if data.get("AdditionalRegions") is not None:
        import capo_directory_service.types.additional_regions

        out["additional_regions"] = (
            capo_directory_service.types.additional_regions.deserialize_cbor(
                data["AdditionalRegions"]
            )
        )
    return out
