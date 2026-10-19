"""Generated from Smithy shape ``com.amazonaws.ecr#UploadLayerPartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.layer_part_blob
    import capo_ecr.types.part_size
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name
    import capo_ecr.types.upload_id


class UploadLayerPartRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to which you are uploading layer parts. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository to which you are uploading layer parts.</p>"""
    upload_id: "capo_ecr.types.upload_id.UploadId"
    """<p>The upload ID from a previous <a>InitiateLayerUpload</a> operation to associate with the layer part upload.</p>"""
    part_first_byte: "capo_ecr.types.part_size.PartSize"
    """<p>The position of the first byte of the layer part witin the overall image layer.</p>"""
    part_last_byte: "capo_ecr.types.part_size.PartSize"
    """<p>The position of the last byte of the layer part within the overall image layer.</p>"""
    layer_part_blob: "capo_ecr.types.layer_part_blob.LayerPartBlob"
    """<p>The base64-encoded layer part payload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadLayerPartRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    out["uploadId"] = value["upload_id"]
    out["partFirstByte"] = value["part_first_byte"]
    out["partLastByte"] = value["part_last_byte"]
    import capo_ecr.types.layer_part_blob

    out["layerPartBlob"] = capo_ecr.types.layer_part_blob.serialize_aws_json_1_1(
        value["layer_part_blob"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UploadLayerPartRequest:
    out: UploadLayerPartRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("uploadId") is not None:
        out["upload_id"] = data["uploadId"]
    else:
        out["upload_id"] = ""
    if data.get("partFirstByte") is not None:
        out["part_first_byte"] = data["partFirstByte"]
    else:
        out["part_first_byte"] = 0
    if data.get("partLastByte") is not None:
        out["part_last_byte"] = data["partLastByte"]
    else:
        out["part_last_byte"] = 0
    if data.get("layerPartBlob") is not None:
        import capo_ecr.types.layer_part_blob

        out["layer_part_blob"] = (
            capo_ecr.types.layer_part_blob.deserialize_aws_json_1_1(
                data["layerPartBlob"]
            )
        )
    else:
        out["layer_part_blob"] = b""
    return out
