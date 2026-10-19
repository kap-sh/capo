"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateOutpostResolverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.instance_count
    import capo_route53resolver.types.outpost_arn
    import capo_route53resolver.types.outpost_instance_type
    import capo_route53resolver.types.outpost_resolver_name
    import capo_route53resolver.types.tag_list


class CreateOutpostResolverRequest(TypedDict, closed=True):
    creator_request_id: "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    """<p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. </p> <p> <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp.</p>"""
    name: "capo_route53resolver.types.outpost_resolver_name.OutpostResolverName"
    """<p>A friendly name that lets you easily find a configuration in the Resolver dashboard in the Route 53 console.</p>"""
    instance_count: NotRequired[
        "capo_route53resolver.types.instance_count.InstanceCount"
    ]
    """<p>Number of Amazon EC2 instances for the Resolver on Outpost. The default and minimal value is 4.</p>"""
    preferred_instance_type: (
        "capo_route53resolver.types.outpost_instance_type.OutpostInstanceType"
    )
    """<p> The Amazon EC2 instance type. If you specify this, you must also specify a value for the <code>OutpostArn</code>. </p>"""
    outpost_arn: "capo_route53resolver.types.outpost_arn.OutpostArn"
    """<p>The Amazon Resource Name (ARN) of the Outpost. If you specify this, you must also specify a value for the <code>PreferredInstanceType</code>.</p>"""
    tags: NotRequired["capo_route53resolver.types.tag_list.TagList"]
    """<p> A string that helps identify the Route 53 Resolvers on Outpost. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOutpostResolverRequest) -> dict:
    out: dict = {}
    out["CreatorRequestId"] = value["creator_request_id"]
    out["Name"] = value["name"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    out["PreferredInstanceType"] = value["preferred_instance_type"]
    out["OutpostArn"] = value["outpost_arn"]
    if "tags" in value:
        import capo_route53resolver.types.tag_list

        out["Tags"] = capo_route53resolver.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOutpostResolverRequest:
    out: CreateOutpostResolverRequest = {}  # type: ignore[typeddict-item]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    else:
        out["creator_request_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("PreferredInstanceType") is not None:
        out["preferred_instance_type"] = data["PreferredInstanceType"]
    else:
        out["preferred_instance_type"] = ""
    if data.get("OutpostArn") is not None:
        out["outpost_arn"] = data["OutpostArn"]
    else:
        out["outpost_arn"] = ""
    if data.get("Tags") is not None:
        import capo_route53resolver.types.tag_list

        out["tags"] = capo_route53resolver.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
