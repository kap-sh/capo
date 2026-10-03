"""Generated from Smithy shape ``com.amazonaws.opensearch#VolumeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of EBS volume that a domain uses. For more information, see <a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/opensearch-createupdatedomains.html#opensearch-createdomain-configure-ebs">Configuring EBS-based storage</a>.</p>"""
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
