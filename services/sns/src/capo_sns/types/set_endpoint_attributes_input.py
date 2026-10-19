"""Generated from Smithy shape ``com.amazonaws.sns#SetEndpointAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.map_string_to_string
    import capo_sns.types.string


class SetEndpointAttributesInput(TypedDict, closed=True):
    endpoint_arn: "capo_sns.types.string.String"
    """<p>EndpointArn used for <code>SetEndpointAttributes</code> action.</p>"""
    attributes: "capo_sns.types.map_string_to_string.MapStringToString"
    """<p>A map of the endpoint attributes. Attributes in this map include the following:</p> <ul> <li> <p> <code>CustomUserData</code> – arbitrary user data to associate with the endpoint. Amazon SNS does not use this data. The data must be in UTF-8 format and less than 2KB.</p> </li> <li> <p> <code>Enabled</code> – flag that enables/disables delivery to the endpoint. Amazon SNS will set this to false when a notification service indicates to Amazon SNS that the endpoint is invalid. Users can set it back to true, typically after updating Token.</p> </li> <li> <p> <code>Token</code> – device token, also referred to as a registration id, for an app and mobile device. This is returned from the notification service when an app and mobile device are registered with the notification service.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetEndpointAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EndpointArn", str(value["endpoint_arn"])))
    import capo_sns.types.map_string_to_string

    capo_sns.types.map_string_to_string.serialize_query(
        value["attributes"], pairs, f"{key_prefix}Attributes"
    )


def deserialize_query(el: Element) -> SetEndpointAttributesInput:
    out: SetEndpointAttributesInput = {}  # type: ignore[typeddict-item]
    child_endpoint_arn = el.find("EndpointArn")
    if child_endpoint_arn is not None:
        out["endpoint_arn"] = str(child_endpoint_arn.text or "")
    else:
        out["endpoint_arn"] = ""
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_sns.types.map_string_to_string

        out["attributes"] = capo_sns.types.map_string_to_string.deserialize_query(
            child_attributes
        )
    else:
        out["attributes"] = {}
    return out
