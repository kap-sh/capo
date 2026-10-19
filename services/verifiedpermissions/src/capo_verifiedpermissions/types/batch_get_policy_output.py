"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#BatchGetPolicyOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.batch_get_policy_error_list
    import capo_verifiedpermissions.types.batch_get_policy_output_list


class BatchGetPolicyOutput(TypedDict, closed=True):
    results: "capo_verifiedpermissions.types.batch_get_policy_output_list.BatchGetPolicyOutputList"
    """<p>Information about the policies listed in the request that were successfully returned. These results are returned in the order they were requested.</p>"""
    errors: "capo_verifiedpermissions.types.batch_get_policy_error_list.BatchGetPolicyErrorList"
    """<p>Information about the policies from the request that resulted in an error. These results are returned in the order they were requested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetPolicyOutput) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.batch_get_policy_output_list

    out["results"] = (
        capo_verifiedpermissions.types.batch_get_policy_output_list.serialize_aws_json_1_0(
            value["results"]
        )
    )
    import capo_verifiedpermissions.types.batch_get_policy_error_list

    out["errors"] = (
        capo_verifiedpermissions.types.batch_get_policy_error_list.serialize_aws_json_1_0(
            value["errors"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetPolicyOutput:
    out: BatchGetPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_verifiedpermissions.types.batch_get_policy_output_list

        out["results"] = (
            capo_verifiedpermissions.types.batch_get_policy_output_list.deserialize_aws_json_1_0(
                data["results"]
            )
        )
    else:
        out["results"] = []
    if data.get("errors") is not None:
        import capo_verifiedpermissions.types.batch_get_policy_error_list

        out["errors"] = (
            capo_verifiedpermissions.types.batch_get_policy_error_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    else:
        out["errors"] = []
    return out


def redact_sensitive(value: BatchGetPolicyOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "results" in value:
        import capo_verifiedpermissions.types.batch_get_policy_output_list

        out["results"] = (
            capo_verifiedpermissions.types.batch_get_policy_output_list.redact_sensitive(
                value["results"]
            )
        )
    return out
