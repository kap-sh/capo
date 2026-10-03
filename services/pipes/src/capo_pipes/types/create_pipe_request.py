"""Generated from Smithy shape ``com.amazonaws.pipes#CreatePipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.arn
    import capo_pipes.types.arn_or_url
    import capo_pipes.types.kms_key_identifier
    import capo_pipes.types.optional_arn
    import capo_pipes.types.pipe_description
    import capo_pipes.types.pipe_enrichment_parameters
    import capo_pipes.types.pipe_log_configuration_parameters
    import capo_pipes.types.pipe_name
    import capo_pipes.types.pipe_source_parameters
    import capo_pipes.types.pipe_target_parameters
    import capo_pipes.types.requested_pipe_state
    import capo_pipes.types.role_arn
    import capo_pipes.types.tag_map


class CreatePipeRequest(TypedDict, closed=True):
    name: "capo_pipes.types.pipe_name.PipeName"
    """<p>The name of the pipe.</p>"""
    description: NotRequired["capo_pipes.types.pipe_description.PipeDescription"]
    """<p>A description of the pipe.</p>"""
    desired_state: NotRequired[
        "capo_pipes.types.requested_pipe_state.RequestedPipeState"
    ]
    """<p>The state the pipe should be in.</p>"""
    source: "capo_pipes.types.arn_or_url.ArnOrUrl"
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
    target: "capo_pipes.types.arn.Arn"
    """<p>The ARN of the target resource.</p>"""
    target_parameters: NotRequired[
        "capo_pipes.types.pipe_target_parameters.PipeTargetParameters"
    ]
    """<p>The parameters required to set up a target for your pipe.</p> <p>For more information about pipe target parameters, including how to use dynamic path parameters, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html">Target parameters</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    role_arn: "capo_pipes.types.role_arn.RoleArn"
    """<p>The ARN of the role that allows the pipe to send data to the target.</p>"""
    tags: NotRequired["capo_pipes.types.tag_map.TagMap"]
    """<p>The list of key-value pairs to associate with the pipe.</p>"""
    log_configuration: NotRequired[
        "capo_pipes.types.pipe_log_configuration_parameters.PipeLogConfigurationParameters"
    ]
    """<p>The logging configuration settings for the pipe.</p>"""
    kms_key_identifier: NotRequired[
        "capo_pipes.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use, if you choose to use a customer managed key to encrypt pipe data. The identifier can be the key Amazon Resource Name (ARN), KeyId, key alias, or key alias ARN.</p> <p>If you do not specify a customer managed key identifier, EventBridge uses an Amazon Web Services owned key to encrypt pipe data.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html">Managing keys</a> in the <i>Key Management Service Developer Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePipeRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "desired_state" in value:
        out["DesiredState"] = value["desired_state"]
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
    out["Target"] = value["target"]
    if "target_parameters" in value:
        import capo_pipes.types.pipe_target_parameters

        out["TargetParameters"] = (
            capo_pipes.types.pipe_target_parameters.serialize_json(
                value["target_parameters"]
            )
        )
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_pipes.types.tag_map

        out["Tags"] = capo_pipes.types.tag_map.serialize_json(value["tags"])
    if "log_configuration" in value:
        import capo_pipes.types.pipe_log_configuration_parameters

        out["LogConfiguration"] = (
            capo_pipes.types.pipe_log_configuration_parameters.serialize_json(
                value["log_configuration"]
            )
        )
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> CreatePipeRequest:
    out: CreatePipeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DesiredState") is not None:
        out["desired_state"] = data["DesiredState"]
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("CreatePipeRequest.source required")
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
    else:
        raise DeserializationError("CreatePipeRequest.target required")
    if data.get("TargetParameters") is not None:
        import capo_pipes.types.pipe_target_parameters

        out["target_parameters"] = (
            capo_pipes.types.pipe_target_parameters.deserialize_json(
                data["TargetParameters"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreatePipeRequest.role_arn required")
    if data.get("Tags") is not None:
        import capo_pipes.types.tag_map

        out["tags"] = capo_pipes.types.tag_map.deserialize_json(data["Tags"])
    if data.get("LogConfiguration") is not None:
        import capo_pipes.types.pipe_log_configuration_parameters

        out["log_configuration"] = (
            capo_pipes.types.pipe_log_configuration_parameters.deserialize_json(
                data["LogConfiguration"]
            )
        )
    if data.get("KmsKeyIdentifier") is not None:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out
