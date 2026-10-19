"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_connector_name
    import capo_bedrock_agentcore_control.types.payment_connector_provision_mode
    import capo_bedrock_agentcore_control.types.payment_connector_status
    import capo_bedrock_agentcore_control.types.payment_connector_type


class PaymentConnectorSummary(TypedDict, closed=True):
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the payment connector.</p>"""
    name: "capo_bedrock_agentcore_control.types.payment_connector_name.PaymentConnectorName"
    """<p>The name of the payment connector.</p>"""
    type: "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
    """<p>The type of the payment connector, which determines the payment provider integration.</p>"""
    provision_mode: NotRequired[
        "capo_bedrock_agentcore_control.types.payment_connector_provision_mode.PaymentConnectorProvisionMode"
    ]
    """<p>Specifies how the payment connector was provisioned. Payment connectors that were created before this field was available return <code>MANUAL</code>.</p> <ul> <li> <p> <code>MANUAL</code> - You provided the credential provider configurations, so you own the credentials.</p> </li> <li> <p> <code>QUICK_CREATE</code> - AgentCore provisioned the credential provider for you, so the credentials are service-managed and you can rotate them with <code>RotatePaymentConnectorCredentials</code>.</p> </li> </ul>"""
    status: "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus"
    """<p>The current status of the payment connector. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment connector was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentConnectorSummary) -> dict:
    out: dict = {}
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.payment_connector_type

    out["type"] = (
        capo_bedrock_agentcore_control.types.payment_connector_type.serialize_json(
            value["type"]
        )
    )
    if "provision_mode" in value:
        import capo_bedrock_agentcore_control.types.payment_connector_provision_mode

        out["provisionMode"] = (
            capo_bedrock_agentcore_control.types.payment_connector_provision_mode.serialize_json(
                value["provision_mode"]
            )
        )
    import capo_bedrock_agentcore_control.types.payment_connector_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_connector_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> PaymentConnectorSummary:
    out: PaymentConnectorSummary = {}  # type: ignore[typeddict-item]
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        out["payment_connector_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.payment_connector_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType",
            "",
        )
    if data.get("provisionMode") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_provision_mode

        out["provision_mode"] = (
            capo_bedrock_agentcore_control.types.payment_connector_provision_mode.deserialize_json(
                data["provisionMode"]
            )
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_connector_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus",
            "",
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
