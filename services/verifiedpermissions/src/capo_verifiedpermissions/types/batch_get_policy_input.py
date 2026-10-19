"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_get_policy_input_list


class BatchGetPolicyInput(TypedDict, closed=True):
    requests: "capo_verifiedpermissions.types.batch_get_policy_input_list.BatchGetPolicyInputList"
    """<p>An array of up to 100 policies you want information about.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyInput) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.batch_get_policy_input_list

    out["requests"] = (
        capo_verifiedpermissions.types.batch_get_policy_input_list.serialize_aws_json_1_0(
            value["requests"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyInput:
    out: BatchGetPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("requests") is not None:
        import capo_verifiedpermissions.types.batch_get_policy_input_list

        out["requests"] = (
            capo_verifiedpermissions.types.batch_get_policy_input_list.deserialize_aws_json_1_0(
                data["requests"]
            )
        )
    else:
        out["requests"] = []
    return out
