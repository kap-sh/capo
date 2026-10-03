"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#PutResourcePolicyRequest``."""

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the account to create or update a resource policy for.</p>"""
    policy: "str"
    r"""<p>The policy to create or update. For example, the following policy grants a user authorization to restore a snapshot.</p> <p> <code>"{\"Version\": \"2012-10-17\", \"Statement\" : [{ \"Sid\": \"AllowUserRestoreFromSnapshot\", \"Principal\":{\"AWS\": [\"739247239426\"]}, \"Action\": [\"redshift-serverless:RestoreFromSnapshot\"] , \"Effect\": \"Allow\" }]}"</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.policy required")
    return out
