"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HttpProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.namespace_name


class HttpProperties(TypedDict, closed=True):
    http_name: NotRequired["capo_servicediscovery.types.namespace_name.NamespaceName"]
    """<p>The name of an HTTP namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpProperties) -> dict:
    out: dict = {}
    if "http_name" in value:
        out["HttpName"] = value["http_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpProperties:
    out: HttpProperties = {}  # type: ignore[typeddict-item]
    if data.get("HttpName") is not None:
        out["http_name"] = data["HttpName"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HttpProperties) -> dict:
    out: dict = {}
    if "http_name" in value:
        out["HttpName"] = value["http_name"]
    return out


def deserialize_cbor(data: dict) -> HttpProperties:
    out: HttpProperties = {}  # type: ignore[typeddict-item]
    if data.get("HttpName") is not None:
        out["http_name"] = data["HttpName"]
    return out
