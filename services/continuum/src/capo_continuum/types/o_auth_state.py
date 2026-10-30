"""Generated from Smithy shape ``com.amazonaws.continuum#OAuthState``."""

from typing import TypeAlias

"""An opaque OAuth `state` value. StartIntegrationAuthorization returns one, and CreateIntegration redeems it, together with the authorization code, for the same AWS account. Sensitive so clients and the service never log it."""
OAuthState: TypeAlias = str
