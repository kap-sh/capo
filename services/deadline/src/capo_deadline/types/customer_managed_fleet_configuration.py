"""Generated from Smithy shape ``com.amazonaws.deadline#CustomerManagedFleetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.auto_scaling_mode
    import capo_deadline.types.customer_managed_auto_scaling_configuration
    import capo_deadline.types.customer_managed_worker_capabilities
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.tag_propagation_mode


class CustomerManagedFleetConfiguration(TypedDict, closed=True):
    mode: "capo_deadline.types.auto_scaling_mode.AutoScalingMode"
    """The Auto Scaling mode for the customer managed fleet."""
    auto_scaling_configuration: NotRequired[
        "capo_deadline.types.customer_managed_auto_scaling_configuration.CustomerManagedAutoScalingConfiguration"
    ]
    """The auto scaling configuration settings for the customer managed fleet."""
    worker_capabilities: "capo_deadline.types.customer_managed_worker_capabilities.CustomerManagedWorkerCapabilities"
    """The worker capabilities for the customer managed fleet."""
    storage_profile_id: NotRequired[
        "capo_deadline.types.storage_profile_id.StorageProfileId"
    ]
    """The storage profile ID for the customer managed fleet."""
    tag_propagation_mode: NotRequired[
        "capo_deadline.types.tag_propagation_mode.TagPropagationMode"
    ]
    """The tag propagation mode for the customer managed fleet."""


# --- restJson1 ser/de ---
def serialize_json(value: CustomerManagedFleetConfiguration) -> dict:
    out: dict = {}
    import capo_deadline.types.auto_scaling_mode

    out["mode"] = capo_deadline.types.auto_scaling_mode.serialize_json(value["mode"])
    if "auto_scaling_configuration" in value:
        import capo_deadline.types.customer_managed_auto_scaling_configuration

        out["autoScalingConfiguration"] = (
            capo_deadline.types.customer_managed_auto_scaling_configuration.serialize_json(
                value["auto_scaling_configuration"]
            )
        )
    import capo_deadline.types.customer_managed_worker_capabilities

    out["workerCapabilities"] = (
        capo_deadline.types.customer_managed_worker_capabilities.serialize_json(
            value["worker_capabilities"]
        )
    )
    if "storage_profile_id" in value:
        out["storageProfileId"] = value["storage_profile_id"]
    if "tag_propagation_mode" in value:
        import capo_deadline.types.tag_propagation_mode

        out["tagPropagationMode"] = (
            capo_deadline.types.tag_propagation_mode.serialize_json(
                value["tag_propagation_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomerManagedFleetConfiguration:
    out: CustomerManagedFleetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_deadline.types.auto_scaling_mode

        out["mode"] = capo_deadline.types.auto_scaling_mode.deserialize_json(
            data["mode"]
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_deadline.types.auto_scaling_mode.AutoScalingMode", ""
        )
    if data.get("autoScalingConfiguration") is not None:
        import capo_deadline.types.customer_managed_auto_scaling_configuration

        out["auto_scaling_configuration"] = (
            capo_deadline.types.customer_managed_auto_scaling_configuration.deserialize_json(
                data["autoScalingConfiguration"]
            )
        )
    if data.get("workerCapabilities") is not None:
        import capo_deadline.types.customer_managed_worker_capabilities

        out["worker_capabilities"] = (
            capo_deadline.types.customer_managed_worker_capabilities.deserialize_json(
                data["workerCapabilities"]
            )
        )
    else:
        raise DeserializationError(
            "CustomerManagedFleetConfiguration.worker_capabilities required"
        )
    if data.get("storageProfileId") is not None:
        out["storage_profile_id"] = data["storageProfileId"]
    if data.get("tagPropagationMode") is not None:
        import capo_deadline.types.tag_propagation_mode

        out["tag_propagation_mode"] = (
            capo_deadline.types.tag_propagation_mode.deserialize_json(
                data["tagPropagationMode"]
            )
        )
    return out
