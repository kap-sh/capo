"""Generated from Smithy shape ``com.amazonaws.emrcontainers#UpdateVirtualClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.client_token
    import capo_emr_containers.types.resource_id_string
    import capo_emr_containers.types.scheduler_configuration


class UpdateVirtualClusterRequest(TypedDict, closed=True):
    id: "capo_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the virtual cluster to update.</p>"""
    scheduler_configuration: NotRequired[
        "capo_emr_containers.types.scheduler_configuration.SchedulerConfiguration"
    ]
    """<p>The scheduler configuration to apply to the virtual cluster. The new configuration fully replaces the existing one. If you omit a field, the corresponding limit is removed.</p>"""
    client_token: "capo_emr_containers.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVirtualClusterRequest) -> dict:
    out: dict = {}
    if "scheduler_configuration" in value:
        import capo_emr_containers.types.scheduler_configuration

        out["schedulerConfiguration"] = (
            capo_emr_containers.types.scheduler_configuration.serialize_json(
                value["scheduler_configuration"]
            )
        )
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateVirtualClusterRequest:
    out: UpdateVirtualClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("schedulerConfiguration") is not None:
        import capo_emr_containers.types.scheduler_configuration

        out["scheduler_configuration"] = (
            capo_emr_containers.types.scheduler_configuration.deserialize_json(
                data["schedulerConfiguration"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out
