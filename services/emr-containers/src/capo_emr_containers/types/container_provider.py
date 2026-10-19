"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ContainerProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.cluster_id
    import capo_emr_containers.types.container_info
    import capo_emr_containers.types.container_provider_type


class ContainerProvider(TypedDict, closed=True):
    type: "capo_emr_containers.types.container_provider_type.ContainerProviderType"
    """<p>The type of the container provider. Amazon EKS is the only supported type as of now.</p>"""
    id: "capo_emr_containers.types.cluster_id.ClusterId"
    """<p>The ID of the container cluster.</p>"""
    info: NotRequired["capo_emr_containers.types.container_info.ContainerInfo"]
    """<p>The information about the container cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProvider) -> dict:
    out: dict = {}
    import capo_emr_containers.types.container_provider_type

    out["type"] = capo_emr_containers.types.container_provider_type.serialize_json(
        value["type"]
    )
    out["id"] = value["id"]
    if "info" in value:
        import capo_emr_containers.types.container_info

        out["info"] = capo_emr_containers.types.container_info.serialize_json(
            value["info"]
        )
    return out


def deserialize_json(data: dict) -> ContainerProvider:
    out: ContainerProvider = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_emr_containers.types.container_provider_type

        out["type"] = (
            capo_emr_containers.types.container_provider_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_emr_containers.types.container_provider_type.ContainerProviderType",
            "",
        )
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("info") is not None:
        import capo_emr_containers.types.container_info

        out["info"] = capo_emr_containers.types.container_info.deserialize_json(
            data["info"]
        )
    return out
