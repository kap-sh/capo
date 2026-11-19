"""Generated from Smithy shape ``com.amazonaws.directconnect#AsPathSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.as_path_list
    import capo_direct_connect.types.as_path_type


class AsPathSegment(TypedDict, closed=True):
    path_type: NotRequired["capo_direct_connect.types.as_path_type.AsPathType"]
    """<p>The type of the AS path segment.</p> <p>The valid values are <code>seq</code> (an ordered <code>AS_SEQUENCE</code>) and <code>set</code> (an unordered <code>AS_SET</code>).</p>"""
    path: NotRequired["capo_direct_connect.types.as_path_list.AsPathList"]
    """<p>The autonomous system (AS) numbers in the segment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsPathSegment) -> dict:
    out: dict = {}
    if "path_type" in value:
        import capo_direct_connect.types.as_path_type

        out["pathType"] = capo_direct_connect.types.as_path_type.serialize_aws_json_1_1(
            value["path_type"]
        )
    if "path" in value:
        import capo_direct_connect.types.as_path_list

        out["path"] = capo_direct_connect.types.as_path_list.serialize_aws_json_1_1(
            value["path"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AsPathSegment:
    out: AsPathSegment = {}  # type: ignore[typeddict-item]
    if data.get("pathType") is not None:
        import capo_direct_connect.types.as_path_type

        out["path_type"] = (
            capo_direct_connect.types.as_path_type.deserialize_aws_json_1_1(
                data["pathType"]
            )
        )
    if data.get("path") is not None:
        import capo_direct_connect.types.as_path_list

        out["path"] = capo_direct_connect.types.as_path_list.deserialize_aws_json_1_1(
            data["path"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AsPathSegment) -> dict:
    out: dict = {}
    if "path_type" in value:
        import capo_direct_connect.types.as_path_type

        out["pathType"] = capo_direct_connect.types.as_path_type.serialize_cbor(
            value["path_type"]
        )
    if "path" in value:
        import capo_direct_connect.types.as_path_list

        out["path"] = capo_direct_connect.types.as_path_list.serialize_cbor(
            value["path"]
        )
    return out


def deserialize_cbor(data: dict) -> AsPathSegment:
    out: AsPathSegment = {}  # type: ignore[typeddict-item]
    if data.get("pathType") is not None:
        import capo_direct_connect.types.as_path_type

        out["path_type"] = capo_direct_connect.types.as_path_type.deserialize_cbor(
            data["pathType"]
        )
    if data.get("path") is not None:
        import capo_direct_connect.types.as_path_list

        out["path"] = capo_direct_connect.types.as_path_list.deserialize_cbor(
            data["path"]
        )
    return out
