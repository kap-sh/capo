"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DistributeImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.distribution_configuration_arn
    import capo_imagebuilder.types.image_logging_configuration
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.role_name_or_arn
    import capo_imagebuilder.types.tag_map


class DistributeImageRequest(TypedDict, closed=True):
    source_image: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The source image to distribute. You can specify the source in any of the following formats:</p> <ul> <li> <p>An AMI ID.</p> </li> <li> <p>An Amazon Web Services Systems Manager Parameter Store reference, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> </li> <li> <p>An Image Builder image Amazon Resource Name (ARN). An image version ARN resolves to the latest available build version.</p> </li> </ul> <p>Whichever format you use, the source must resolve to an AMI in the current Amazon Web Services Region.</p>"""
    distribution_configuration_arn: "capo_imagebuilder.types.distribution_configuration_arn.DistributionConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the distribution configuration. The configuration defines target Regions, accounts, and AMI settings. The distribution configuration must be in the same Region as this operation.</p>"""
    execution_role: "capo_imagebuilder.types.role_name_or_arn.RoleNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the IAM role that Image Builder assumes to distribute the image.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags to apply to the new Image Builder image resource that this operation creates. To tag the output AMIs, use <code>amiTags</code> in the distribution configuration.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    logging_configuration: NotRequired[
        "capo_imagebuilder.types.image_logging_configuration.ImageLoggingConfiguration"
    ]
    """<p>The logging configuration for the distribution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DistributeImageRequest) -> dict:
    out: dict = {}
    out["sourceImage"] = value["source_image"]
    out["distributionConfigurationArn"] = value["distribution_configuration_arn"]
    out["executionRole"] = value["execution_role"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    if "logging_configuration" in value:
        import capo_imagebuilder.types.image_logging_configuration

        out["loggingConfiguration"] = (
            capo_imagebuilder.types.image_logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DistributeImageRequest:
    out: DistributeImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceImage") is not None:
        out["source_image"] = data["sourceImage"]
    else:
        raise DeserializationError("DistributeImageRequest.source_image required")
    if data.get("distributionConfigurationArn") is not None:
        out["distribution_configuration_arn"] = data["distributionConfigurationArn"]
    else:
        raise DeserializationError(
            "DistributeImageRequest.distribution_configuration_arn required"
        )
    if data.get("executionRole") is not None:
        out["execution_role"] = data["executionRole"]
    else:
        raise DeserializationError("DistributeImageRequest.execution_role required")
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("DistributeImageRequest.client_token required")
    if data.get("loggingConfiguration") is not None:
        import capo_imagebuilder.types.image_logging_configuration

        out["logging_configuration"] = (
            capo_imagebuilder.types.image_logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    return out
