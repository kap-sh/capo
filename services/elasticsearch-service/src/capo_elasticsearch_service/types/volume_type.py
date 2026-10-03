"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#VolumeType``."""

from typing import Literal, TypeAlias, cast

"""<p> The type of EBS volume, standard, gp2, gp3 or io1. See <a href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-createupdatedomains.html#es-createdomain-configure-ebs" target="_blank">Configuring EBS-based Storage</a>for more information.</p>"""
VolumeType: TypeAlias = Literal[
    "standard",
    "gp2",
    "io1",
    "gp3",
]


# --- restJson1 ser/de ---
def serialize_json(value: VolumeType) -> str:
    return value


def deserialize_json(data: str) -> VolumeType:
    return cast(VolumeType, data)
