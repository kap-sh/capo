"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class DeleteACLRequest(TypedDict, closed=True):
    acl_name: "capo_memorydb.types.string.String"
    """<p>The name of the Access Control List to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteACLRequest) -> dict:
    out: dict = {}
    out["ACLName"] = value["acl_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteACLRequest:
    out: DeleteACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("ACLName") is not None:
        out["acl_name"] = data["ACLName"]
    else:
        out["acl_name"] = ""
    return out
