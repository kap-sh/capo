"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_arn
    import capo_config_service.types.conformance_pack_id
    import capo_config_service.types.conformance_pack_input_parameters
    import capo_config_service.types.conformance_pack_name
    import capo_config_service.types.date
    import capo_config_service.types.delivery_s3_bucket
    import capo_config_service.types.delivery_s3_key_prefix
    import capo_config_service.types.string_with_char_limit256
    import capo_config_service.types.template_ssm_document_details


class ConformancePackDetail(TypedDict, closed=True):
    conformance_pack_name: (
        "capo_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack.</p>"""
    conformance_pack_arn: (
        "capo_config_service.types.conformance_pack_arn.ConformancePackArn"
    )
    """<p>Amazon Resource Name (ARN) of the conformance pack.</p>"""
    conformance_pack_id: (
        "capo_config_service.types.conformance_pack_id.ConformancePackId"
    )
    """<p>ID of the conformance pack.</p>"""
    delivery_s3_bucket: NotRequired[
        "capo_config_service.types.delivery_s3_bucket.DeliveryS3Bucket"
    ]
    """<p>The name of the Amazon S3 bucket where Config stores conformance pack templates. </p> <note> <p>This field is optional.</p> </note>"""
    delivery_s3_key_prefix: NotRequired[
        "capo_config_service.types.delivery_s3_key_prefix.DeliveryS3KeyPrefix"
    ]
    """<p>The prefix for the Amazon S3 bucket.</p> <note> <p>This field is optional.</p> </note>"""
    conformance_pack_input_parameters: NotRequired[
        "capo_config_service.types.conformance_pack_input_parameters.ConformancePackInputParameters"
    ]
    """<p>A list of <code>ConformancePackInputParameter</code> objects.</p>"""
    last_update_requested_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The last time a conformation pack update was requested. </p>"""
    created_by: NotRequired[
        "capo_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    ]
    """<p>The Amazon Web Services service that created the conformance pack.</p>"""
    template_ssm_document_details: NotRequired[
        "capo_config_service.types.template_ssm_document_details.TemplateSSMDocumentDetails"
    ]
    """<p>An object that contains the name or Amazon Resource Name (ARN) of the Amazon Web Services Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackDetail) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    out["ConformancePackArn"] = value["conformance_pack_arn"]
    out["ConformancePackId"] = value["conformance_pack_id"]
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
    if "last_update_requested_time" in value:
        import capo_config_service.types.date

        out["LastUpdateRequestedTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_update_requested_time"]
            )
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "template_ssm_document_details" in value:
        import capo_config_service.types.template_ssm_document_details

        out["TemplateSSMDocumentDetails"] = (
            capo_config_service.types.template_ssm_document_details.serialize_aws_json_1_1(
                value["template_ssm_document_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackDetail:
    out: ConformancePackDetail = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        out["conformance_pack_name"] = ""
    if data.get("ConformancePackArn") is not None:
        out["conformance_pack_arn"] = data["ConformancePackArn"]
    else:
        out["conformance_pack_arn"] = ""
    if data.get("ConformancePackId") is not None:
        out["conformance_pack_id"] = data["ConformancePackId"]
    else:
        out["conformance_pack_id"] = ""
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
    if data.get("LastUpdateRequestedTime") is not None:
        import capo_config_service.types.date

        out["last_update_requested_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateRequestedTime"]
            )
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("TemplateSSMDocumentDetails") is not None:
        import capo_config_service.types.template_ssm_document_details

        out["template_ssm_document_details"] = (
            capo_config_service.types.template_ssm_document_details.deserialize_aws_json_1_1(
                data["TemplateSSMDocumentDetails"]
            )
        )
    return out
