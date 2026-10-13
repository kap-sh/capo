"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterClusters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.matter_cluster

MatterClusters: TypeAlias = list[
    "capo_iot_managed_integrations.types.matter_cluster.MatterCluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterClusters) -> list:
    import capo_iot_managed_integrations.types.matter_cluster

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.matter_cluster.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MatterClusters:
    import capo_iot_managed_integrations.types.matter_cluster

    out: MatterClusters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.matter_cluster.deserialize_json(item)
        )
    return out


def redact_sensitive(value: MatterClusters) -> list[Any]:
    import capo_iot_managed_integrations.types.matter_cluster

    return [
        capo_iot_managed_integrations.types.matter_cluster.redact_sensitive(item)
        for item in value
    ]
