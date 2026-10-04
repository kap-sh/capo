"""Generated from Smithy shape ``com.amazonaws.endusermessaging#NotifyCodeConfigurationIdOrArn``."""

from typing import TypeAlias

"""System-generated NotifyCodeConfiguration identifier or full ARN. Accepts either a bare id or a full ARN (e.g., "arn:aws:end-user-messaging:us-east-1:123456789012:notify-code-configuration/<id>"). Identifiers are opaque tokens; clients must not assume a specific length or format. SDKs handle percent-encoding of ARN characters in path parameters transparently."""
NotifyCodeConfigurationIdOrArn: TypeAlias = str
