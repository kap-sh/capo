"""Generated from Smithy shape ``com.amazonaws.evs#CreateEnvironmentConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.appliance_fqdn
    import capo_evs.types.client_token
    import capo_evs.types.connector_type
    import capo_evs.types.environment_id
    import capo_evs.types.secret_identifier


class CreateEnvironmentConnectorRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the connector creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "capo_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment to create the connector in.</p>"""
    type: "capo_evs.types.connector_type.ConnectorType"
    """<p>The type of connector to create.</p> <ul> <li> <p> <code>OPERATIONS_MANAGER</code>: Connector to an Operations Manager appliance. Required for VCF 9x environments.</p> </li> <li> <p> <code>SDDC_MANAGER</code>: Connector to an SDDC Manager appliance. Required for VCF 5.x environments.</p> </li> <li> <p> <code>VCENTER</code>: Connector to a vCenter Server appliance. Required for features that depend on vCenter, such as Windows Server license-included.</p> </li> </ul>"""
    appliance_fqdn: "capo_evs.types.appliance_fqdn.ApplianceFqdn"
    """<p>The fully qualified domain name (FQDN) of the VCF appliance that the connector targets.</p>"""
    secret_identifier: "capo_evs.types.secret_identifier.SecretIdentifier"
    """<p>The ARN or name of the Amazon Web Services Secrets Manager secret that stores the credentials for the VCF appliance. <code>SDDC_MANAGER</code> requires an <code>apiKey</code> field; <code>OPERATIONS_MANAGER</code> and <code>VCENTER</code> require <code>username</code> and <code>password</code> fields.</p> <important> <p>Do not use credentials with Administrator privileges. We recommend using a service account with read-only permissions.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentConnectorRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["environmentId"] = value["environment_id"]
    import capo_evs.types.connector_type

    out["type"] = capo_evs.types.connector_type.serialize_aws_json_1_0(value["type"])
    out["applianceFqdn"] = value["appliance_fqdn"]
    out["secretIdentifier"] = value["secret_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentConnectorRequest:
    out: CreateEnvironmentConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("type") is not None:
        import capo_evs.types.connector_type

        out["type"] = capo_evs.types.connector_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_evs.types.connector_type.ConnectorType", "")
    if data.get("applianceFqdn") is not None:
        out["appliance_fqdn"] = data["applianceFqdn"]
    else:
        out["appliance_fqdn"] = ""
    if data.get("secretIdentifier") is not None:
        out["secret_identifier"] = data["secretIdentifier"]
    else:
        out["secret_identifier"] = ""
    return out
