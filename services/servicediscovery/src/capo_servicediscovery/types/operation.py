"""Generated from Smithy shape ``com.amazonaws.servicediscovery#Operation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.aws_account_id
    import capo_servicediscovery.types.code
    import capo_servicediscovery.types.message
    import capo_servicediscovery.types.operation_id
    import capo_servicediscovery.types.operation_status
    import capo_servicediscovery.types.operation_targets_map
    import capo_servicediscovery.types.operation_type
    import capo_servicediscovery.types.timestamp


class Operation(TypedDict, closed=True):
    id: NotRequired["capo_servicediscovery.types.operation_id.OperationId"]
    """<p>The ID of the operation that you want to get information about.</p>"""
    owner_account: NotRequired[
        "capo_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that owns the namespace associated with the operation.</p>"""
    type: NotRequired["capo_servicediscovery.types.operation_type.OperationType"]
    """<p>The name of the operation that's associated with the specified ID.</p>"""
    status: NotRequired["capo_servicediscovery.types.operation_status.OperationStatus"]
    """<p>The status of the operation. Values include the following:</p> <dl> <dt>SUBMITTED</dt> <dd> <p>This is the initial state that occurs immediately after you submit a request.</p> </dd> <dt>PENDING</dt> <dd> <p>Cloud Map is performing the operation.</p> </dd> <dt>SUCCESS</dt> <dd> <p>The operation succeeded.</p> </dd> <dt>FAIL</dt> <dd> <p>The operation failed. For the failure reason, see <code>ErrorMessage</code>.</p> </dd> </dl>"""
    error_message: NotRequired["capo_servicediscovery.types.message.Message"]
    """<p>If the value of <code>Status</code> is <code>FAIL</code>, the reason that the operation failed.</p>"""
    error_code: NotRequired["capo_servicediscovery.types.code.Code"]
    """<p>The code associated with <code>ErrorMessage</code>. Values for <code>ErrorCode</code> include the following:</p> <ul> <li> <p> <code>ACCESS_DENIED</code> </p> </li> <li> <p> <code>CANNOT_CREATE_HOSTED_ZONE</code> </p> </li> <li> <p> <code>EXPIRED_TOKEN</code> </p> </li> <li> <p> <code>HOSTED_ZONE_NOT_FOUND</code> </p> </li> <li> <p> <code>INTERNAL_FAILURE</code> </p> </li> <li> <p> <code>INVALID_CHANGE_BATCH</code> </p> </li> <li> <p> <code>THROTTLED_REQUEST</code> </p> </li> </ul>"""
    create_date: NotRequired["capo_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date and time that the request was submitted, in Unix date/time format and Coordinated Universal Time (UTC). The value of <code>CreateDate</code> is accurate to milliseconds. For example, the value <code>1516925490.087</code> represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    update_date: NotRequired["capo_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date and time that the value of <code>Status</code> changed to the current value, in Unix date/time format and Coordinated Universal Time (UTC). The value of <code>UpdateDate</code> is accurate to milliseconds. For example, the value <code>1516925490.087</code> represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    targets: NotRequired[
        "capo_servicediscovery.types.operation_targets_map.OperationTargetsMap"
    ]
    """<p>The name of the target entity that's associated with the operation:</p> <dl> <dt>NAMESPACE</dt> <dd> <p>The namespace ID is returned in the <code>ResourceId</code> property.</p> </dd> <dt>SERVICE</dt> <dd> <p>The service ID is returned in the <code>ResourceId</code> property.</p> </dd> <dt>INSTANCE</dt> <dd> <p>The instance ID is returned in the <code>ResourceId</code> property.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Operation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    if "type" in value:
        import capo_servicediscovery.types.operation_type

        out["Type"] = capo_servicediscovery.types.operation_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "status" in value:
        import capo_servicediscovery.types.operation_status

        out["Status"] = (
            capo_servicediscovery.types.operation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "create_date" in value:
        import capo_servicediscovery.types.timestamp

        out["CreateDate"] = (
            capo_servicediscovery.types.timestamp.serialize_aws_json_1_1(
                value["create_date"]
            )
        )
    if "update_date" in value:
        import capo_servicediscovery.types.timestamp

        out["UpdateDate"] = (
            capo_servicediscovery.types.timestamp.serialize_aws_json_1_1(
                value["update_date"]
            )
        )
    if "targets" in value:
        import capo_servicediscovery.types.operation_targets_map

        out["Targets"] = (
            capo_servicediscovery.types.operation_targets_map.serialize_aws_json_1_1(
                value["targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Operation:
    out: Operation = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("OwnerAccount") is not None:
        out["owner_account"] = data["OwnerAccount"]
    if data.get("Type") is not None:
        import capo_servicediscovery.types.operation_type

        out["type"] = (
            capo_servicediscovery.types.operation_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Status") is not None:
        import capo_servicediscovery.types.operation_status

        out["status"] = (
            capo_servicediscovery.types.operation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("CreateDate") is not None:
        import capo_servicediscovery.types.timestamp

        out["create_date"] = (
            capo_servicediscovery.types.timestamp.deserialize_aws_json_1_1(
                data["CreateDate"]
            )
        )
    if data.get("UpdateDate") is not None:
        import capo_servicediscovery.types.timestamp

        out["update_date"] = (
            capo_servicediscovery.types.timestamp.deserialize_aws_json_1_1(
                data["UpdateDate"]
            )
        )
    if data.get("Targets") is not None:
        import capo_servicediscovery.types.operation_targets_map

        out["targets"] = (
            capo_servicediscovery.types.operation_targets_map.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Operation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    if "type" in value:
        import capo_servicediscovery.types.operation_type

        out["Type"] = capo_servicediscovery.types.operation_type.serialize_cbor(
            value["type"]
        )
    if "status" in value:
        import capo_servicediscovery.types.operation_status

        out["Status"] = capo_servicediscovery.types.operation_status.serialize_cbor(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "create_date" in value:
        import capo_servicediscovery.types.timestamp

        out["CreateDate"] = capo_servicediscovery.types.timestamp.serialize_cbor(
            value["create_date"]
        )
    if "update_date" in value:
        import capo_servicediscovery.types.timestamp

        out["UpdateDate"] = capo_servicediscovery.types.timestamp.serialize_cbor(
            value["update_date"]
        )
    if "targets" in value:
        import capo_servicediscovery.types.operation_targets_map

        out["Targets"] = (
            capo_servicediscovery.types.operation_targets_map.serialize_cbor(
                value["targets"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Operation:
    out: Operation = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("OwnerAccount") is not None:
        out["owner_account"] = data["OwnerAccount"]
    if data.get("Type") is not None:
        import capo_servicediscovery.types.operation_type

        out["type"] = capo_servicediscovery.types.operation_type.deserialize_cbor(
            data["Type"]
        )
    if data.get("Status") is not None:
        import capo_servicediscovery.types.operation_status

        out["status"] = capo_servicediscovery.types.operation_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("CreateDate") is not None:
        import capo_servicediscovery.types.timestamp

        out["create_date"] = capo_servicediscovery.types.timestamp.deserialize_cbor(
            data["CreateDate"]
        )
    if data.get("UpdateDate") is not None:
        import capo_servicediscovery.types.timestamp

        out["update_date"] = capo_servicediscovery.types.timestamp.deserialize_cbor(
            data["UpdateDate"]
        )
    if data.get("Targets") is not None:
        import capo_servicediscovery.types.operation_targets_map

        out["targets"] = (
            capo_servicediscovery.types.operation_targets_map.deserialize_cbor(
                data["Targets"]
            )
        )
    return out
