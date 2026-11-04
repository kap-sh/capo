"""Generated from Smithy shape ``com.amazonaws.omics#ContainerRegistryMap``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.image_mappings_list
    import capo_omics.types.registry_mappings_list


class ContainerRegistryMap(TypedDict, closed=True):
    registry_mappings: NotRequired[
        "capo_omics.types.registry_mappings_list.RegistryMappingsList"
    ]
    """<p>Mapping that provides the ECR repository path where upstream container images are pulled and synchronized.</p>"""
    image_mappings: NotRequired[
        "capo_omics.types.image_mappings_list.ImageMappingsList"
    ]
    """<p>Image mappings specify path mappings between the ECR private repository and their corresponding external repositories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRegistryMap) -> dict:
    out: dict = {}
    if "registry_mappings" in value:
        import capo_omics.types.registry_mappings_list

        out["registryMappings"] = (
            capo_omics.types.registry_mappings_list.serialize_json(
                value["registry_mappings"]
            )
        )
    if "image_mappings" in value:
        import capo_omics.types.image_mappings_list

        out["imageMappings"] = capo_omics.types.image_mappings_list.serialize_json(
            value["image_mappings"]
        )
    return out


def deserialize_json(data: dict) -> ContainerRegistryMap:
    out: ContainerRegistryMap = {}  # type: ignore[typeddict-item]
    if data.get("registryMappings") is not None:
        import capo_omics.types.registry_mappings_list

        out["registry_mappings"] = (
            capo_omics.types.registry_mappings_list.deserialize_json(
                data["registryMappings"]
            )
        )
    if data.get("imageMappings") is not None:
        import capo_omics.types.image_mappings_list

        out["image_mappings"] = capo_omics.types.image_mappings_list.deserialize_json(
            data["imageMappings"]
        )
    return out
