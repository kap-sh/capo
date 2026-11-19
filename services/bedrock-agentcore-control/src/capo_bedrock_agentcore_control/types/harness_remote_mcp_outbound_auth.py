"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessRemoteMcpOutboundAuth``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.iam_credential_provider


class HarnessRemoteMcpOutboundAuthAwsIamMember(TypedDict, closed=True):
    awsIam: "capo_bedrock_agentcore_control.types.iam_credential_provider.IamCredentialProvider"


class HarnessRemoteMcpOutboundAuthNoneMember(TypedDict, closed=True):
    none: "None"


HarnessRemoteMcpOutboundAuth: TypeAlias = (
    HarnessRemoteMcpOutboundAuthAwsIamMember
    | HarnessRemoteMcpOutboundAuthNoneMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessRemoteMcpOutboundAuth) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"HarnessRemoteMcpOutboundAuth: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "awsIam" in value:
        import capo_bedrock_agentcore_control.types.iam_credential_provider

        return {
            "awsIam": capo_bedrock_agentcore_control.types.iam_credential_provider.serialize_json(
                value["awsIam"]
            )
        }
    elif "none" in value:
        return {"none": {}}
    else:
        raise SerializationError("HarnessRemoteMcpOutboundAuth: no variant present")


def deserialize_json(data: dict) -> HarnessRemoteMcpOutboundAuth:
    if data.get("awsIam") is not None:
        import capo_bedrock_agentcore_control.types.iam_credential_provider

        return {
            "awsIam": capo_bedrock_agentcore_control.types.iam_credential_provider.deserialize_json(
                data["awsIam"]
            )
        }
    elif data.get("none") is not None:
        return {"none": None}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "HarnessRemoteMcpOutboundAuth: no recognized variant key"
        )
