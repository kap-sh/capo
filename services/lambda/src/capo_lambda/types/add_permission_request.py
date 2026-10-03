"""Generated from Smithy shape ``com.amazonaws.lambda#AddPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.action
    import capo_lambda.types.arn
    import capo_lambda.types.event_source_token
    import capo_lambda.types.function_url_auth_type
    import capo_lambda.types.invoked_via_function_url
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.numeric_latest_published_or_alias_qualifier
    import capo_lambda.types.principal
    import capo_lambda.types.principal_org_id
    import capo_lambda.types.source_owner
    import capo_lambda.types.statement_id
    import capo_lambda.types.string


class AddPermissionRequest(TypedDict, closed=True):
    function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName"
    """<p>The name or ARN of the Lambda function, version, or alias.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    statement_id: "capo_lambda.types.statement_id.StatementId"
    """<p>A statement identifier that differentiates the statement from others in the same policy.</p>"""
    action: "capo_lambda.types.action.Action"
    """<p>The action that the principal can use on the function. For example, <code>lambda:InvokeFunction</code> or <code>lambda:GetFunction</code>.</p>"""
    principal: "capo_lambda.types.principal.Principal"
    """<p>The Amazon Web Services service, Amazon Web Services account, IAM user, or IAM role that invokes the function. If you specify a service, use <code>SourceArn</code> or <code>SourceAccount</code> to limit who can invoke the function through that service.</p>"""
    source_arn: NotRequired["capo_lambda.types.arn.Arn"]
    """<p>For Amazon Web Services services, the ARN of the Amazon Web Services resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.</p> <p>Note that Lambda configures the comparison using the <code>StringLike</code> operator.</p>"""
    function_url_auth_type: NotRequired[
        "capo_lambda.types.function_url_auth_type.FunctionUrlAuthType"
    ]
    """<p>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html">Control access to Lambda function URLs</a>.</p>"""
    invoked_via_function_url: NotRequired[
        "capo_lambda.types.invoked_via_function_url.InvokedViaFunctionUrl"
    ]
    """<p>Indicates whether the permission applies when the function is invoked through a function URL. </p>"""
    source_account: NotRequired["capo_lambda.types.source_owner.SourceOwner"]
    """<p>For Amazon Web Services service, the ID of the Amazon Web Services account that owns the resource. Use this together with <code>SourceArn</code> to ensure that the specified account owns the resource. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.</p>"""
    event_source_token: NotRequired[
        "capo_lambda.types.event_source_token.EventSourceToken"
    ]
    """<p>For Alexa Smart Home functions, a token that the invoker must supply.</p>"""
    qualifier: NotRequired[
        "capo_lambda.types.numeric_latest_published_or_alias_qualifier.NumericLatestPublishedOrAliasQualifier"
    ]
    """<p>Specify a version or alias to add permissions to a published version of the function.</p>"""
    revision_id: NotRequired["capo_lambda.types.string.String"]
    """<p>Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.</p>"""
    principal_org_id: NotRequired["capo_lambda.types.principal_org_id.PrincipalOrgID"]
    """<p>The identifier for your organization in Organizations. Use this to grant permissions to all the Amazon Web Services accounts under this organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddPermissionRequest) -> dict:
    out: dict = {}
    out["StatementId"] = value["statement_id"]
    out["Action"] = value["action"]
    out["Principal"] = value["principal"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "function_url_auth_type" in value:
        import capo_lambda.types.function_url_auth_type

        out["FunctionUrlAuthType"] = (
            capo_lambda.types.function_url_auth_type.serialize_json(
                value["function_url_auth_type"]
            )
        )
    if "invoked_via_function_url" in value:
        out["InvokedViaFunctionUrl"] = value["invoked_via_function_url"]
    if "source_account" in value:
        out["SourceAccount"] = value["source_account"]
    if "event_source_token" in value:
        out["EventSourceToken"] = value["event_source_token"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "principal_org_id" in value:
        out["PrincipalOrgID"] = value["principal_org_id"]
    return out


def deserialize_json(data: dict) -> AddPermissionRequest:
    out: AddPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("StatementId") is not None:
        out["statement_id"] = data["StatementId"]
    else:
        raise DeserializationError("AddPermissionRequest.statement_id required")
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        raise DeserializationError("AddPermissionRequest.action required")
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    else:
        raise DeserializationError("AddPermissionRequest.principal required")
    if data.get("SourceArn") is not None:
        out["source_arn"] = data["SourceArn"]
    if data.get("FunctionUrlAuthType") is not None:
        import capo_lambda.types.function_url_auth_type

        out["function_url_auth_type"] = (
            capo_lambda.types.function_url_auth_type.deserialize_json(
                data["FunctionUrlAuthType"]
            )
        )
    if data.get("InvokedViaFunctionUrl") is not None:
        out["invoked_via_function_url"] = data["InvokedViaFunctionUrl"]
    if data.get("SourceAccount") is not None:
        out["source_account"] = data["SourceAccount"]
    if data.get("EventSourceToken") is not None:
        out["event_source_token"] = data["EventSourceToken"]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    if data.get("PrincipalOrgID") is not None:
        out["principal_org_id"] = data["PrincipalOrgID"]
    return out
