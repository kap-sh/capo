"""Generated from Smithy shape ``com.amazonaws.eks#ConnectorConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.connector_config_provider
    import capo_eks.types.string


class ConnectorConfigRequest(TypedDict, closed=True):
    role_arn: "capo_eks.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the role that is authorized to request the connector configuration.</p>"""
    provider: "capo_eks.types.connector_config_provider.ConnectorConfigProvider"
    """<p>The cloud provider for the target cluster to connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorConfigRequest) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    import capo_eks.types.connector_config_provider

    out["provider"] = capo_eks.types.connector_config_provider.serialize_json(
        value["provider"]
    )
    return out


def deserialize_json(data: dict) -> ConnectorConfigRequest:
    out: ConnectorConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("provider") is not None:
        import capo_eks.types.connector_config_provider

        out["provider"] = capo_eks.types.connector_config_provider.deserialize_json(
            data["provider"]
        )
    else:
        import typing

        out["provider"] = typing.cast(
            "capo_eks.types.connector_config_provider.ConnectorConfigProvider", ""
        )
    return out
