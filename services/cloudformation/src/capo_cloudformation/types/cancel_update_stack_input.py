"""Generated from Smithy shape ``com.amazonaws.cloudformation#CancelUpdateStackInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.stack_name


class CancelUpdateStackInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name.StackName"]
    """<note> <p>If you don't pass a parameter to <code>StackName</code>, the API returns a response that describes all resources in the account.</p> <p>The IAM policy below can be added to IAM policies when you want to limit resource-level permissions and avoid returning a response when no parameter is sent in the request:</p> <p> <code>{ "Version": "2012-10-17", "Statement": [{ "Effect": "Deny", "Action": "cloudformation:DescribeStacks", "NotResource": "arn:aws:cloudformation:*:*:stack/*/*" }] }</code> </p> </note> <p>The name or the unique stack ID that's associated with the stack.</p>"""
    client_request_token: NotRequired[
        "capo_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for this <code>CancelUpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry <code>CancelUpdateStack</code> requests to ensure that CloudFormation successfully received them.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CancelUpdateStackInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "client_request_token" in value:
        pairs.append(
            (f"{key_prefix}ClientRequestToken", str(value["client_request_token"]))
        )


def deserialize_query(el: Element) -> CancelUpdateStackInput:
    out: CancelUpdateStackInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    return out
