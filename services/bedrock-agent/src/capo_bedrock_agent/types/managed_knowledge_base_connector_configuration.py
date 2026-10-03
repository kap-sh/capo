"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ManagedKnowledgeBaseConnectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.deletion_protection_configuration
    import capo_bedrock_agent.types.media_extraction_configuration
    import capo_bedrock_agent.types.sync_schedule


class ManagedKnowledgeBaseConnectorConfiguration(TypedDict, closed=True):
    deletion_protection_configuration: NotRequired[
        "capo_bedrock_agent.types.deletion_protection_configuration.DeletionProtectionConfiguration"
    ]
    """<p>A safeguard against accidental bulk deletion of indexed content.</p>"""
    media_extraction_configuration: NotRequired[
        "capo_bedrock_agent.types.media_extraction_configuration.MediaExtractionConfiguration"
    ]
    """<p>Configuration for extracting media (images, audio, video) from data source files.</p>"""
    connector_parameters: NotRequired["object"]
    """<p>Connector-specific parameters. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-connect-ds.html">Connect a data source</a>.</p>"""
    sync_schedule: NotRequired["capo_bedrock_agent.types.sync_schedule.SyncSchedule"]
    """<p>The recurring schedule on which the connector automatically syncs this data source. If not specified, the data source is not synced automatically and you start each sync yourself. Not supported for the Custom connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedKnowledgeBaseConnectorConfiguration) -> dict:
    out: dict = {}
    if "deletion_protection_configuration" in value:
        import capo_bedrock_agent.types.deletion_protection_configuration

        out["deletionProtectionConfiguration"] = (
            capo_bedrock_agent.types.deletion_protection_configuration.serialize_json(
                value["deletion_protection_configuration"]
            )
        )
    if "media_extraction_configuration" in value:
        import capo_bedrock_agent.types.media_extraction_configuration

        out["mediaExtractionConfiguration"] = (
            capo_bedrock_agent.types.media_extraction_configuration.serialize_json(
                value["media_extraction_configuration"]
            )
        )
    if "connector_parameters" in value:
        out["connectorParameters"] = value["connector_parameters"]
    if "sync_schedule" in value:
        import capo_bedrock_agent.types.sync_schedule

        out["syncSchedule"] = capo_bedrock_agent.types.sync_schedule.serialize_json(
            value["sync_schedule"]
        )
    return out


def deserialize_json(data: dict) -> ManagedKnowledgeBaseConnectorConfiguration:
    out: ManagedKnowledgeBaseConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("deletionProtectionConfiguration") is not None:
        import capo_bedrock_agent.types.deletion_protection_configuration

        out["deletion_protection_configuration"] = (
            capo_bedrock_agent.types.deletion_protection_configuration.deserialize_json(
                data["deletionProtectionConfiguration"]
            )
        )
    if data.get("mediaExtractionConfiguration") is not None:
        import capo_bedrock_agent.types.media_extraction_configuration

        out["media_extraction_configuration"] = (
            capo_bedrock_agent.types.media_extraction_configuration.deserialize_json(
                data["mediaExtractionConfiguration"]
            )
        )
    if data.get("connectorParameters") is not None:
        out["connector_parameters"] = data["connectorParameters"]
    if data.get("syncSchedule") is not None:
        import capo_bedrock_agent.types.sync_schedule

        out["sync_schedule"] = capo_bedrock_agent.types.sync_schedule.deserialize_json(
            data["syncSchedule"]
        )
    return out
