"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.http_endpoint_name
    import capo_firehose.types.http_endpoint_url


class HttpEndpointDescription(TypedDict, closed=True):
    url: NotRequired["capo_firehose.types.http_endpoint_url.HttpEndpointUrl"]
    """<p>The URL of the HTTP endpoint selected as the destination.</p>"""
    name: NotRequired["capo_firehose.types.http_endpoint_name.HttpEndpointName"]
    """<p>The name of the HTTP endpoint selected as the destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointDescription) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointDescription:
    out: HttpEndpointDescription = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


def redact_sensitive(value: HttpEndpointDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
