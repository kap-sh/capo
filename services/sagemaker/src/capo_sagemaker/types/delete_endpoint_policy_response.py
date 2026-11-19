"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteEndpointPolicyResponse``."""

from typing_extensions import TypedDict


class DeleteEndpointPolicyResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEndpointPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEndpointPolicyResponse:
    out: DeleteEndpointPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
