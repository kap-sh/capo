"""Generated from Smithy shape ``com.amazonaws.continuum#OAuthCodeChallenge``."""

from typing import TypeAlias

"""A PKCE code challenge (RFC 7636): the base64url encoding, without padding, of the SHA-256 digest of the code verifier the service keeps."""
OAuthCodeChallenge: TypeAlias = str
