"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.http_endpoint_access_key
    import capo_firehose.types.http_endpoint_name
    import capo_firehose.types.http_endpoint_url


class HttpEndpointConfiguration(TypedDict, closed=True):
    url: "capo_firehose.types.http_endpoint_url.HttpEndpointUrl"
    """<p>The URL of the HTTP endpoint selected as the destination.</p> <important> <p>If you choose an HTTP endpoint as your destination, review and follow the instructions in the <a href="https://docs.aws.amazon.com/firehose/latest/dev/httpdeliveryrequestresponse.html">Appendix - HTTP Endpoint Delivery Request and Response Specifications</a>.</p> </important>"""
    name: NotRequired["capo_firehose.types.http_endpoint_name.HttpEndpointName"]
    """<p>The name of the HTTP endpoint selected as the destination.</p>"""
    access_key: NotRequired[
        "capo_firehose.types.http_endpoint_access_key.HttpEndpointAccessKey"
    ]
    """<p>The access key required for Kinesis Firehose to authenticate with the HTTP endpoint selected as the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointConfiguration) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    if "name" in value:
        out["Name"] = value["name"]
    if "access_key" in value:
        out["AccessKey"] = value["access_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointConfiguration:
    out: HttpEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("HttpEndpointConfiguration.url required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AccessKey") is not None:
        out["access_key"] = data["AccessKey"]
    return out
