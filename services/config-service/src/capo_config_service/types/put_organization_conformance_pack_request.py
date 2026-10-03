"""Generated from Smithy shape ``com.amazonaws.configservice#PutOrganizationConformancePackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_input_parameters
    import capo_config_service.types.delivery_s3_bucket
    import capo_config_service.types.delivery_s3_key_prefix
    import capo_config_service.types.excluded_accounts
    import capo_config_service.types.organization_conformance_pack_name
    import capo_config_service.types.tags_list
    import capo_config_service.types.template_body
    import capo_config_service.types.template_s3_uri


class PutOrganizationConformancePackRequest(TypedDict, closed=True):
    organization_conformance_pack_name: "capo_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName"
    """<p>Name of the organization conformance pack you want to create.</p>"""
    template_s3_uri: NotRequired[
        "capo_config_service.types.template_s3_uri.TemplateS3Uri"
    ]
    """<p>Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).</p> <note> <p>You must have access to read Amazon S3 bucket. In addition, in order to ensure a successful deployment, the template object must not be in an <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html">archived storage class</a> if this parameter is passed.</p> </note>"""
    template_body: NotRequired["capo_config_service.types.template_body.TemplateBody"]
    """<p>A string that contains the full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p>"""
    delivery_s3_bucket: NotRequired[
        "capo_config_service.types.delivery_s3_bucket.DeliveryS3Bucket"
    ]
    """<p>The name of the Amazon S3 bucket where Config stores conformance pack templates.</p> <note> <p>This field is optional. If used, it must be prefixed with <code>awsconfigconforms</code>.</p> </note>"""
    delivery_s3_key_prefix: NotRequired[
        "capo_config_service.types.delivery_s3_key_prefix.DeliveryS3KeyPrefix"
    ]
    """<p>The prefix for the Amazon S3 bucket.</p> <note> <p>This field is optional.</p> </note>"""
    conformance_pack_input_parameters: NotRequired[
        "capo_config_service.types.conformance_pack_input_parameters.ConformancePackInputParameters"
    ]
    """<p>A list of <code>ConformancePackInputParameter</code> objects.</p>"""
    excluded_accounts: NotRequired[
        "capo_config_service.types.excluded_accounts.ExcludedAccounts"
    ]
    """<p>A list of Amazon Web Services accounts to be excluded from an organization conformance pack while deploying a conformance pack.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>The tags for the organization conformance pack. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutOrganizationConformancePackRequest) -> dict:
    out: dict = {}
    out["OrganizationConformancePackName"] = value["organization_conformance_pack_name"]
    if "template_s3_uri" in value:
        out["TemplateS3Uri"] = value["template_s3_uri"]
    if "template_body" in value:
        out["TemplateBody"] = value["template_body"]
    if "delivery_s3_bucket" in value:
        out["DeliveryS3Bucket"] = value["delivery_s3_bucket"]
    if "delivery_s3_key_prefix" in value:
        out["DeliveryS3KeyPrefix"] = value["delivery_s3_key_prefix"]
    if "conformance_pack_input_parameters" in value:
        import capo_config_service.types.conformance_pack_input_parameters

        out["ConformancePackInputParameters"] = (
            capo_config_service.types.conformance_pack_input_parameters.serialize_aws_json_1_1(
                value["conformance_pack_input_parameters"]
            )
        )
    if "excluded_accounts" in value:
        import capo_config_service.types.excluded_accounts

        out["ExcludedAccounts"] = (
            capo_config_service.types.excluded_accounts.serialize_aws_json_1_1(
                value["excluded_accounts"]
            )
        )
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutOrganizationConformancePackRequest:
    out: PutOrganizationConformancePackRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationConformancePackName") is not None:
        out["organization_conformance_pack_name"] = data[
            "OrganizationConformancePackName"
        ]
    else:
        raise DeserializationError(
            "PutOrganizationConformancePackRequest.organization_conformance_pack_name required"
        )
    if data.get("TemplateS3Uri") is not None:
        out["template_s3_uri"] = data["TemplateS3Uri"]
    if data.get("TemplateBody") is not None:
        out["template_body"] = data["TemplateBody"]
    if data.get("DeliveryS3Bucket") is not None:
        out["delivery_s3_bucket"] = data["DeliveryS3Bucket"]
    if data.get("DeliveryS3KeyPrefix") is not None:
        out["delivery_s3_key_prefix"] = data["DeliveryS3KeyPrefix"]
    if data.get("ConformancePackInputParameters") is not None:
        import capo_config_service.types.conformance_pack_input_parameters

        out["conformance_pack_input_parameters"] = (
            capo_config_service.types.conformance_pack_input_parameters.deserialize_aws_json_1_1(
                data["ConformancePackInputParameters"]
            )
        )
    if data.get("ExcludedAccounts") is not None:
        import capo_config_service.types.excluded_accounts

        out["excluded_accounts"] = (
            capo_config_service.types.excluded_accounts.deserialize_aws_json_1_1(
                data["ExcludedAccounts"]
            )
        )
    if data.get("Tags") is not None:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
