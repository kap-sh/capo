"""Generated from Smithy shape ``com.amazonaws.pinpoint#EmailChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string


class EmailChannelResponse(TypedDict, closed=True):
    application_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the email channel applies to.</p>"""
    configuration_set: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The <a href="https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html">Amazon SES configuration set</a> that's applied to messages that are sent through the channel.</p>"""
    creation_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the email channel was enabled.</p>"""
    enabled: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the email channel is enabled for the application.</p>"""
    from_address: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The verified email address that email is sent from when you send email through the channel.</p>"""
    has_credential: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>(Not used) This property is retained only for backward compatibility.</p>"""
    id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>(Deprecated) An identifier for the email channel. This property is retained only for backward compatibility.</p>"""
    identity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the identity, verified with Amazon Simple Email Service (Amazon SES), that's used when you send email through the channel.</p>"""
    is_archived: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the email channel is archived.</p>"""
    last_modified_by: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The user who last modified the email channel.</p>"""
    last_modified_date: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when the email channel was last modified.</p>"""
    messages_per_second: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The maximum number of emails that can be sent through the channel each second.</p>"""
    platform: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The type of messaging or notification platform for the channel. For the email channel, this value is EMAIL.</p>"""
    role_arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The ARN of the AWS Identity and Access Management (IAM) role that Amazon Pinpoint uses to submit email-related event data for the channel.</p>"""
    orchestration_sending_role_arn: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The ARN of an IAM role for Amazon Pinpoint to use to send email from your campaigns or journeys through Amazon SES.</p>"""
    version: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The current version of the email channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailChannelResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "configuration_set" in value:
        out["ConfigurationSet"] = value["configuration_set"]
    if "creation_date" in value:
        out["CreationDate"] = value["creation_date"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    if "has_credential" in value:
        out["HasCredential"] = value["has_credential"]
    if "id" in value:
        out["Id"] = value["id"]
    if "identity" in value:
        out["Identity"] = value["identity"]
    if "is_archived" in value:
        out["IsArchived"] = value["is_archived"]
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "last_modified_date" in value:
        out["LastModifiedDate"] = value["last_modified_date"]
    if "messages_per_second" in value:
        out["MessagesPerSecond"] = value["messages_per_second"]
    if "platform" in value:
        out["Platform"] = value["platform"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "orchestration_sending_role_arn" in value:
        out["OrchestrationSendingRoleArn"] = value["orchestration_sending_role_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> EmailChannelResponse:
    out: EmailChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("ConfigurationSet") is not None:
        out["configuration_set"] = data["ConfigurationSet"]
    if data.get("CreationDate") is not None:
        out["creation_date"] = data["CreationDate"]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("FromAddress") is not None:
        out["from_address"] = data["FromAddress"]
    if data.get("HasCredential") is not None:
        out["has_credential"] = data["HasCredential"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Identity") is not None:
        out["identity"] = data["Identity"]
    if data.get("IsArchived") is not None:
        out["is_archived"] = data["IsArchived"]
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("LastModifiedDate") is not None:
        out["last_modified_date"] = data["LastModifiedDate"]
    if data.get("MessagesPerSecond") is not None:
        out["messages_per_second"] = data["MessagesPerSecond"]
    if data.get("Platform") is not None:
        out["platform"] = data["Platform"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("OrchestrationSendingRoleArn") is not None:
        out["orchestration_sending_role_arn"] = data["OrchestrationSendingRoleArn"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
