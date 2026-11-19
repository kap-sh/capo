"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateSubnetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.subnet_group


class CreateSubnetGroupResponse(TypedDict, closed=True):
    subnet_group: NotRequired["capo_memorydb.types.subnet_group.SubnetGroup"]
    """<p>The newly-created subnet group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSubnetGroupResponse) -> dict:
    out: dict = {}
    if "subnet_group" in value:
        import capo_memorydb.types.subnet_group

        out["SubnetGroup"] = capo_memorydb.types.subnet_group.serialize_aws_json_1_1(
            value["subnet_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSubnetGroupResponse:
    out: CreateSubnetGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubnetGroup") is not None:
        import capo_memorydb.types.subnet_group

        out["subnet_group"] = capo_memorydb.types.subnet_group.deserialize_aws_json_1_1(
            data["SubnetGroup"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateSubnetGroupResponse) -> dict:
    out: dict = {}
    if "subnet_group" in value:
        import capo_memorydb.types.subnet_group

        out["SubnetGroup"] = capo_memorydb.types.subnet_group.serialize_cbor(
            value["subnet_group"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateSubnetGroupResponse:
    out: CreateSubnetGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubnetGroup") is not None:
        import capo_memorydb.types.subnet_group

        out["subnet_group"] = capo_memorydb.types.subnet_group.deserialize_cbor(
            data["SubnetGroup"]
        )
    return out
