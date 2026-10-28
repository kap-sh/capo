"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ModuleParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError, SerializationError
from capo_rtbfabric.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_rtbfabric.types.no_bid_module_parameters
    import capo_rtbfabric.types.open_rtb_attribute_module_parameters
    import capo_rtbfabric.types.rate_limiter_module_parameters


class ModuleParametersNoBidMember(TypedDict, closed=True):
    noBid: "capo_rtbfabric.types.no_bid_module_parameters.NoBidModuleParameters"


class ModuleParametersOpenRtbAttributeMember(TypedDict, closed=True):
    openRtbAttribute: "capo_rtbfabric.types.open_rtb_attribute_module_parameters.OpenRtbAttributeModuleParameters"


class ModuleParametersRateLimiterMember(TypedDict, closed=True):
    rateLimiter: "capo_rtbfabric.types.rate_limiter_module_parameters.RateLimiterModuleParameters"


ModuleParameters: TypeAlias = (
    ModuleParametersNoBidMember
    | ModuleParametersOpenRtbAttributeMember
    | ModuleParametersRateLimiterMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ModuleParameters) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ModuleParameters: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "noBid" in value:
        import capo_rtbfabric.types.no_bid_module_parameters

        return {
            "noBid": capo_rtbfabric.types.no_bid_module_parameters.serialize_json(
                value["noBid"]
            )
        }
    elif "openRtbAttribute" in value:
        import capo_rtbfabric.types.open_rtb_attribute_module_parameters

        return {
            "openRtbAttribute": capo_rtbfabric.types.open_rtb_attribute_module_parameters.serialize_json(
                value["openRtbAttribute"]
            )
        }
    elif "rateLimiter" in value:
        import capo_rtbfabric.types.rate_limiter_module_parameters

        return {
            "rateLimiter": capo_rtbfabric.types.rate_limiter_module_parameters.serialize_json(
                value["rateLimiter"]
            )
        }
    else:
        raise SerializationError("ModuleParameters: no variant present")


def deserialize_json(data: dict) -> ModuleParameters:
    if data.get("noBid") is not None:
        import capo_rtbfabric.types.no_bid_module_parameters

        return {
            "noBid": capo_rtbfabric.types.no_bid_module_parameters.deserialize_json(
                data["noBid"]
            )
        }
    elif data.get("openRtbAttribute") is not None:
        import capo_rtbfabric.types.open_rtb_attribute_module_parameters

        return {
            "openRtbAttribute": capo_rtbfabric.types.open_rtb_attribute_module_parameters.deserialize_json(
                data["openRtbAttribute"]
            )
        }
    elif data.get("rateLimiter") is not None:
        import capo_rtbfabric.types.rate_limiter_module_parameters

        return {
            "rateLimiter": capo_rtbfabric.types.rate_limiter_module_parameters.deserialize_json(
                data["rateLimiter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ModuleParameters: no recognized variant key")
