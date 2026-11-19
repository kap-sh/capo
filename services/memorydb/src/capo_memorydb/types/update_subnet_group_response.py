"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateSubnetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.subnet_group


class UpdateSubnetGroupResponse(TypedDict, closed=True):
    subnet_group: NotRequired["capo_memorydb.types.subnet_group.SubnetGroup"]
    """<p>The updated subnet group</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubnetGroupResponse) -> dict:
    out: dict = {}
    if "subnet_group" in value:
        import capo_memorydb.types.subnet_group

        out["SubnetGroup"] = capo_memorydb.types.subnet_group.serialize_aws_json_1_1(
            value["subnet_group"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubnetGroupResponse:
    out: UpdateSubnetGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubnetGroup") is not None:
        import capo_memorydb.types.subnet_group

        out["subnet_group"] = capo_memorydb.types.subnet_group.deserialize_aws_json_1_1(
            data["SubnetGroup"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateSubnetGroupResponse) -> dict:
    out: dict = {}
    if "subnet_group" in value:
        import capo_memorydb.types.subnet_group

        out["SubnetGroup"] = capo_memorydb.types.subnet_group.serialize_cbor(
            value["subnet_group"]
        )
    return out


def deserialize_cbor(data: dict) -> UpdateSubnetGroupResponse:
    out: UpdateSubnetGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("SubnetGroup") is not None:
        import capo_memorydb.types.subnet_group

        out["subnet_group"] = capo_memorydb.types.subnet_group.deserialize_cbor(
            data["SubnetGroup"]
        )
    return out
