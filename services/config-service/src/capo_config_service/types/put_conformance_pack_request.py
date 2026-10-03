"""Generated from Smithy shape ``com.amazonaws.configservice#PutConformancePackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_input_parameters
    import capo_config_service.types.conformance_pack_name
    import capo_config_service.types.delivery_s3_bucket
    import capo_config_service.types.delivery_s3_key_prefix
    import capo_config_service.types.tags_list
    import capo_config_service.types.template_body
    import capo_config_service.types.template_s3_uri
    import capo_config_service.types.template_ssm_document_details


class PutConformancePackRequest(TypedDict, closed=True):
    conformance_pack_name: (
        "capo_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>The unique name of the conformance pack you want to deploy.</p>"""
    template_s3_uri: NotRequired[
        "capo_config_service.types.template_s3_uri.TemplateS3Uri"
    ]
    """<p>The location of the file containing the template body (<code>s3://bucketname/prefix</code>). The uri must point to a conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket in the same Region as the conformance pack. </p> <note> <p>You must have access to read Amazon S3 bucket. In addition, in order to ensure a successful deployment, the template object must not be in an <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html">archived storage class</a> if this parameter is passed.</p> </note>"""
    template_body: NotRequired["capo_config_service.types.template_body.TemplateBody"]
    """<p>A string that contains the full conformance pack template body. The structure containing the template body has a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <note> <p>You can use a YAML template with two resource types: Config rule (<code>AWS::Config::ConfigRule</code>) and remediation action (<code>AWS::Config::RemediationConfiguration</code>).</p> </note>"""
    delivery_s3_bucket: NotRequired[
        "capo_config_service.types.delivery_s3_bucket.DeliveryS3Bucket"
    ]
    """<p>The name of the Amazon S3 bucket where Config stores conformance pack templates.</p> <note> <p>This field is optional.</p> </note>"""
    delivery_s3_key_prefix: NotRequired[
        "capo_config_service.types.delivery_s3_key_prefix.DeliveryS3KeyPrefix"
    ]
    """<p>The prefix for the Amazon S3 bucket. </p> <note> <p>This field is optional.</p> </note>"""
    conformance_pack_input_parameters: NotRequired[
        "capo_config_service.types.conformance_pack_input_parameters.ConformancePackInputParameters"
    ]
    """<p>A list of <code>ConformancePackInputParameter</code> objects.</p>"""
    template_ssm_document_details: NotRequired[
        "capo_config_service.types.template_ssm_document_details.TemplateSSMDocumentDetails"
    ]
    """<p>An object of type <code>TemplateSSMDocumentDetails</code>, which contains the name or the Amazon Resource Name (ARN) of the Amazon Web Services Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>The tags for the conformance pack. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConformancePackRequest) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
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
    if "template_ssm_document_details" in value:
        import capo_config_service.types.template_ssm_document_details

        out["TemplateSSMDocumentDetails"] = (
            capo_config_service.types.template_ssm_document_details.serialize_aws_json_1_1(
                value["template_ssm_document_details"]
            )
        )
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConformancePackRequest:
    out: PutConformancePackRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        raise DeserializationError(
            "PutConformancePackRequest.conformance_pack_name required"
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
    if data.get("TemplateSSMDocumentDetails") is not None:
        import capo_config_service.types.template_ssm_document_details

        out["template_ssm_document_details"] = (
            capo_config_service.types.template_ssm_document_details.deserialize_aws_json_1_1(
                data["TemplateSSMDocumentDetails"]
            )
        )
    if data.get("Tags") is not None:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
