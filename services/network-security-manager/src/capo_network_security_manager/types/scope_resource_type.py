"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ScopeResourceType``."""

from typing import Literal, TypeAlias, cast

ScopeResourceType: TypeAlias = Literal[
    "AWS::ApiGateway::Stage",
    "AWS::CloudFront::Distribution",
    "AWS::EC2::EIP",
    "AWS::ElasticLoadBalancingV2::LoadBalancer::application",
    "AWS::ElasticLoadBalancing::LoadBalancer",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeResourceType) -> str:
    return value


def deserialize_json(data: str) -> ScopeResourceType:
    return cast(ScopeResourceType, data)
