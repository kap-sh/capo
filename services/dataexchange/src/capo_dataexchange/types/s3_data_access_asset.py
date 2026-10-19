"""Generated from Smithy shape ``com.amazonaws.dataexchange#S3DataAccessAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string
    import capo_dataexchange.types.list_of__string
    import capo_dataexchange.types.list_of_kms_keys_to_grant


class S3DataAccessAsset(TypedDict, closed=True):
    bucket: "capo_dataexchange.types.__string.__string"
    """<p>The Amazon S3 bucket hosting data to be shared in the S3 data access.</p>"""
    key_prefixes: NotRequired["capo_dataexchange.types.list_of__string.ListOf__string"]
    """<p>The Amazon S3 bucket used for hosting shared data in the Amazon S3 data access.</p>"""
    keys: NotRequired["capo_dataexchange.types.list_of__string.ListOf__string"]
    """<p>S3 keys made available using this asset.</p>"""
    s3_access_point_alias: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The automatically-generated bucket-style alias for your Amazon S3 Access Point. Customers can access their entitled data using the S3 Access Point alias.</p>"""
    s3_access_point_arn: NotRequired["capo_dataexchange.types.__string.__string"]
    """<p>The ARN for your Amazon S3 Access Point. Customers can also access their entitled data using the S3 Access Point ARN.</p>"""
    kms_keys_to_grant: NotRequired[
        "capo_dataexchange.types.list_of_kms_keys_to_grant.ListOfKmsKeysToGrant"
    ]
    """<p> List of AWS KMS CMKs (Key Management System Customer Managed Keys) and ARNs used to encrypt S3 objects being shared in this S3 Data Access asset. Providers must include all AWS KMS keys used to encrypt these shared S3 objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DataAccessAsset) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "key_prefixes" in value:
        import capo_dataexchange.types.list_of__string

        out["KeyPrefixes"] = capo_dataexchange.types.list_of__string.serialize_json(
            value["key_prefixes"]
        )
    if "keys" in value:
        import capo_dataexchange.types.list_of__string

        out["Keys"] = capo_dataexchange.types.list_of__string.serialize_json(
            value["keys"]
        )
    if "s3_access_point_alias" in value:
        out["S3AccessPointAlias"] = value["s3_access_point_alias"]
    if "s3_access_point_arn" in value:
        out["S3AccessPointArn"] = value["s3_access_point_arn"]
    if "kms_keys_to_grant" in value:
        import capo_dataexchange.types.list_of_kms_keys_to_grant

        out["KmsKeysToGrant"] = (
            capo_dataexchange.types.list_of_kms_keys_to_grant.serialize_json(
                value["kms_keys_to_grant"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3DataAccessAsset:
    out: S3DataAccessAsset = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("KeyPrefixes") is not None:
        import capo_dataexchange.types.list_of__string

        out["key_prefixes"] = capo_dataexchange.types.list_of__string.deserialize_json(
            data["KeyPrefixes"]
        )
    if data.get("Keys") is not None:
        import capo_dataexchange.types.list_of__string

        out["keys"] = capo_dataexchange.types.list_of__string.deserialize_json(
            data["Keys"]
        )
    if data.get("S3AccessPointAlias") is not None:
        out["s3_access_point_alias"] = data["S3AccessPointAlias"]
    if data.get("S3AccessPointArn") is not None:
        out["s3_access_point_arn"] = data["S3AccessPointArn"]
    if data.get("KmsKeysToGrant") is not None:
        import capo_dataexchange.types.list_of_kms_keys_to_grant

        out["kms_keys_to_grant"] = (
            capo_dataexchange.types.list_of_kms_keys_to_grant.deserialize_json(
                data["KmsKeysToGrant"]
            )
        )
    return out
