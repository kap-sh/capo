"""Generated from Smithy shape ``com.amazonaws.macie2#S3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__boolean
    import capo_macie2.types.__long
    import capo_macie2.types.__string
    import capo_macie2.types.__timestamp_iso8601
    import capo_macie2.types.key_value_pair_list
    import capo_macie2.types.server_side_encryption
    import capo_macie2.types.storage_class


class S3Object(TypedDict, closed=True):
    bucket_arn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the bucket that contains the object.</p>"""
    e_tag: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The entity tag (ETag) that identifies the affected version of the object. If the object was overwritten or changed after Amazon Macie produced the finding, this value might be different from the current ETag for the object.</p>"""
    extension: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The file name extension of the object. If the object doesn't have a file name extension, this value is "".</p>"""
    key: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The full name (<i>key</i>) of the object, including the object's prefix if applicable.</p>"""
    last_modified: NotRequired[
        "capo_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the object was last modified.</p>"""
    path: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The full path to the affected object, including the name of the affected bucket and the object's name (key).</p>"""
    public_access: NotRequired["capo_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the object is publicly accessible due to the combination of permissions settings that apply to the object.</p>"""
    server_side_encryption: NotRequired[
        "capo_macie2.types.server_side_encryption.ServerSideEncryption"
    ]
    """<p>The type of server-side encryption that was used to encrypt the object.</p>"""
    size: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total storage size, in bytes, of the object.</p>"""
    storage_class: NotRequired["capo_macie2.types.storage_class.StorageClass"]
    """<p>The storage class of the object.</p>"""
    tags: NotRequired["capo_macie2.types.key_value_pair_list.KeyValuePairList"]
    """<p>The tags that are associated with the object.</p>"""
    version_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The identifier for the affected version of the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Object) -> dict:
    out: dict = {}
    if "bucket_arn" in value:
        out["bucketArn"] = value["bucket_arn"]
    if "e_tag" in value:
        out["eTag"] = value["e_tag"]
    if "extension" in value:
        out["extension"] = value["extension"]
    if "key" in value:
        out["key"] = value["key"]
    if "last_modified" in value:
        import capo_macie2.types.__timestamp_iso8601

        out["lastModified"] = capo_macie2.types.__timestamp_iso8601.serialize_json(
            value["last_modified"]
        )
    if "path" in value:
        out["path"] = value["path"]
    if "public_access" in value:
        out["publicAccess"] = value["public_access"]
    if "server_side_encryption" in value:
        import capo_macie2.types.server_side_encryption

        out["serverSideEncryption"] = (
            capo_macie2.types.server_side_encryption.serialize_json(
                value["server_side_encryption"]
            )
        )
    if "size" in value:
        out["size"] = value["size"]
    if "storage_class" in value:
        import capo_macie2.types.storage_class

        out["storageClass"] = capo_macie2.types.storage_class.serialize_json(
            value["storage_class"]
        )
    if "tags" in value:
        import capo_macie2.types.key_value_pair_list

        out["tags"] = capo_macie2.types.key_value_pair_list.serialize_json(
            value["tags"]
        )
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if data.get("bucketArn") is not None:
        out["bucket_arn"] = data["bucketArn"]
    if data.get("eTag") is not None:
        out["e_tag"] = data["eTag"]
    if data.get("extension") is not None:
        out["extension"] = data["extension"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("lastModified") is not None:
        import capo_macie2.types.__timestamp_iso8601

        out["last_modified"] = capo_macie2.types.__timestamp_iso8601.deserialize_json(
            data["lastModified"]
        )
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("publicAccess") is not None:
        out["public_access"] = data["publicAccess"]
    if data.get("serverSideEncryption") is not None:
        import capo_macie2.types.server_side_encryption

        out["server_side_encryption"] = (
            capo_macie2.types.server_side_encryption.deserialize_json(
                data["serverSideEncryption"]
            )
        )
    if data.get("size") is not None:
        out["size"] = data["size"]
    if data.get("storageClass") is not None:
        import capo_macie2.types.storage_class

        out["storage_class"] = capo_macie2.types.storage_class.deserialize_json(
            data["storageClass"]
        )
    if data.get("tags") is not None:
        import capo_macie2.types.key_value_pair_list

        out["tags"] = capo_macie2.types.key_value_pair_list.deserialize_json(
            data["tags"]
        )
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    return out
