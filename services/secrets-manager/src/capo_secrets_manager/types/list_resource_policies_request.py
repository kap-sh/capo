"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ListResourcePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.max_results_type
    import capo_secrets_manager.types.next_token_type
    import capo_secrets_manager.types.secret_id_type


class ListResourcePoliciesRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    max_results: NotRequired[
        "capo_secrets_manager.types.max_results_type.MaxResultsType"
    ]
    """<p>The number of results to include in the response. If you don't specify this value, the service returns up to 100 results.</p> <p>If there are more results available, in the response, Secrets Manager includes <code>NextToken</code>. To get the next results, call <code>ListResourcePolicies</code> again with the value from <code>NextToken</code>.</p>"""
    next_token: NotRequired["capo_secrets_manager.types.next_token_type.NextTokenType"]
    """<p>A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call <code>ListResourcePolicies</code> again with this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcePoliciesRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcePoliciesRequest:
    out: ListResourcePoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        out["secret_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
