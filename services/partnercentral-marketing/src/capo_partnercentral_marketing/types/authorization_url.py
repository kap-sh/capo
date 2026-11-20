"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AuthorizationUrl``."""

from typing import TypeAlias

"""Single-use URL the partner visits to grant authorization on the social platform. Returned only by CreateSocialConnectionAuthorizationUrl, never by a read operation. Treated as sensitive: it is a bearer capability, so anyone holding it before it is used can link an account. Never log it."""
AuthorizationUrl: TypeAlias = str
