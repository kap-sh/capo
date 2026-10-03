"""Generated from Smithy shape ``com.amazonaws.connect#StartContactConversationalAnalyticsJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.analytics_configuration
    import capo_connect.types.analytics_modes
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class StartContactConversationalAnalyticsJobRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    analytics_modes: "capo_connect.types.analytics_modes.AnalyticsModes"
    """<p>The analytics modes to run for the contact. Valid values: <code>PostContact</code>.</p>"""
    analytics_configuration: (
        "capo_connect.types.analytics_configuration.AnalyticsConfiguration"
    )
    """<p>The configuration for the conversational analytics job.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactConversationalAnalyticsJobRequest) -> dict:
    out: dict = {}
    import capo_connect.types.analytics_modes

    out["AnalyticsModes"] = capo_connect.types.analytics_modes.serialize_json(
        value["analytics_modes"]
    )
    import capo_connect.types.analytics_configuration

    out["AnalyticsConfiguration"] = (
        capo_connect.types.analytics_configuration.serialize_json(
            value["analytics_configuration"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartContactConversationalAnalyticsJobRequest:
    out: StartContactConversationalAnalyticsJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("AnalyticsModes") is not None:
        import capo_connect.types.analytics_modes

        out["analytics_modes"] = capo_connect.types.analytics_modes.deserialize_json(
            data["AnalyticsModes"]
        )
    else:
        raise DeserializationError(
            "StartContactConversationalAnalyticsJobRequest.analytics_modes required"
        )
    if data.get("AnalyticsConfiguration") is not None:
        import capo_connect.types.analytics_configuration

        out["analytics_configuration"] = (
            capo_connect.types.analytics_configuration.deserialize_json(
                data["AnalyticsConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartContactConversationalAnalyticsJobRequest.analytics_configuration required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
