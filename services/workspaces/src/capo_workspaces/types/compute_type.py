"""Generated from Smithy shape ``com.amazonaws.workspaces#ComputeType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.compute


class ComputeType(TypedDict, closed=True):
    name: NotRequired["capo_workspaces.types.compute.Compute"]
    """<p>The compute type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeType) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_workspaces.types.compute

        out["Name"] = capo_workspaces.types.compute.serialize_aws_json_1_1(
            value["name"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeType:
    out: ComputeType = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_workspaces.types.compute

        out["name"] = capo_workspaces.types.compute.deserialize_aws_json_1_1(
            data["Name"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComputeType) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_workspaces.types.compute

        out["Name"] = capo_workspaces.types.compute.serialize_cbor(value["name"])
    return out


def deserialize_cbor(data: dict) -> ComputeType:
    out: ComputeType = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_workspaces.types.compute

        out["name"] = capo_workspaces.types.compute.deserialize_cbor(data["Name"])
    return out
