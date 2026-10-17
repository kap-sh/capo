"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "AWS::EC2::Instance",
    "AWS::EC2::VPC",
    "AWS::Lambda::Function",
    "AWS::CloudTrail",
    "AWS::EKS::Cluster",
    "AWS::WAFv2::WebACL",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::Route53Resolver::ResolverEndpoint",
    "AWS::BedrockAgentCore::Runtime",
    "AWS::BedrockAgentCore::Browser",
    "AWS::BedrockAgentCore::CodeInterpreter",
    "AWS::BedrockAgentCore::Gateway",
    "AWS::BedrockAgentCore::Memory",
    "AWS::BedrockAgentCore::WorkloadIdentity",
    "AWS::BedrockAgentCore::PaymentManager",
    "AWS::SecurityHub::Hub",
    "AWS::CloudFront::Distribution",
    "AWS::SecurityHub::HubV2",
    "AWS::CloudWatch::OTelEnrichment",
    "AWS::MSK::Cluster",
    "AWS::S3::Bucket",
    "AWS::Bedrock::KnowledgeBase",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
