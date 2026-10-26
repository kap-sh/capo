"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PutConnectInstanceIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.instance_id
    import capo_connectcampaignsv2.types.integration_config


class PutConnectInstanceIntegrationRequest(TypedDict, closed=True):
    connect_instance_id: "capo_connectcampaignsv2.types.instance_id.InstanceId"
    integration_config: (
        "capo_connectcampaignsv2.types.integration_config.IntegrationConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: PutConnectInstanceIntegrationRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.integration_config

    out["integrationConfig"] = (
        capo_connectcampaignsv2.types.integration_config.serialize_json(
            value["integration_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutConnectInstanceIntegrationRequest:
    out: PutConnectInstanceIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationConfig") is not None:
        import capo_connectcampaignsv2.types.integration_config

        out["integration_config"] = (
            capo_connectcampaignsv2.types.integration_config.deserialize_json(
                data["integrationConfig"]
            )
        )
    else:
        out["integration_config"] = {"$unknown": {"name": ""}}
    return out
