"""Generated from Smithy shape ``com.amazonaws.memorydb#MultiRegionParameterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class MultiRegionParameterGroup(TypedDict, closed=True):
    name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the multi-region parameter group.</p>"""
    family: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the parameter group family that this multi-region parameter group is compatible with.</p>"""
    description: NotRequired["capo_memorydb.types.string.String"]
    """<p>A description of the multi-region parameter group.</p>"""
    arn: NotRequired["capo_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the multi-region parameter group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionParameterGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "family" in value:
        out["Family"] = value["family"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MultiRegionParameterGroup:
    out: MultiRegionParameterGroup = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Family") is not None:
        out["family"] = data["Family"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MultiRegionParameterGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "family" in value:
        out["Family"] = value["family"]
    if "description" in value:
        out["Description"] = value["description"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> MultiRegionParameterGroup:
    out: MultiRegionParameterGroup = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Family") is not None:
        out["family"] = data["Family"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ARN") is not None:
        out["arn"] = data["ARN"]
    return out
