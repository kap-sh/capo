"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#GetRequestAuthorizationPolicyOutput``."""

from typing_extensions import TypedDict


class GetRequestAuthorizationPolicyOutput(TypedDict, closed=True):
    policy_document: "object"
    """<p>The policy document evaluated for the denied request, returned as a JSON object.</p> <p>For some AWS services and policy types, this document includes all actions relevant to the service that processed the denied request, but might omit actions for other services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRequestAuthorizationPolicyOutput) -> dict:
    out: dict = {}
    out["policyDocument"] = value["policy_document"]
    return out


def deserialize_json(data: dict) -> GetRequestAuthorizationPolicyOutput:
    out: GetRequestAuthorizationPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyDocument") is not None:
        out["policy_document"] = data["policyDocument"]
    else:
        out["policy_document"] = None
    return out
