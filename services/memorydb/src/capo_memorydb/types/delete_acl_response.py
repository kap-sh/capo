"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteACLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.acl


class DeleteACLResponse(TypedDict, closed=True):
    acl: NotRequired["capo_memorydb.types.acl.ACL"]
    """<p>The Access Control List object that has been deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteACLResponse) -> dict:
    out: dict = {}
    if "acl" in value:
        import capo_memorydb.types.acl

        out["ACL"] = capo_memorydb.types.acl.serialize_aws_json_1_1(value["acl"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteACLResponse:
    out: DeleteACLResponse = {}  # type: ignore[typeddict-item]
    if data.get("ACL") is not None:
        import capo_memorydb.types.acl

        out["acl"] = capo_memorydb.types.acl.deserialize_aws_json_1_1(data["ACL"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteACLResponse) -> dict:
    out: dict = {}
    if "acl" in value:
        import capo_memorydb.types.acl

        out["ACL"] = capo_memorydb.types.acl.serialize_cbor(value["acl"])
    return out


def deserialize_cbor(data: dict) -> DeleteACLResponse:
    out: DeleteACLResponse = {}  # type: ignore[typeddict-item]
    if data.get("ACL") is not None:
        import capo_memorydb.types.acl

        out["acl"] = capo_memorydb.types.acl.deserialize_cbor(data["ACL"])
    return out
