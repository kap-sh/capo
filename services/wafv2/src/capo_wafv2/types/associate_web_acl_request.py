"""Generated from Smithy shape ``com.amazonaws.wafv2#AssociateWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.resource_arn


class AssociateWebACLRequest(TypedDict, closed=True):
    web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL that you want to associate with the resource.</p>"""
    resource_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to associate with the web ACL. </p> <p>The ARN must be in one of the following formats:</p> <ul> <li> <p>For an Application Load Balancer: <code>arn:<i>partition</i>:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/app/<i>load-balancer-name</i>/<i>load-balancer-id</i> </code> </p> </li> <li> <p>For an Amazon API Gateway REST API: <code>arn:<i>partition</i>:apigateway:<i>region</i>::/restapis/<i>api-id</i>/stages/<i>stage-name</i> </code> </p> </li> <li> <p>For an AppSync GraphQL API: <code>arn:<i>partition</i>:appsync:<i>region</i>:<i>account-id</i>:apis/<i>GraphQLApiId</i> </code> </p> </li> <li> <p>For an Amazon Cognito user pool: <code>arn:<i>partition</i>:cognito-idp:<i>region</i>:<i>account-id</i>:userpool/<i>user-pool-id</i> </code> </p> </li> <li> <p>For an App Runner service: <code>arn:<i>partition</i>:apprunner:<i>region</i>:<i>account-id</i>:service/<i>apprunner-service-name</i>/<i>apprunner-service-id</i> </code> </p> </li> <li> <p>For an Amazon Web Services Verified Access instance: <code>arn:<i>partition</i>:ec2:<i>region</i>:<i>account-id</i>:verified-access-instance/<i>instance-id</i> </code> </p> </li> <li> <p>For an Amplify application: <code>arn:<i>partition</i>:amplify:<i>region</i>:<i>account-id</i>:apps/<i>app-id</i> </code> </p> </li> <li> <p>For an Amazon Bedrock AgentCore Gateway: <code>arn:<i>partition</i>:bedrock-agentcore:<i>region</i>:<i>account-id</i>:gateway/<i>gateway-id</i> </code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLArn"] = value["web_acl_arn"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateWebACLRequest:
    out: AssociateWebACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebACLArn") is not None:
        out["web_acl_arn"] = data["WebACLArn"]
    else:
        out["web_acl_arn"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
