"""Generated from Smithy shape ``com.amazonaws.deadline#ServiceManagedEc2InstanceMarketOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.ec2_market_type


class ServiceManagedEc2InstanceMarketOptions(TypedDict, closed=True):
    type: "capo_deadline.types.ec2_market_type.Ec2MarketType"
    """The Amazon EC2 instance type."""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedEc2InstanceMarketOptions) -> dict:
    out: dict = {}
    import capo_deadline.types.ec2_market_type

    out["type"] = capo_deadline.types.ec2_market_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> ServiceManagedEc2InstanceMarketOptions:
    out: ServiceManagedEc2InstanceMarketOptions = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_deadline.types.ec2_market_type

        out["type"] = capo_deadline.types.ec2_market_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast(
            "capo_deadline.types.ec2_market_type.Ec2MarketType", ""
        )
    return out
