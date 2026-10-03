"""Generated from Smithy shape ``com.amazonaws.kms#DeleteImportedKeyMaterialResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kms.types.backing_key_id_response_type
    import capo_kms.types.key_id_type


class DeleteImportedKeyMaterialResponse(TypedDict, closed=True):
    key_id: NotRequired["capo_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">key ARN</a>) of the KMS key from which the key material was deleted.</p>"""
    key_material_id: NotRequired[
        "capo_kms.types.backing_key_id_response_type.BackingKeyIdResponseType"
    ]
    """<p>Identifies the deleted key material.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteImportedKeyMaterialResponse) -> dict:
    out: dict = {}
    if "key_id" in value:
        out["KeyId"] = value["key_id"]
    if "key_material_id" in value:
        out["KeyMaterialId"] = value["key_material_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteImportedKeyMaterialResponse:
    out: DeleteImportedKeyMaterialResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyId") is not None:
        out["key_id"] = data["KeyId"]
    if data.get("KeyMaterialId") is not None:
        out["key_material_id"] = data["KeyMaterialId"]
    return out
