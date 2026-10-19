"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointCommonAttribute``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.http_endpoint_attribute_name
    import capo_firehose.types.http_endpoint_attribute_value


class HttpEndpointCommonAttribute(TypedDict, closed=True):
    attribute_name: (
        "capo_firehose.types.http_endpoint_attribute_name.HttpEndpointAttributeName"
    )
    """<p>The name of the HTTP endpoint common attribute.</p>"""
    attribute_value: (
        "capo_firehose.types.http_endpoint_attribute_value.HttpEndpointAttributeValue"
    )
    """<p>The value of the HTTP endpoint common attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointCommonAttribute) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    out["AttributeValue"] = value["attribute_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointCommonAttribute:
    out: HttpEndpointCommonAttribute = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("AttributeValue") is not None:
        out["attribute_value"] = data["AttributeValue"]
    else:
        out["attribute_value"] = ""
    return out


def redact_sensitive(value: HttpEndpointCommonAttribute) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attribute_name" in value:
        out["attribute_name"] = "*** Sensitive Data Redacted ***"
    if "attribute_value" in value:
        out["attribute_value"] = "*** Sensitive Data Redacted ***"
    return out
