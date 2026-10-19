"""Generated from Smithy shape ``com.amazonaws.ecrpublic#BatchCheckLayerAvailabilityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.batched_operation_layer_digest_list
    import capo_ecr_public.types.registry_id_or_alias
    import capo_ecr_public.types.repository_name


class BatchCheckLayerAvailabilityRequest(TypedDict, closed=True):
    registry_id: NotRequired[
        "capo_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
    ]
    """<p>The Amazon Web Services account ID, or registry alias, associated with the public registry that contains the image layers to check. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "capo_ecr_public.types.repository_name.RepositoryName"
    """<p>The name of the repository that's associated with the image layers to check.</p>"""
    layer_digests: "capo_ecr_public.types.batched_operation_layer_digest_list.BatchedOperationLayerDigestList"
    """<p>The digests of the image layers to check.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCheckLayerAvailabilityRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import capo_ecr_public.types.batched_operation_layer_digest_list

    out["layerDigests"] = (
        capo_ecr_public.types.batched_operation_layer_digest_list.serialize_aws_json_1_1(
            value["layer_digests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCheckLayerAvailabilityRequest:
    out: BatchCheckLayerAvailabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("layerDigests") is not None:
        import capo_ecr_public.types.batched_operation_layer_digest_list

        out["layer_digests"] = (
            capo_ecr_public.types.batched_operation_layer_digest_list.deserialize_aws_json_1_1(
                data["layerDigests"]
            )
        )
    else:
        out["layer_digests"] = []
    return out
