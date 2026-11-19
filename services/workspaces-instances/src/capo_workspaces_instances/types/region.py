"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Region``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.region_name


class Region(TypedDict, closed=True):
    region_name: NotRequired["capo_workspaces_instances.types.region_name.RegionName"]
    """<p>Name of the AWS region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Region) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Region) -> dict:
    out: dict = {}
    if "region_name" in value:
        out["RegionName"] = value["region_name"]
    return out


def deserialize_cbor(data: dict) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    return out
