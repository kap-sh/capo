"""Generated from Smithy shape ``com.amazonaws.endusermessaging#NotifyCodeConfigurationId``."""

from typing import TypeAlias

"""Bare system-generated NotifyCodeConfiguration identifier (output-only). Always a bare id, never an ARN — the ARN is carried separately by `NotifyCodeConfiguration$notifyCodeConfigurationArn`. Identifiers are opaque tokens; clients must not assume a specific length or format."""
NotifyCodeConfigurationId: TypeAlias = str
