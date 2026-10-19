"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CachePointBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.cache_point_type


class CachePointBlock(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.cache_point_type.CachePointType"
    """<p>Indicates that the CachePointBlock is of the default type</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CachePointBlock) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.cache_point_type

    out["type"] = capo_bedrock_agent.types.cache_point_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> CachePointBlock:
    out: CachePointBlock = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.cache_point_type

        out["type"] = capo_bedrock_agent.types.cache_point_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.cache_point_type.CachePointType", ""
        )
    return out
