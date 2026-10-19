"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CreateDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.client_token
    import capo_medical_imaging.types.datastore_name
    import capo_medical_imaging.types.kms_key_arn
    import capo_medical_imaging.types.lambda_arn
    import capo_medical_imaging.types.lossless_storage_format
    import capo_medical_imaging.types.tag_map


class CreateDatastoreRequest(TypedDict, closed=True):
    datastore_name: NotRequired[
        "capo_medical_imaging.types.datastore_name.DatastoreName"
    ]
    """<p>The data store name.</p>"""
    client_token: "capo_medical_imaging.types.client_token.ClientToken"
    """<p>A unique identifier for API idempotency.</p>"""
    tags: NotRequired["capo_medical_imaging.types.tag_map.TagMap"]
    """<p>The tags provided when creating a data store.</p>"""
    kms_key_arn: NotRequired["capo_medical_imaging.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>"""
    lambda_authorizer_arn: NotRequired[
        "capo_medical_imaging.types.lambda_arn.LambdaArn"
    ]
    """<p>The ARN of the authorizer's Lambda function.</p>"""
    lossless_storage_format: NotRequired[
        "capo_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
    ]
    """<p>The lossless storage format for the datastore.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatastoreRequest) -> dict:
    out: dict = {}
    if "datastore_name" in value:
        out["datastoreName"] = value["datastore_name"]
    out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_medical_imaging.types.tag_map

        out["tags"] = capo_medical_imaging.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "lambda_authorizer_arn" in value:
        out["lambdaAuthorizerArn"] = value["lambda_authorizer_arn"]
    if "lossless_storage_format" in value:
        import capo_medical_imaging.types.lossless_storage_format

        out["losslessStorageFormat"] = (
            capo_medical_imaging.types.lossless_storage_format.serialize_json(
                value["lossless_storage_format"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDatastoreRequest:
    out: CreateDatastoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("datastoreName") is not None:
        out["datastore_name"] = data["datastoreName"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("tags") is not None:
        import capo_medical_imaging.types.tag_map

        out["tags"] = capo_medical_imaging.types.tag_map.deserialize_json(data["tags"])
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("lambdaAuthorizerArn") is not None:
        out["lambda_authorizer_arn"] = data["lambdaAuthorizerArn"]
    if data.get("losslessStorageFormat") is not None:
        import capo_medical_imaging.types.lossless_storage_format

        out["lossless_storage_format"] = (
            capo_medical_imaging.types.lossless_storage_format.deserialize_json(
                data["losslessStorageFormat"]
            )
        )
    return out
