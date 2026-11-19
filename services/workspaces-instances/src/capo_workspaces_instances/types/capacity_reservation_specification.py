"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CapacityReservationSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.capacity_reservation_preference_enum
    import capo_workspaces_instances.types.capacity_reservation_target


class CapacityReservationSpecification(TypedDict, closed=True):
    capacity_reservation_preference: NotRequired[
        "capo_workspaces_instances.types.capacity_reservation_preference_enum.CapacityReservationPreferenceEnum"
    ]
    """<p>Preference for using capacity reservation.</p>"""
    capacity_reservation_target: NotRequired[
        "capo_workspaces_instances.types.capacity_reservation_target.CapacityReservationTarget"
    ]
    """<p>Specific capacity reservation target.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityReservationSpecification) -> dict:
    out: dict = {}
    if "capacity_reservation_preference" in value:
        import capo_workspaces_instances.types.capacity_reservation_preference_enum

        out["CapacityReservationPreference"] = (
            capo_workspaces_instances.types.capacity_reservation_preference_enum.serialize_aws_json_1_0(
                value["capacity_reservation_preference"]
            )
        )
    if "capacity_reservation_target" in value:
        import capo_workspaces_instances.types.capacity_reservation_target

        out["CapacityReservationTarget"] = (
            capo_workspaces_instances.types.capacity_reservation_target.serialize_aws_json_1_0(
                value["capacity_reservation_target"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityReservationSpecification:
    out: CapacityReservationSpecification = {}  # type: ignore[typeddict-item]
    if data.get("CapacityReservationPreference") is not None:
        import capo_workspaces_instances.types.capacity_reservation_preference_enum

        out["capacity_reservation_preference"] = (
            capo_workspaces_instances.types.capacity_reservation_preference_enum.deserialize_aws_json_1_0(
                data["CapacityReservationPreference"]
            )
        )
    if data.get("CapacityReservationTarget") is not None:
        import capo_workspaces_instances.types.capacity_reservation_target

        out["capacity_reservation_target"] = (
            capo_workspaces_instances.types.capacity_reservation_target.deserialize_aws_json_1_0(
                data["CapacityReservationTarget"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CapacityReservationSpecification) -> dict:
    out: dict = {}
    if "capacity_reservation_preference" in value:
        import capo_workspaces_instances.types.capacity_reservation_preference_enum

        out["CapacityReservationPreference"] = (
            capo_workspaces_instances.types.capacity_reservation_preference_enum.serialize_cbor(
                value["capacity_reservation_preference"]
            )
        )
    if "capacity_reservation_target" in value:
        import capo_workspaces_instances.types.capacity_reservation_target

        out["CapacityReservationTarget"] = (
            capo_workspaces_instances.types.capacity_reservation_target.serialize_cbor(
                value["capacity_reservation_target"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CapacityReservationSpecification:
    out: CapacityReservationSpecification = {}  # type: ignore[typeddict-item]
    if data.get("CapacityReservationPreference") is not None:
        import capo_workspaces_instances.types.capacity_reservation_preference_enum

        out["capacity_reservation_preference"] = (
            capo_workspaces_instances.types.capacity_reservation_preference_enum.deserialize_cbor(
                data["CapacityReservationPreference"]
            )
        )
    if data.get("CapacityReservationTarget") is not None:
        import capo_workspaces_instances.types.capacity_reservation_target

        out["capacity_reservation_target"] = (
            capo_workspaces_instances.types.capacity_reservation_target.deserialize_cbor(
                data["CapacityReservationTarget"]
            )
        )
    return out
