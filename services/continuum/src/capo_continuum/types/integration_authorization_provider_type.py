"""Generated from Smithy shape ``com.amazonaws.continuum#IntegrationAuthorizationProviderType``."""

from typing import Literal, TypeAlias, cast

"""A provider whose OAuth authorization can be started with StartIntegrationAuthorization."""
IntegrationAuthorizationProviderType: TypeAlias = Literal["GITHUB",]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationAuthorizationProviderType) -> str:
    return value


def deserialize_json(data: str) -> IntegrationAuthorizationProviderType:
    return cast(IntegrationAuthorizationProviderType, data)
