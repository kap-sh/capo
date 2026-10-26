"""Generated from Smithy shape ``com.amazonaws.healthlake#CreateDataTransformationProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.client_token
    import capo_healthlake.types.create_data_transformation_profile_source
    import capo_healthlake.types.kms_key_id
    import capo_healthlake.types.profile_description
    import capo_healthlake.types.profile_name_string
    import capo_healthlake.types.source_format
    import capo_healthlake.types.tag_map


class CreateDataTransformationProfileRequest(TypedDict, closed=True):
    source_format: "capo_healthlake.types.source_format.SourceFormat"
    """<p>The source data format that this profile converts from (Consolidated Clinical Document Architecture (C-CDA) or Comma-separated values (CSV)).</p>"""
    source: "capo_healthlake.types.create_data_transformation_profile_source.CreateDataTransformationProfileSource"
    """<p>The source for the initial profile content. Specify a built-in starter profile, an existing profile version to clone, raw profile content for CI/CD workflows, or a sample data file in Amazon S3.</p>"""
    kms_key_id: NotRequired["capo_healthlake.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key identifier used to encrypt the profile content at rest.</p>"""
    profile_description: NotRequired[
        "capo_healthlake.types.profile_description.ProfileDescription"
    ]
    """<p>A human-readable description of the profile's purpose.</p>"""
    profile_name: "capo_healthlake.types.profile_name_string.ProfileNameString"
    """<p>A name for the data transformation profile.</p>"""
    tags: NotRequired["capo_healthlake.types.tag_map.TagMap"]
    """<p>The tags to associate with the profile at creation time.</p>"""
    client_token: NotRequired["capo_healthlake.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDataTransformationProfileRequest) -> dict:
    out: dict = {}
    import capo_healthlake.types.source_format

    out["SourceFormat"] = capo_healthlake.types.source_format.serialize_aws_json_1_0(
        value["source_format"]
    )
    import capo_healthlake.types.create_data_transformation_profile_source

    out["Source"] = (
        capo_healthlake.types.create_data_transformation_profile_source.serialize_aws_json_1_0(
            value["source"]
        )
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "profile_description" in value:
        out["ProfileDescription"] = value["profile_description"]
    out["ProfileName"] = value["profile_name"]
    if "tags" in value:
        import capo_healthlake.types.tag_map

        out["Tags"] = capo_healthlake.types.tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateDataTransformationProfileRequest:
    out: CreateDataTransformationProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    else:
        import typing

        out["source_format"] = typing.cast(
            "capo_healthlake.types.source_format.SourceFormat", ""
        )
    if data.get("Source") is not None:
        import capo_healthlake.types.create_data_transformation_profile_source

        out["source"] = (
            capo_healthlake.types.create_data_transformation_profile_source.deserialize_aws_json_1_0(
                data["Source"]
            )
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ProfileDescription") is not None:
        out["profile_description"] = data["ProfileDescription"]
    if data.get("ProfileName") is not None:
        out["profile_name"] = data["ProfileName"]
    else:
        out["profile_name"] = ""
    if data.get("Tags") is not None:
        import capo_healthlake.types.tag_map

        out["tags"] = capo_healthlake.types.tag_map.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: CreateDataTransformationProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        import capo_healthlake.types.create_data_transformation_profile_source

        out["source"] = (
            capo_healthlake.types.create_data_transformation_profile_source.redact_sensitive(
                value["source"]
            )
        )
    return out
