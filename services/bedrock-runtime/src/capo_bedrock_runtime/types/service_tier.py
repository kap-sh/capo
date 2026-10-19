"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ServiceTier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.service_tier_type


class ServiceTier(TypedDict, closed=True):
    type: "capo_bedrock_runtime.types.service_tier_type.ServiceTierType"
    """<p>Specifies the processing tier type used for serving the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceTier) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.service_tier_type

    out["type"] = capo_bedrock_runtime.types.service_tier_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> ServiceTier:
    out: ServiceTier = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.service_tier_type

        out["type"] = capo_bedrock_runtime.types.service_tier_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_runtime.types.service_tier_type.ServiceTierType", ""
        )
    return out
