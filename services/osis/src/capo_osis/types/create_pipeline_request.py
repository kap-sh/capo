"""Generated from Smithy shape ``com.amazonaws.osis#CreatePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.buffer_options
    import capo_osis.types.encryption_at_rest_options
    import capo_osis.types.log_publishing_options
    import capo_osis.types.pipeline_configuration_body
    import capo_osis.types.pipeline_name
    import capo_osis.types.pipeline_role_arn
    import capo_osis.types.pipeline_units
    import capo_osis.types.tag_list
    import capo_osis.types.vpc_options


class CreatePipelineRequest(TypedDict, closed=True):
    pipeline_name: "capo_osis.types.pipeline_name.PipelineName"
    """<p>The name of the OpenSearch Ingestion pipeline to create. Pipeline names are unique across the pipelines owned by an account within an Amazon Web Services Region.</p>"""
    min_units: "capo_osis.types.pipeline_units.PipelineUnits"
    """<p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    max_units: "capo_osis.types.pipeline_units.PipelineUnits"
    """<p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    pipeline_configuration_body: (
        "capo_osis.types.pipeline_configuration_body.PipelineConfigurationBody"
    )
    r"""<p>The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with <code>\n</code>.</p>"""
    log_publishing_options: NotRequired[
        "capo_osis.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Key-value pairs to configure log publishing.</p>"""
    vpc_options: NotRequired["capo_osis.types.vpc_options.VpcOptions"]
    """<p>Container for the values required to configure VPC access for the pipeline. If you don't specify these values, OpenSearch Ingestion creates the pipeline with a public endpoint.</p>"""
    buffer_options: NotRequired["capo_osis.types.buffer_options.BufferOptions"]
    """<p>Key-value pairs to configure persistent buffering for the pipeline.</p>"""
    encryption_at_rest_options: NotRequired[
        "capo_osis.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    """<p>Key-value pairs to configure encryption for data that is written to a persistent buffer.</p>"""
    tags: NotRequired["capo_osis.types.tag_list.TagList"]
    """<p>List of tags to add to the pipeline upon creation.</p>"""
    pipeline_role_arn: NotRequired["capo_osis.types.pipeline_role_arn.PipelineRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants the pipeline permission to access Amazon Web Services resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipelineRequest) -> dict:
    out: dict = {}
    out["PipelineName"] = value["pipeline_name"]
    out["MinUnits"] = value["min_units"]
    out["MaxUnits"] = value["max_units"]
    out["PipelineConfigurationBody"] = value["pipeline_configuration_body"]
    if "log_publishing_options" in value:
        import capo_osis.types.log_publishing_options

        out["LogPublishingOptions"] = (
            capo_osis.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "vpc_options" in value:
        import capo_osis.types.vpc_options

        out["VpcOptions"] = capo_osis.types.vpc_options.serialize_json(
            value["vpc_options"]
        )
    if "buffer_options" in value:
        import capo_osis.types.buffer_options

        out["BufferOptions"] = capo_osis.types.buffer_options.serialize_json(
            value["buffer_options"]
        )
    if "encryption_at_rest_options" in value:
        import capo_osis.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            capo_osis.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "tags" in value:
        import capo_osis.types.tag_list

        out["Tags"] = capo_osis.types.tag_list.serialize_json(value["tags"])
    if "pipeline_role_arn" in value:
        out["PipelineRoleArn"] = value["pipeline_role_arn"]
    return out


def deserialize_json(data: dict) -> CreatePipelineRequest:
    out: CreatePipelineRequest = {}  # type: ignore[typeddict-item]
    if data.get("PipelineName") is not None:
        out["pipeline_name"] = data["PipelineName"]
    else:
        out["pipeline_name"] = ""
    if data.get("MinUnits") is not None:
        out["min_units"] = data["MinUnits"]
    else:
        out["min_units"] = 0
    if data.get("MaxUnits") is not None:
        out["max_units"] = data["MaxUnits"]
    else:
        out["max_units"] = 0
    if data.get("PipelineConfigurationBody") is not None:
        out["pipeline_configuration_body"] = data["PipelineConfigurationBody"]
    else:
        out["pipeline_configuration_body"] = ""
    if data.get("LogPublishingOptions") is not None:
        import capo_osis.types.log_publishing_options

        out["log_publishing_options"] = (
            capo_osis.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if data.get("VpcOptions") is not None:
        import capo_osis.types.vpc_options

        out["vpc_options"] = capo_osis.types.vpc_options.deserialize_json(
            data["VpcOptions"]
        )
    if data.get("BufferOptions") is not None:
        import capo_osis.types.buffer_options

        out["buffer_options"] = capo_osis.types.buffer_options.deserialize_json(
            data["BufferOptions"]
        )
    if data.get("EncryptionAtRestOptions") is not None:
        import capo_osis.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            capo_osis.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_osis.types.tag_list

        out["tags"] = capo_osis.types.tag_list.deserialize_json(data["Tags"])
    if data.get("PipelineRoleArn") is not None:
        out["pipeline_role_arn"] = data["PipelineRoleArn"]
    return out
