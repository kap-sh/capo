"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CapacityReservationTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.arn
    import capo_workspaces_instances.types.string128


class CapacityReservationTarget(TypedDict, closed=True):
    capacity_reservation_id: NotRequired[
        "capo_workspaces_instances.types.string128.String128"
    ]
    """<p>Unique identifier for the capacity reservation.</p>"""
    capacity_reservation_resource_group_arn: NotRequired[
        "capo_workspaces_instances.types.arn.ARN"
    ]
    """<p>ARN of the capacity reservation resource group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityReservationTarget) -> dict:
    out: dict = {}
    if "capacity_reservation_id" in value:
        out["CapacityReservationId"] = value["capacity_reservation_id"]
    if "capacity_reservation_resource_group_arn" in value:
        out["CapacityReservationResourceGroupArn"] = value[
            "capacity_reservation_resource_group_arn"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityReservationTarget:
    out: CapacityReservationTarget = {}  # type: ignore[typeddict-item]
    if data.get("CapacityReservationId") is not None:
        out["capacity_reservation_id"] = data["CapacityReservationId"]
    if data.get("CapacityReservationResourceGroupArn") is not None:
        out["capacity_reservation_resource_group_arn"] = data[
            "CapacityReservationResourceGroupArn"
        ]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CapacityReservationTarget) -> dict:
    out: dict = {}
    if "capacity_reservation_id" in value:
        out["CapacityReservationId"] = value["capacity_reservation_id"]
    if "capacity_reservation_resource_group_arn" in value:
        out["CapacityReservationResourceGroupArn"] = value[
            "capacity_reservation_resource_group_arn"
        ]
    return out


def deserialize_cbor(data: dict) -> CapacityReservationTarget:
    out: CapacityReservationTarget = {}  # type: ignore[typeddict-item]
    if data.get("CapacityReservationId") is not None:
        out["capacity_reservation_id"] = data["CapacityReservationId"]
    if data.get("CapacityReservationResourceGroupArn") is not None:
        out["capacity_reservation_resource_group_arn"] = data[
            "CapacityReservationResourceGroupArn"
        ]
    return out
