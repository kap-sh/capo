"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateVoiceConnectorRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.network_type
    import capo_chime_sdk_voice.types.tag_list
    import capo_chime_sdk_voice.types.voice_connector_aws_region
    import capo_chime_sdk_voice.types.voice_connector_integration_type
    import capo_chime_sdk_voice.types.voice_connector_name


class CreateVoiceConnectorRequest(TypedDict, closed=True):
    name: "capo_chime_sdk_voice.types.voice_connector_name.VoiceConnectorName"
    """<p>The name of the Voice Connector.</p>"""
    aws_region: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector_aws_region.VoiceConnectorAwsRegion"
    ]
    """<p>The AWS Region in which the Amazon Chime SDK Voice Connector is created. Default value: <code>us-east-1</code> .</p>"""
    require_encryption: "capo_chime_sdk_voice.types.boolean.Boolean"
    """<p>Enables or disables encryption for the Voice Connector.</p>"""
    tags: NotRequired["capo_chime_sdk_voice.types.tag_list.TagList"]
    """<p>The tags assigned to the Voice Connector.</p>"""
    integration_type: NotRequired[
        "capo_chime_sdk_voice.types.voice_connector_integration_type.VoiceConnectorIntegrationType"
    ]
    """<p>The connectors for use with Connect Customer.</p> <p>The following options are available:</p> <ul> <li> <p> <code>CONNECT_CALL_TRANSFER_CONNECTOR</code> - Enables enterprises to integrate Connect Customer with other voice systems to directly transfer voice calls and metadata without using the public telephone network. They can use Connect Customer telephony and Interactive Voice Response (IVR) with their existing voice systems to modernize the IVR experience of their existing contact center and their enterprise and branch voice systems. Additionally, enterprises migrating their contact center to Connect Customer can start with Connect telephony and IVR for immediate modernization ahead of agent migration.</p> <note> <p>This integration is a gated feature. Please reach out to your account team to discuss this feature with a Connect Specialist.</p> </note> </li> <li> <p> <code>CONNECT_ANALYTICS_CONNECTOR</code> - Enables enterprises to integrate Connect Customer with other voice systems for real-time and post-call analytics. They can use Connect Customer Contact Lens with their existing voice systems to provides call recordings, conversational analytics (including contact transcript, sensitive data redaction, content categorization, theme detection, sentiment analysis, real-time alerts, and post-contact summary), and agent performance evaluations (including evaluation forms, automated evaluation, supervisor review) with a rich user experience to display, search and filter customer interactions, and programmatic access to data streams and the data lake. Additionally, enterprises migrating their contact center to Connect Customer can start with Contact Lens analytics and performance insights ahead of agent migration.</p> </li> </ul>"""
    network_type: NotRequired["capo_chime_sdk_voice.types.network_type.NetworkType"]
    """<p>The type of network for the Voice Connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVoiceConnectorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "aws_region" in value:
        import capo_chime_sdk_voice.types.voice_connector_aws_region

        out["AwsRegion"] = (
            capo_chime_sdk_voice.types.voice_connector_aws_region.serialize_json(
                value["aws_region"]
            )
        )
    out["RequireEncryption"] = value["require_encryption"]
    if "tags" in value:
        import capo_chime_sdk_voice.types.tag_list

        out["Tags"] = capo_chime_sdk_voice.types.tag_list.serialize_json(value["tags"])
    if "integration_type" in value:
        import capo_chime_sdk_voice.types.voice_connector_integration_type

        out["IntegrationType"] = (
            capo_chime_sdk_voice.types.voice_connector_integration_type.serialize_json(
                value["integration_type"]
            )
        )
    if "network_type" in value:
        import capo_chime_sdk_voice.types.network_type

        out["NetworkType"] = capo_chime_sdk_voice.types.network_type.serialize_json(
            value["network_type"]
        )
    return out


def deserialize_json(data: dict) -> CreateVoiceConnectorRequest:
    out: CreateVoiceConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("AwsRegion") is not None:
        import capo_chime_sdk_voice.types.voice_connector_aws_region

        out["aws_region"] = (
            capo_chime_sdk_voice.types.voice_connector_aws_region.deserialize_json(
                data["AwsRegion"]
            )
        )
    if data.get("RequireEncryption") is not None:
        out["require_encryption"] = data["RequireEncryption"]
    else:
        out["require_encryption"] = False
    if data.get("Tags") is not None:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.deserialize_json(data["Tags"])
    if data.get("IntegrationType") is not None:
        import capo_chime_sdk_voice.types.voice_connector_integration_type

        out["integration_type"] = (
            capo_chime_sdk_voice.types.voice_connector_integration_type.deserialize_json(
                data["IntegrationType"]
            )
        )
    if data.get("NetworkType") is not None:
        import capo_chime_sdk_voice.types.network_type

        out["network_type"] = capo_chime_sdk_voice.types.network_type.deserialize_json(
            data["NetworkType"]
        )
    return out


def redact_sensitive(value: CreateVoiceConnectorRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_chime_sdk_voice.types.tag_list

        out["tags"] = capo_chime_sdk_voice.types.tag_list.redact_sensitive(
            value["tags"]
        )
    return out
