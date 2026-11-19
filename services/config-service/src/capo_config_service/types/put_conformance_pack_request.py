"""Generated from Smithy shape ``com.amazonaws.configservice#PutConformancePackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_input_parameters
    import capo_config_service.types.conformance_pack_name
    import capo_config_service.types.conformance_pack_scope
    import capo_config_service.types.conformance_pack_source
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
    """<p>A list of <code>ConformancePackInputParameter</code> objects. Custom conformance packs can have at most 60 input parameters. Managed conformance packs can have at most 330 input parameters.</p>"""
    template_ssm_document_details: NotRequired[
        "capo_config_service.types.template_ssm_document_details.TemplateSSMDocumentDetails"
    ]
    """<p>An object of type <code>TemplateSSMDocumentDetails</code>, which contains the name or the Amazon Resource Name (ARN) of the Amazon Web Services Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>The tags for the conformance pack. Each tag consists of a key and an optional value, both of which you define.</p>"""
    source: NotRequired[
        "capo_config_service.types.conformance_pack_source.ConformancePackSource"
    ]
    """<p>An object of type <code>ConformancePackSource</code>, which contains the identifier of the managed conformance pack that you want to deploy. If you specify a source, Config creates a managed conformance pack. Managed conformance packs are predefined collections of Config rules that are created and maintained by Amazon Web Services.</p> <note> <p>If you specify a source, you cannot specify <code>TemplateS3Uri</code>, <code>TemplateBody</code>, <code>TemplateSSMDocumentDetails</code>, <code>DeliveryS3Bucket</code>, or <code>DeliveryS3KeyPrefix</code>. You cannot convert an existing conformance pack between a managed conformance pack and a custom conformance pack. You also cannot change the source of an existing managed conformance pack.</p> </note>"""
    scope: NotRequired[
        "capo_config_service.types.conformance_pack_scope.ConformancePackScope"
    ]
    """<p>An object of type <code>ConformancePackScope</code> that defines which resources can trigger an evaluation for Config rules in the conformance pack. The scope can include a tag key and optional tag value. Specify a scope to constrain the resources that can trigger an evaluation for rules in the conformance pack. If you do not specify a scope, all rules in the conformance pack are unscoped.</p> <note> <p>This field is optional and is supported only for managed conformance packs. If you specify a scope, you must also specify <code>Source</code>.</p> </note>"""


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
    if "source" in value:
        import capo_config_service.types.conformance_pack_source

        out["Source"] = (
            capo_config_service.types.conformance_pack_source.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "scope" in value:
        import capo_config_service.types.conformance_pack_scope

        out["Scope"] = (
            capo_config_service.types.conformance_pack_scope.serialize_aws_json_1_1(
                value["scope"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConformancePackRequest:
    out: PutConformancePackRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        out["conformance_pack_name"] = ""
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
    if data.get("Source") is not None:
        import capo_config_service.types.conformance_pack_source

        out["source"] = (
            capo_config_service.types.conformance_pack_source.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    if data.get("Scope") is not None:
        import capo_config_service.types.conformance_pack_scope

        out["scope"] = (
            capo_config_service.types.conformance_pack_scope.deserialize_aws_json_1_1(
                data["Scope"]
            )
        )
    return out
