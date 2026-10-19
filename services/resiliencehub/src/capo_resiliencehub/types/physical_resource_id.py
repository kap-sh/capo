"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PhysicalResourceId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.aws_region
    import capo_resiliencehub.types.customer_id
    import capo_resiliencehub.types.physical_identifier_type
    import capo_resiliencehub.types.string255


class PhysicalResourceId(TypedDict, closed=True):
    identifier: "capo_resiliencehub.types.string255.String255"
    """<p>Identifier of the physical resource.</p>"""
    type: "capo_resiliencehub.types.physical_identifier_type.PhysicalIdentifierType"
    """<p>Specifies the type of physical resource identifier.</p> <dl> <dt>Arn</dt> <dd> <p>The resource identifier is an Amazon Resource Name (ARN) and it can identify the following list of resources:</p> <ul> <li> <p> <code>AWS::ECS::Service</code> </p> </li> <li> <p> <code>AWS::EFS::FileSystem</code> </p> </li> <li> <p> <code>AWS::ElasticLoadBalancingV2::LoadBalancer</code> </p> </li> <li> <p> <code>AWS::Lambda::Function</code> </p> </li> <li> <p> <code>AWS::SNS::Topic</code> </p> </li> </ul> </dd> <dt>Native</dt> <dd> <p>The resource identifier is an Resilience Hub-native identifier and it can identify the following list of resources:</p> <ul> <li> <p> <code>AWS::ApiGateway::RestApi</code> </p> </li> <li> <p> <code>AWS::ApiGatewayV2::Api</code> </p> </li> <li> <p> <code>AWS::AutoScaling::AutoScalingGroup</code> </p> </li> <li> <p> <code>AWS::DocDB::DBCluster</code> </p> </li> <li> <p> <code>AWS::DocDB::DBGlobalCluster</code> </p> </li> <li> <p> <code>AWS::DocDB::DBInstance</code> </p> </li> <li> <p> <code>AWS::DynamoDB::GlobalTable</code> </p> </li> <li> <p> <code>AWS::DynamoDB::Table</code> </p> </li> <li> <p> <code>AWS::EC2::EC2Fleet</code> </p> </li> <li> <p> <code>AWS::EC2::Instance</code> </p> </li> <li> <p> <code>AWS::EC2::NatGateway</code> </p> </li> <li> <p> <code>AWS::EC2::Volume</code> </p> </li> <li> <p> <code>AWS::ElasticLoadBalancing::LoadBalancer</code> </p> </li> <li> <p> <code>AWS::RDS::DBCluster</code> </p> </li> <li> <p> <code>AWS::RDS::DBInstance</code> </p> </li> <li> <p> <code>AWS::RDS::GlobalCluster</code> </p> </li> <li> <p> <code>AWS::Route53::RecordSet</code> </p> </li> <li> <p> <code>AWS::S3::Bucket</code> </p> </li> <li> <p> <code>AWS::SQS::Queue</code> </p> </li> </ul> </dd> </dl>"""
    aws_region: NotRequired["capo_resiliencehub.types.aws_region.AwsRegion"]
    """<p>The Amazon Web Services Region that the physical resource is located in.</p>"""
    aws_account_id: NotRequired["capo_resiliencehub.types.customer_id.CustomerId"]
    """<p>The Amazon Web Services account that owns the physical resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalResourceId) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    import capo_resiliencehub.types.physical_identifier_type

    out["type"] = capo_resiliencehub.types.physical_identifier_type.serialize_json(
        value["type"]
    )
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    return out


def deserialize_json(data: dict) -> PhysicalResourceId:
    out: PhysicalResourceId = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("type") is not None:
        import capo_resiliencehub.types.physical_identifier_type

        out["type"] = (
            capo_resiliencehub.types.physical_identifier_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_resiliencehub.types.physical_identifier_type.PhysicalIdentifierType",
            "",
        )
    if data.get("awsRegion") is not None:
        out["aws_region"] = data["awsRegion"]
    if data.get("awsAccountId") is not None:
        out["aws_account_id"] = data["awsAccountId"]
    return out
