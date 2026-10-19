"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteConnectInstanceIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.instance_id
    import capo_connectcampaignsv2.types.integration_identifier


class DeleteConnectInstanceIntegrationRequest(TypedDict, closed=True):
    connect_instance_id: "capo_connectcampaignsv2.types.instance_id.InstanceId"
    integration_identifier: (
        "capo_connectcampaignsv2.types.integration_identifier.IntegrationIdentifier"
    )


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectInstanceIntegrationRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.integration_identifier

    out["integrationIdentifier"] = (
        capo_connectcampaignsv2.types.integration_identifier.serialize_json(
            value["integration_identifier"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteConnectInstanceIntegrationRequest:
    out: DeleteConnectInstanceIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationIdentifier") is not None:
        import capo_connectcampaignsv2.types.integration_identifier

        out["integration_identifier"] = (
            capo_connectcampaignsv2.types.integration_identifier.deserialize_json(
                data["integrationIdentifier"]
            )
        )
    else:
        import capo_connectcampaignsv2.types._unknown

        out["integration_identifier"] = (
            capo_connectcampaignsv2.types._unknown.UnknownUnionMember("")
        )
    return out
