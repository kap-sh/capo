"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordIamCredentialProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.iam_role_arn
    import capo_agent_registry_control.types.iam_signing_region
    import capo_agent_registry_control.types.iam_signing_service_name


class RegistryRecordIamCredentialProvider(TypedDict, closed=True):
    role_arn: NotRequired["capo_agent_registry_control.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to assume for request signing.</p>"""
    service: NotRequired[
        "capo_agent_registry_control.types.iam_signing_service_name.IamSigningServiceName"
    ]
    """<p>The service name to use for request signing, such as execute-api.</p>"""
    region: NotRequired[
        "capo_agent_registry_control.types.iam_signing_region.IamSigningRegion"
    ]
    """<p>The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordIamCredentialProvider) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "service" in value:
        out["service"] = value["service"]
    if "region" in value:
        out["region"] = value["region"]
    return out


def deserialize_json(data: dict) -> RegistryRecordIamCredentialProvider:
    out: RegistryRecordIamCredentialProvider = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("service") is not None:
        out["service"] = data["service"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    return out
