"""Generated from Smithy shape ``com.amazonaws.connect#DisassociateHoursOfOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.instance_id
    import capo_connect.types.parent_hours_of_operation_id_list


class DisassociateHoursOfOperationsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier of the child hours of operation.</p>"""
    parent_hours_of_operation_ids: "capo_connect.types.parent_hours_of_operation_id_list.ParentHoursOfOperationIdList"
    """<p>The Amazon Resource Names (ARNs) of the parent hours of operation resources to disassociate with the child hours of operation resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateHoursOfOperationsRequest) -> dict:
    out: dict = {}
    import capo_connect.types.parent_hours_of_operation_id_list

    out["ParentHoursOfOperationIds"] = (
        capo_connect.types.parent_hours_of_operation_id_list.serialize_json(
            value["parent_hours_of_operation_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> DisassociateHoursOfOperationsRequest:
    out: DisassociateHoursOfOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ParentHoursOfOperationIds") is not None:
        import capo_connect.types.parent_hours_of_operation_id_list

        out["parent_hours_of_operation_ids"] = (
            capo_connect.types.parent_hours_of_operation_id_list.deserialize_json(
                data["ParentHoursOfOperationIds"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateHoursOfOperationsRequest.parent_hours_of_operation_ids required"
        )
    return out
