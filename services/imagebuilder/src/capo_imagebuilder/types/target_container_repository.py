"""Generated from Smithy shape ``com.amazonaws.imagebuilder#TargetContainerRepository``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.container_repository_service
    import capo_imagebuilder.types.non_empty_string


class TargetContainerRepository(TypedDict, closed=True):
    service: "capo_imagebuilder.types.container_repository_service.ContainerRepositoryService"
    """<p>Specifies the service in which this image was registered.</p>"""
    repository_name: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The name of the container repository where the output container image is stored. Provide the repository name only (a namespace path such as <code>team-a/my-repo</code> is allowed, but not the registry hostname).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetContainerRepository) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.container_repository_service

    out["service"] = (
        capo_imagebuilder.types.container_repository_service.serialize_json(
            value["service"]
        )
    )
    out["repositoryName"] = value["repository_name"]
    return out


def deserialize_json(data: dict) -> TargetContainerRepository:
    out: TargetContainerRepository = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_imagebuilder.types.container_repository_service

        out["service"] = (
            capo_imagebuilder.types.container_repository_service.deserialize_json(
                data["service"]
            )
        )
    else:
        import typing

        out["service"] = typing.cast(
            "capo_imagebuilder.types.container_repository_service.ContainerRepositoryService",
            "",
        )
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    return out
