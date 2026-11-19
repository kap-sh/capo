"""Generated from Smithy shape ``com.amazonaws.fms#RegionScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_region_list
    import capo_fms.types.boolean


class RegionScope(TypedDict, closed=True):
    regions: NotRequired["capo_fms.types.aws_region_list.AWSRegionList"]
    """<p>The Amazon Web Services Regions that the specified Firewall Manager administrator can perform actions in.</p>"""
    all_regions_enabled: "capo_fms.types.boolean.Boolean"
    """<p>Allows the specified Firewall Manager administrator to manage all Amazon Web Services Regions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegionScope) -> dict:
    out: dict = {}
    if "regions" in value:
        import capo_fms.types.aws_region_list

        out["Regions"] = capo_fms.types.aws_region_list.serialize_aws_json_1_1(
            value["regions"]
        )
    out["AllRegionsEnabled"] = value.get("all_regions_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RegionScope:
    out: RegionScope = {}  # type: ignore[typeddict-item]
    if data.get("Regions") is not None:
        import capo_fms.types.aws_region_list

        out["regions"] = capo_fms.types.aws_region_list.deserialize_aws_json_1_1(
            data["Regions"]
        )
    if data.get("AllRegionsEnabled") is not None:
        out["all_regions_enabled"] = data["AllRegionsEnabled"]
    else:
        out["all_regions_enabled"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegionScope) -> dict:
    out: dict = {}
    if "regions" in value:
        import capo_fms.types.aws_region_list

        out["Regions"] = capo_fms.types.aws_region_list.serialize_cbor(value["regions"])
    out["AllRegionsEnabled"] = value.get("all_regions_enabled", False)
    return out


def deserialize_cbor(data: dict) -> RegionScope:
    out: RegionScope = {}  # type: ignore[typeddict-item]
    if data.get("Regions") is not None:
        import capo_fms.types.aws_region_list

        out["regions"] = capo_fms.types.aws_region_list.deserialize_cbor(
            data["Regions"]
        )
    if data.get("AllRegionsEnabled") is not None:
        out["all_regions_enabled"] = data["AllRegionsEnabled"]
    else:
        out["all_regions_enabled"] = False
    return out
