"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CertificateConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.certificate_configuration

CertificateConfigurationList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.certificate_configuration.CertificateConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateConfigurationList) -> list:
    import capo_bedrock_agentcore_control.types.certificate_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.certificate_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CertificateConfigurationList:
    import capo_bedrock_agentcore_control.types.certificate_configuration

    out: CertificateConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.certificate_configuration.deserialize_json(
                item
            )
        )
    return out
