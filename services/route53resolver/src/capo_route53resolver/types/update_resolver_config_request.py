"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateResolverConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.autodefined_reverse_flag
    import capo_route53resolver.types.resource_id


class UpdateResolverConfigRequest(TypedDict, closed=True):
    resource_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Amazon Virtual Private Cloud VPC or a Route 53 Profile that you're configuring Resolver for.</p>"""
    autodefined_reverse_flag: (
        "capo_route53resolver.types.autodefined_reverse_flag.AutodefinedReverseFlag"
    )
    """<p>Indicates whether or not the Resolver will create autodefined rules for reverse DNS lookups. This is enabled by default. Disabling this option will also affect EC2-Classic instances using ClassicLink. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-classiclink.html">ClassicLink</a> in the <i>Amazon EC2 guide</i>.</p> <important> <p>We are retiring EC2-Classic on August 15, 2022. We recommend that you migrate from EC2-Classic to a VPC. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html">Migrate from EC2-Classic to a VPC</a> in the <i>Amazon EC2 guide</i> and the blog <a href="http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/">EC2-Classic Networking is Retiring – Here’s How to Prepare</a>.</p> </important> <note> <p>It can take some time for the status change to be completed.</p> </note> <p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResolverConfigRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_route53resolver.types.autodefined_reverse_flag

    out["AutodefinedReverseFlag"] = (
        capo_route53resolver.types.autodefined_reverse_flag.serialize_aws_json_1_1(
            value["autodefined_reverse_flag"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResolverConfigRequest:
    out: UpdateResolverConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("UpdateResolverConfigRequest.resource_id required")
    if data.get("AutodefinedReverseFlag") is not None:
        import capo_route53resolver.types.autodefined_reverse_flag

        out["autodefined_reverse_flag"] = (
            capo_route53resolver.types.autodefined_reverse_flag.deserialize_aws_json_1_1(
                data["AutodefinedReverseFlag"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateResolverConfigRequest.autodefined_reverse_flag required"
        )
    return out
