"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateSegmentSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.data_format
    import capo_customer_profiles.types.encryption_key
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.role_arn
    import capo_customer_profiles.types.string1_to255


class CreateSegmentSnapshotRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The name of the segment definition used in this snapshot request.</p>"""
    data_format: "capo_customer_profiles.types.data_format.DataFormat"
    """<p>The format in which the segment will be exported.</p>"""
    encryption_key: NotRequired[
        "capo_customer_profiles.types.encryption_key.encryptionKey"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the exported segment.</p>"""
    role_arn: NotRequired["capo_customer_profiles.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that allows Customer Profiles service principal to assume the role for conducting KMS and S3 operations.</p>"""
    destination_uri: NotRequired[
        "capo_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The destination to which the segment will be exported. This field must be provided if the request is not submitted from the Connect Customer Admin Website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentSnapshotRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.data_format

    out["DataFormat"] = capo_customer_profiles.types.data_format.serialize_json(
        value["data_format"]
    )
    if "encryption_key" in value:
        out["EncryptionKey"] = value["encryption_key"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "destination_uri" in value:
        out["DestinationUri"] = value["destination_uri"]
    return out


def deserialize_json(data: dict) -> CreateSegmentSnapshotRequest:
    out: CreateSegmentSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("DataFormat") is not None:
        import capo_customer_profiles.types.data_format

        out["data_format"] = capo_customer_profiles.types.data_format.deserialize_json(
            data["DataFormat"]
        )
    else:
        import typing

        out["data_format"] = typing.cast(
            "capo_customer_profiles.types.data_format.DataFormat", ""
        )
    if data.get("EncryptionKey") is not None:
        out["encryption_key"] = data["EncryptionKey"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("DestinationUri") is not None:
        out["destination_uri"] = data["DestinationUri"]
    return out
