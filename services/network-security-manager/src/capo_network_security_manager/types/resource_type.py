"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "AWS::ApiGateway::Stage",
    "AWS::CloudFront::Distribution",
    "AWS::EC2::EIP",
    "AWS::ElasticLoadBalancingV2::LoadBalancer::application",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::WAFv2::WebACL",
    "AWS::Shield::Protection",
    "AWS::ShieldRegional::Protection",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
