"""Generated from Smithy shape ``com.amazonaws.signin#GrantType``."""

from typing import TypeAlias

"""OAuth 2.0 grant type parameter For auth code redemption: Must be "authorization_code" For token refresh: Must be "refresh_token" Based on client_id & grant_type, authn/authz is skipped for CLI endpoints."""
GrantType: TypeAlias = str
