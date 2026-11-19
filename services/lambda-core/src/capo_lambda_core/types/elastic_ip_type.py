"""Generated from Smithy shape ``com.amazonaws.lambdacore#ElasticIpType``."""

from typing import Literal, TypeAlias, cast

"""<p>The Elastic IP type for a network connector's ENIs.</p>"""
ElasticIpType: TypeAlias = Literal[
    "None",
    "ServiceManaged",
]


# --- restJson1 ser/de ---
def serialize_json(value: ElasticIpType) -> str:
    return value


def deserialize_json(data: str) -> ElasticIpType:
    return cast(ElasticIpType, data)
