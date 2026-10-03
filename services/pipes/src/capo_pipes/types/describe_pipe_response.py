"""Generated from Smithy shape ``com.amazonaws.pipes#DescribePipeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.arn
    import capo_pipes.types.arn_or_url
    import capo_pipes.types.kms_key_identifier
    import capo_pipes.types.optional_arn
    import capo_pipes.types.pipe_arn
    import capo_pipes.types.pipe_description
    import capo_pipes.types.pipe_enrichment_parameters
    import capo_pipes.types.pipe_log_configuration
    import capo_pipes.types.pipe_name
    import capo_pipes.types.pipe_source_parameters
    import capo_pipes.types.pipe_state
    import capo_pipes.types.pipe_state_reason
    import capo_pipes.types.pipe_target_parameters
    import capo_pipes.types.requested_pipe_state_describe_response
    import capo_pipes.types.role_arn
    import capo_pipes.types.tag_map
    import capo_pipes.types.timestamp


class DescribePipeResponse(TypedDict, closed=True):
    arn: NotRequired["capo_pipes.types.pipe_arn.PipeArn"]
    """<p>The ARN of the pipe.</p>"""
    name: NotRequired["capo_pipes.types.pipe_name.PipeName"]
    """<p>The name of the pipe.</p>"""
    description: NotRequired["capo_pipes.types.pipe_description.PipeDescription"]
    """<p>A description of the pipe.</p>"""
    desired_state: NotRequired[
        "capo_pipes.types.requested_pipe_state_describe_response.RequestedPipeStateDescribeResponse"
    ]
    """<p>The state the pipe should be in.</p>"""
    current_state: NotRequired["capo_pipes.types.pipe_state.PipeState"]
    """<p>The state the pipe is in.</p>"""
    state_reason: NotRequired["capo_pipes.types.pipe_state_reason.PipeStateReason"]
    """<p>The reason the pipe is in its current state.</p>"""
    source: NotRequired["capo_pipes.types.arn_or_url.ArnOrUrl"]
    """<p>The ARN of the source resource.</p>"""
    source_parameters: NotRequired[
        "capo_pipes.types.pipe_source_parameters.PipeSourceParameters"
    ]
    """<p>The parameters required to set up a source for your pipe.</p>"""
    enrichment: NotRequired["capo_pipes.types.optional_arn.OptionalArn"]
    """<p>The ARN of the enrichment resource.</p>"""
    enrichment_parameters: NotRequired[
        "capo_pipes.types.pipe_enrichment_parameters.PipeEnrichmentParameters"
    ]
    """<p>The parameters required to set up enrichment on your pipe.</p>"""
    target: NotRequired["capo_pipes.types.arn.Arn"]
    """<p>The ARN of the target resource.</p>"""
    target_parameters: NotRequired[
        "capo_pipes.types.pipe_target_parameters.PipeTargetParameters"
    ]
    """<p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    role_arn: NotRequired["capo_pipes.types.role_arn.RoleArn"]
    """<p>The ARN of the role that allows the pipe to send data to the target.</p>"""
    tags: NotRequired["capo_pipes.types.tag_map.TagMap"]
    """<p>The list of key-value pairs to associate with the pipe.</p>"""
    creation_time: NotRequired["capo_pipes.types.timestamp.Timestamp"]
    """<p>The time the pipe was created.</p>"""
    last_modified_time: NotRequired["capo_pipes.types.timestamp.Timestamp"]
    """<p>When the pipe was last updated, in <a href="https://www.w3.org/TR/NOTE-datetime">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    log_configuration: NotRequired[
        "capo_pipes.types.pipe_log_configuration.PipeLogConfiguration"
    ]
    """<p>The logging configuration settings for the pipe.</p>"""
    kms_key_identifier: NotRequired[
        "capo_pipes.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt pipe data, if one has been specified.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-encryption.html">Data encryption in EventBridge</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePipeResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "desired_state" in value:
        out["DesiredState"] = value["desired_state"]
    if "current_state" in value:
        out["CurrentState"] = value["current_state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "source" in value:
        out["Source"] = value["source"]
    if "source_parameters" in value:
        import capo_pipes.types.pipe_source_parameters

        out["SourceParameters"] = (
            capo_pipes.types.pipe_source_parameters.serialize_json(
                value["source_parameters"]
            )
        )
    if "enrichment" in value:
        out["Enrichment"] = value["enrichment"]
    if "enrichment_parameters" in value:
        import capo_pipes.types.pipe_enrichment_parameters

        out["EnrichmentParameters"] = (
            capo_pipes.types.pipe_enrichment_parameters.serialize_json(
                value["enrichment_parameters"]
            )
        )
    if "target" in value:
        out["Target"] = value["target"]
    if "target_parameters" in value:
        import capo_pipes.types.pipe_target_parameters

        out["TargetParameters"] = (
            capo_pipes.types.pipe_target_parameters.serialize_json(
                value["target_parameters"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_pipes.types.tag_map

        out["Tags"] = capo_pipes.types.tag_map.serialize_json(value["tags"])
    if "creation_time" in value:
        import capo_pipes.types.timestamp

        out["CreationTime"] = capo_pipes.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_pipes.types.timestamp

        out["LastModifiedTime"] = capo_pipes.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "log_configuration" in value:
        import capo_pipes.types.pipe_log_configuration

        out["LogConfiguration"] = (
            capo_pipes.types.pipe_log_configuration.serialize_json(
                value["log_configuration"]
            )
        )
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> DescribePipeResponse:
    out: DescribePipeResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DesiredState") is not None:
        out["desired_state"] = data["DesiredState"]
    if data.get("CurrentState") is not None:
        out["current_state"] = data["CurrentState"]
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    if data.get("SourceParameters") is not None:
        import capo_pipes.types.pipe_source_parameters

        out["source_parameters"] = (
            capo_pipes.types.pipe_source_parameters.deserialize_json(
                data["SourceParameters"]
            )
        )
    if data.get("Enrichment") is not None:
        out["enrichment"] = data["Enrichment"]
    if data.get("EnrichmentParameters") is not None:
        import capo_pipes.types.pipe_enrichment_parameters

        out["enrichment_parameters"] = (
            capo_pipes.types.pipe_enrichment_parameters.deserialize_json(
                data["EnrichmentParameters"]
            )
        )
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    if data.get("TargetParameters") is not None:
        import capo_pipes.types.pipe_target_parameters

        out["target_parameters"] = (
            capo_pipes.types.pipe_target_parameters.deserialize_json(
                data["TargetParameters"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("Tags") is not None:
        import capo_pipes.types.tag_map

        out["tags"] = capo_pipes.types.tag_map.deserialize_json(data["Tags"])
    if data.get("CreationTime") is not None:
        import capo_pipes.types.timestamp

        out["creation_time"] = capo_pipes.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_pipes.types.timestamp

        out["last_modified_time"] = capo_pipes.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LogConfiguration") is not None:
        import capo_pipes.types.pipe_log_configuration

        out["log_configuration"] = (
            capo_pipes.types.pipe_log_configuration.deserialize_json(
                data["LogConfiguration"]
            )
        )
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out
