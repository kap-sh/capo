"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetDeliveryOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.configuration_set_name
    import capo_sesv2.types.max_delivery_seconds
    import capo_sesv2.types.sending_pool_name
    import capo_sesv2.types.shared_pool_delivery_mode
    import capo_sesv2.types.tls_policy


class PutConfigurationSetDeliveryOptionsRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set to associate with a dedicated IP pool.</p>"""
    tls_policy: NotRequired["capo_sesv2.types.tls_policy.TlsPolicy"]
    """<p>Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is <code>REQUIRE</code>, messages are only delivered if a TLS connection can be established. If the value is <code>OPTIONAL</code>, messages can be delivered in plain text if a TLS connection can't be established.</p>"""
    sending_pool_name: NotRequired["capo_sesv2.types.sending_pool_name.SendingPoolName"]
    """<p>The name of the dedicated IP pool to associate with the configuration set.</p>"""
    max_delivery_seconds: NotRequired[
        "capo_sesv2.types.max_delivery_seconds.MaxDeliverySeconds"
    ]
    """<p>The maximum amount of time, in seconds, that Amazon SES API v2 will attempt delivery of email. If specified, the value must greater than or equal to 300 seconds (5 minutes) and less than or equal to 50400 seconds (840 minutes). </p>"""
    shared_pool_delivery_mode: NotRequired[
        "capo_sesv2.types.shared_pool_delivery_mode.SharedPoolDeliveryMode"
    ]
    """<p>The shared pool delivery mode for email that you send with the configuration set from shared IP addresses. This setting overrides the shared pool delivery mode of your account. Can be one of the following:</p> <ul> <li> <p> <code>GLOBAL</code> – Amazon SES delivers from your sending Region first and, when it improves your deliverability, also uses Amazon SES shared IP addresses with established sending history in other Amazon Web Services Regions within the same Amazon Web Services partition.</p> </li> <li> <p> <code>REGIONAL</code> – Amazon SES delivers your email only from shared IP addresses in your sending Region.</p> </li> <li> <p> <code>ACCOUNT</code> – The configuration set uses the shared pool delivery mode of your account.</p> </li> </ul> <p>If you don't specify a value, the current value doesn't change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetDeliveryOptionsRequest) -> dict:
    out: dict = {}
    if "tls_policy" in value:
        import capo_sesv2.types.tls_policy

        out["TlsPolicy"] = capo_sesv2.types.tls_policy.serialize_json(
            value["tls_policy"]
        )
    if "sending_pool_name" in value:
        out["SendingPoolName"] = value["sending_pool_name"]
    if "max_delivery_seconds" in value:
        out["MaxDeliverySeconds"] = value["max_delivery_seconds"]
    if "shared_pool_delivery_mode" in value:
        import capo_sesv2.types.shared_pool_delivery_mode

        out["SharedPoolDeliveryMode"] = (
            capo_sesv2.types.shared_pool_delivery_mode.serialize_json(
                value["shared_pool_delivery_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutConfigurationSetDeliveryOptionsRequest:
    out: PutConfigurationSetDeliveryOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("TlsPolicy") is not None:
        import capo_sesv2.types.tls_policy

        out["tls_policy"] = capo_sesv2.types.tls_policy.deserialize_json(
            data["TlsPolicy"]
        )
    if data.get("SendingPoolName") is not None:
        out["sending_pool_name"] = data["SendingPoolName"]
    if data.get("MaxDeliverySeconds") is not None:
        out["max_delivery_seconds"] = data["MaxDeliverySeconds"]
    if data.get("SharedPoolDeliveryMode") is not None:
        import capo_sesv2.types.shared_pool_delivery_mode

        out["shared_pool_delivery_mode"] = (
            capo_sesv2.types.shared_pool_delivery_mode.deserialize_json(
                data["SharedPoolDeliveryMode"]
            )
        )
    return out
