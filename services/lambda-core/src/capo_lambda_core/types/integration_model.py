"""Generated from Smithy shape ``com.amazonaws.lambdacore#IntegrationModel``."""

from typing import Literal, TypeAlias, cast

"""Supported integration model for a runtime."""
IntegrationModel: TypeAlias = Literal["RuntimeAPI",]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationModel) -> str:
    return value


def deserialize_json(data: str) -> IntegrationModel:
    return cast(IntegrationModel, data)
