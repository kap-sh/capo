"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.operation_id


class GetOperationRequest(TypedDict, closed=True):
    operation_id: "capo_servicediscovery.types.operation_id.OperationId"
    """<p>The ID of the operation that you want to get more information about.</p>"""
    owner_account: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that owns the namespace associated with the operation, as specified in the namespace <code>ResourceOwner</code> field. For operations associated with namespaces that are shared with your account, you must specify an <code>OwnerAccount</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationRequest) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationRequest:
    out: GetOperationRequest = {}  # type: ignore[typeddict-item]
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    else:
        out["operation_id"] = ""
    if data.get("OwnerAccount") is not None:
        out["owner_account"] = data["OwnerAccount"]
    return out
