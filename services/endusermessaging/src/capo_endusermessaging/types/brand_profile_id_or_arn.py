"""Generated from Smithy shape ``com.amazonaws.endusermessaging#BrandProfileIdOrArn``."""

from typing import TypeAlias

"""System-generated brand profile identifier or full ARN. Accepts either a bare ID (e.g., "bp-abc12345678901234") or a full ARN (e.g., "arn:aws:end-user-messaging:us-east-1:123456789012:brand-profile/bp-abc12345678901234"). SDKs handle percent-encoding of ARN characters in path parameters transparently."""
BrandProfileIdOrArn: TypeAlias = str
