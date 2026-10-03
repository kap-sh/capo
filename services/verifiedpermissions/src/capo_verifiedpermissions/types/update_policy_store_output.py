"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdatePolicyStoreOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.resource_arn
    import capo_verifiedpermissions.types.timestamp_format


class UpdatePolicyStoreOutput(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The ID of the updated policy store.</p>"""
    arn: "capo_verifiedpermissions.types.resource_arn.ResourceArn"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the updated policy store.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy store was originally created.</p>"""
    last_updated_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time that the policy store was most recently updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePolicyStoreOutput) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["arn"] = value["arn"]
    import capo_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    import capo_verifiedpermissions.types.timestamp_format

    out["lastUpdatedDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["last_updated_date"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePolicyStoreOutput:
    out: UpdatePolicyStoreOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("UpdatePolicyStoreOutput.policy_store_id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdatePolicyStoreOutput.arn required")
    if data.get("createdDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyStoreOutput.created_date required")
    if data.get("lastUpdatedDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyStoreOutput.last_updated_date required")
    return out
