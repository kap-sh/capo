"""Generated from Smithy shape ``com.amazonaws.licensemanager#ReceivedMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.allowed_operation_list
    import capo_license_manager.types.grant_type
    import capo_license_manager.types.received_status
    import capo_license_manager.types.status_reason_message


class ReceivedMetadata(TypedDict, closed=True):
    received_status: NotRequired[
        "capo_license_manager.types.received_status.ReceivedStatus"
    ]
    """<p>Received status.</p>"""
    received_status_reason: NotRequired[
        "capo_license_manager.types.status_reason_message.StatusReasonMessage"
    ]
    """<p>Received status reason.</p>"""
    allowed_operations: NotRequired[
        "capo_license_manager.types.allowed_operation_list.AllowedOperationList"
    ]
    """<p>Allowed operations.</p>"""
    grant_type: NotRequired["capo_license_manager.types.grant_type.GrantType"]
    """<p>The type of the grant through which the license was received. Valid values:</p> <ul> <li> <p> <code>BuyerGrant</code> - Grants you the entitlement to use the license.</p> </li> <li> <p> <code>DelegateGrant</code> - Gives you read-only visibility into the licenses and grants distributed to buyers, with no entitlement to use them.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReceivedMetadata) -> dict:
    out: dict = {}
    if "received_status" in value:
        import capo_license_manager.types.received_status

        out["ReceivedStatus"] = (
            capo_license_manager.types.received_status.serialize_aws_json_1_1(
                value["received_status"]
            )
        )
    if "received_status_reason" in value:
        out["ReceivedStatusReason"] = value["received_status_reason"]
    if "allowed_operations" in value:
        import capo_license_manager.types.allowed_operation_list

        out["AllowedOperations"] = (
            capo_license_manager.types.allowed_operation_list.serialize_aws_json_1_1(
                value["allowed_operations"]
            )
        )
    if "grant_type" in value:
        import capo_license_manager.types.grant_type

        out["GrantType"] = capo_license_manager.types.grant_type.serialize_aws_json_1_1(
            value["grant_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReceivedMetadata:
    out: ReceivedMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ReceivedStatus") is not None:
        import capo_license_manager.types.received_status

        out["received_status"] = (
            capo_license_manager.types.received_status.deserialize_aws_json_1_1(
                data["ReceivedStatus"]
            )
        )
    if data.get("ReceivedStatusReason") is not None:
        out["received_status_reason"] = data["ReceivedStatusReason"]
    if data.get("AllowedOperations") is not None:
        import capo_license_manager.types.allowed_operation_list

        out["allowed_operations"] = (
            capo_license_manager.types.allowed_operation_list.deserialize_aws_json_1_1(
                data["AllowedOperations"]
            )
        )
    if data.get("GrantType") is not None:
        import capo_license_manager.types.grant_type

        out["grant_type"] = (
            capo_license_manager.types.grant_type.deserialize_aws_json_1_1(
                data["GrantType"]
            )
        )
    return out
