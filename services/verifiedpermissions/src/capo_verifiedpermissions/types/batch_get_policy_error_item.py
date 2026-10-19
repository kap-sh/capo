"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyErrorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_get_policy_error_code


class BatchGetPolicyErrorItem(TypedDict, closed=True):
    code: "capo_verifiedpermissions.types.batch_get_policy_error_code.BatchGetPolicyErrorCode"
    """<p>The error code that was returned.</p>"""
    policy_store_id: "str"
    """<p>The identifier of the policy store associated with the failed request.</p>"""
    policy_id: "str"
    """<p>The identifier of the policy associated with the failed request.</p>"""
    message: "str"
    """<p>A detailed error message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyErrorItem) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.batch_get_policy_error_code

    out["code"] = (
        capo_verifiedpermissions.types.batch_get_policy_error_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    out["policyStoreId"] = value["policy_store_id"]
    out["policyId"] = value["policy_id"]
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyErrorItem:
    out: BatchGetPolicyErrorItem = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_verifiedpermissions.types.batch_get_policy_error_code

        out["code"] = (
            capo_verifiedpermissions.types.batch_get_policy_error_code.deserialize_aws_json_1_0(
                data["code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_verifiedpermissions.types.batch_get_policy_error_code.BatchGetPolicyErrorCode",
            "",
        )
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        out["policy_store_id"] = ""
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        out["policy_id"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
