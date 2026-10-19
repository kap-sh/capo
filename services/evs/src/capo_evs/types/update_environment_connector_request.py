"""Generated from Smithy shape ``com.amazonaws.evs#UpdateEnvironmentConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.appliance_fqdn
    import capo_evs.types.client_token
    import capo_evs.types.connector_id
    import capo_evs.types.environment_id
    import capo_evs.types.secret_identifier


class UpdateEnvironmentConnectorRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector update request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "capo_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment that the connector belongs to.</p>"""
    connector_id: "capo_evs.types.connector_id.ConnectorId"
    """<p>A unique ID for the connector to update.</p>"""
    appliance_fqdn: NotRequired["capo_evs.types.appliance_fqdn.ApplianceFqdn"]
    """<p>The new fully qualified domain name (FQDN) of the VCF appliance that the connector connects to.</p>"""
    secret_identifier: NotRequired["capo_evs.types.secret_identifier.SecretIdentifier"]
    """<p>The new ARN or name of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateEnvironmentConnectorRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["environmentId"] = value["environment_id"]
    out["connectorId"] = value["connector_id"]
    if "appliance_fqdn" in value:
        out["applianceFqdn"] = value["appliance_fqdn"]
    if "secret_identifier" in value:
        out["secretIdentifier"] = value["secret_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateEnvironmentConnectorRequest:
    out: UpdateEnvironmentConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("connectorId") is not None:
        out["connector_id"] = data["connectorId"]
    else:
        out["connector_id"] = ""
    if data.get("applianceFqdn") is not None:
        out["appliance_fqdn"] = data["applianceFqdn"]
    if data.get("secretIdentifier") is not None:
        out["secret_identifier"] = data["secretIdentifier"]
    return out
