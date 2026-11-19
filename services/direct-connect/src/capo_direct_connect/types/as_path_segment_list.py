"""Generated from Smithy shape ``com.amazonaws.directconnect#AsPathSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.as_path_segment

AsPathSegmentList: TypeAlias = list[
    "capo_direct_connect.types.as_path_segment.AsPathSegment"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsPathSegmentList) -> list:
    import capo_direct_connect.types.as_path_segment

    out: list = []
    for item in value:
        out.append(
            capo_direct_connect.types.as_path_segment.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AsPathSegmentList:
    import capo_direct_connect.types.as_path_segment

    out: AsPathSegmentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.as_path_segment.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AsPathSegmentList) -> list:
    import capo_direct_connect.types.as_path_segment

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.as_path_segment.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AsPathSegmentList:
    import capo_direct_connect.types.as_path_segment

    out: AsPathSegmentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.as_path_segment.deserialize_cbor(item))
    return out
