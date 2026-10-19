"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DatastoreProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.arn
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.datastore_name
    import capo_medical_imaging.types.datastore_status
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.kms_key_arn
    import capo_medical_imaging.types.lambda_arn
    import capo_medical_imaging.types.lossless_storage_format


class DatastoreProperties(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_name: "capo_medical_imaging.types.datastore_name.DatastoreName"
    """<p>The data store name.</p>"""
    datastore_status: "capo_medical_imaging.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""
    kms_key_arn: NotRequired["capo_medical_imaging.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) assigned to the Key Management Service (KMS) key for accessing encrypted data.</p>"""
    lambda_authorizer_arn: NotRequired[
        "capo_medical_imaging.types.lambda_arn.LambdaArn"
    ]
    """<p>The ARN of the authorizer's Lambda function.</p>"""
    lossless_storage_format: NotRequired[
        "capo_medical_imaging.types.lossless_storage_format.LosslessStorageFormat"
    ]
    """<p>The datastore's lossless storage format.</p>"""
    datastore_arn: NotRequired["capo_medical_imaging.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the data store.</p>"""
    created_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the data store was created.</p>"""
    updated_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the data store was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatastoreProperties) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["datastoreName"] = value["datastore_name"]
    import capo_medical_imaging.types.datastore_status

    out["datastoreStatus"] = capo_medical_imaging.types.datastore_status.serialize_json(
        value["datastore_status"]
    )
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
    if "datastore_arn" in value:
        out["datastoreArn"] = value["datastore_arn"]
    if "created_at" in value:
        import capo_medical_imaging.types.date

        out["createdAt"] = capo_medical_imaging.types.date.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_medical_imaging.types.date

        out["updatedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> DatastoreProperties:
    out: DatastoreProperties = {}  # type: ignore[typeddict-item]
    if data.get("datastoreId") is not None:
        out["datastore_id"] = data["datastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("datastoreName") is not None:
        out["datastore_name"] = data["datastoreName"]
    else:
        out["datastore_name"] = ""
    if data.get("datastoreStatus") is not None:
        import capo_medical_imaging.types.datastore_status

        out["datastore_status"] = (
            capo_medical_imaging.types.datastore_status.deserialize_json(
                data["datastoreStatus"]
            )
        )
    else:
        import typing

        out["datastore_status"] = typing.cast(
            "capo_medical_imaging.types.datastore_status.DatastoreStatus", ""
        )
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
    if data.get("datastoreArn") is not None:
        out["datastore_arn"] = data["datastoreArn"]
    if data.get("createdAt") is not None:
        import capo_medical_imaging.types.date

        out["created_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_medical_imaging.types.date

        out["updated_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["updatedAt"]
        )
    return out
