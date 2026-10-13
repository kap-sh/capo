"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyStoreItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_store_description
    import capo_verifiedpermissions.types.policy_store_id
    import capo_verifiedpermissions.types.resource_arn
    import capo_verifiedpermissions.types.timestamp_format


class PolicyStoreItem(TypedDict, closed=True):
    policy_store_id: "capo_verifiedpermissions.types.policy_store_id.PolicyStoreId"
    """<p>The unique identifier of the policy store.</p>"""
    arn: "capo_verifiedpermissions.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the policy store.</p>"""
    created_date: "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    """<p>The date and time the policy was created.</p>"""
    last_updated_date: NotRequired[
        "capo_verifiedpermissions.types.timestamp_format.TimestampFormat"
    ]
    """<p>The date and time the policy store was most recently updated.</p>"""
    description: NotRequired[
        "capo_verifiedpermissions.types.policy_store_description.PolicyStoreDescription"
    ]
    """<p>Descriptive text that you can provide to help with identification of the current policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyStoreItem) -> dict:
    out: dict = {}
    out["policyStoreId"] = value["policy_store_id"]
    out["arn"] = value["arn"]
    import capo_verifiedpermissions.types.timestamp_format

    out["createdDate"] = (
        capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
            value["created_date"]
        )
    )
    if "last_updated_date" in value:
        import capo_verifiedpermissions.types.timestamp_format

        out["lastUpdatedDate"] = (
            capo_verifiedpermissions.types.timestamp_format.serialize_aws_json_1_0(
                value["last_updated_date"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyStoreItem:
    out: PolicyStoreItem = {}  # type: ignore[typeddict-item]
    if data.get("policyStoreId") is not None:
        out["policy_store_id"] = data["policyStoreId"]
    else:
        raise DeserializationError("PolicyStoreItem.policy_store_id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("PolicyStoreItem.arn required")
    if data.get("createdDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["created_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("PolicyStoreItem.created_date required")
    if data.get("lastUpdatedDate") is not None:
        import capo_verifiedpermissions.types.timestamp_format

        out["last_updated_date"] = (
            capo_verifiedpermissions.types.timestamp_format.deserialize_aws_json_1_0(
                data["lastUpdatedDate"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: PolicyStoreItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
