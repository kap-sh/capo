"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletePolicyStoreInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_store_id


class DeletePolicyStoreInput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>Specifies the ID of the policy store that you want to delete.</p> <note> <p>To specify a policy store, the alias name cannot be used. Only the ID can be used.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePolicyStoreInput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePolicyStoreInput:
    out: DeletePolicyStoreInput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    return out
