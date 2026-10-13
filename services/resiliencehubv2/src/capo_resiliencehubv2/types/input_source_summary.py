"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#InputSourceSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.eks_source
    import capo_resiliencehubv2.types.input_source_id
    import capo_resiliencehubv2.types.input_source_type
    import capo_resiliencehubv2.types.resource_tag_list
    import capo_resiliencehubv2.types.s3_url


class InputSourceSummary(TypedDict, closed=True):
    input_source_id: "capo_resiliencehubv2.types.input_source_id.InputSourceId"
    """<p>The unique identifier of the input source.</p>"""
    type: NotRequired["capo_resiliencehubv2.types.input_source_type.InputSourceType"]
    """<p>The type of the input source.</p>"""
    resource_tags: NotRequired[
        "capo_resiliencehubv2.types.resource_tag_list.ResourceTagList"
    ]
    """<p>The resource tags used for discovery, if this input source uses tags.</p>"""
    cfn_stack_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    tf_state_file_url: NotRequired["capo_resiliencehubv2.types.s3_url.S3Url"]
    eks: NotRequired["capo_resiliencehubv2.types.eks_source.EksSource"]
    """<p>The Amazon EKS configuration, if this input source uses EKS.</p>"""
    design_file_s3_url: NotRequired["capo_resiliencehubv2.types.s3_url.S3Url"]
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the input source was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSourceSummary) -> dict:
    out: dict = {}
    out["inputSourceId"] = value["input_source_id"]
    if "type" in value:
        import capo_resiliencehubv2.types.input_source_type

        out["type"] = capo_resiliencehubv2.types.input_source_type.serialize_json(
            value["type"]
        )
    if "resource_tags" in value:
        import capo_resiliencehubv2.types.resource_tag_list

        out["resourceTags"] = (
            capo_resiliencehubv2.types.resource_tag_list.serialize_json(
                value["resource_tags"]
            )
        )
    if "cfn_stack_arn" in value:
        out["cfnStackArn"] = value["cfn_stack_arn"]
    if "tf_state_file_url" in value:
        out["tfStateFileUrl"] = value["tf_state_file_url"]
    if "eks" in value:
        import capo_resiliencehubv2.types.eks_source

        out["eks"] = capo_resiliencehubv2.types.eks_source.serialize_json(value["eks"])
    if "design_file_s3_url" in value:
        out["designFileS3Url"] = value["design_file_s3_url"]
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> InputSourceSummary:
    out: InputSourceSummary = {}  # type: ignore[typeddict-item]
    if data.get("inputSourceId") is not None:
        out["input_source_id"] = data["inputSourceId"]
    else:
        raise DeserializationError("InputSourceSummary.input_source_id required")
    if data.get("type") is not None:
        import capo_resiliencehubv2.types.input_source_type

        out["type"] = capo_resiliencehubv2.types.input_source_type.deserialize_json(
            data["type"]
        )
    if data.get("resourceTags") is not None:
        import capo_resiliencehubv2.types.resource_tag_list

        out["resource_tags"] = (
            capo_resiliencehubv2.types.resource_tag_list.deserialize_json(
                data["resourceTags"]
            )
        )
    if data.get("cfnStackArn") is not None:
        out["cfn_stack_arn"] = data["cfnStackArn"]
    if data.get("tfStateFileUrl") is not None:
        out["tf_state_file_url"] = data["tfStateFileUrl"]
    if data.get("eks") is not None:
        import capo_resiliencehubv2.types.eks_source

        out["eks"] = capo_resiliencehubv2.types.eks_source.deserialize_json(data["eks"])
    if data.get("designFileS3Url") is not None:
        out["design_file_s3_url"] = data["designFileS3Url"]
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    return out


def redact_sensitive(value: InputSourceSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "eks" in value:
        import capo_resiliencehubv2.types.eks_source

        out["eks"] = capo_resiliencehubv2.types.eks_source.redact_sensitive(
            value["eks"]
        )
    return out
