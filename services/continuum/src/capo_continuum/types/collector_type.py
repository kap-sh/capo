"""Generated from Smithy shape ``com.amazonaws.continuum#CollectorType``."""

from typing import Literal, TypeAlias, cast

"""The source collected by a Collector. Additional kinds can be added as they become supported; recorder provisioning remains a service detail."""
CollectorType: TypeAlias = Literal["AWS_COLLECTOR",]


# --- restJson1 ser/de ---
def serialize_json(value: CollectorType) -> str:
    return value


def deserialize_json(data: str) -> CollectorType:
    return cast(CollectorType, data)
