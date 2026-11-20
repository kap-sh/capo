"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SocialConnectionId``."""

from typing import TypeAlias

"""Service-generated identifier of a social connection. Stable for the life of the connection: it survives a revoke and a re-authorization of the same account, and is never reused once the connection is deleted. `sc-` and 13 lowercase letters or digits (DG-092)."""
SocialConnectionId: TypeAlias = str
