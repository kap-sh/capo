"""Generated from Smithy shape ``com.amazonaws.dax#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.integer
    import capo_dax.types.string


class Endpoint(TypedDict, closed=True):
    address: NotRequired["capo_dax.types.string.String"]
    """<p>The DNS hostname of the endpoint.</p>"""
    port: "capo_dax.types.integer.Integer"
    """<p>The port number that applications should use to connect to the endpoint.</p>"""
    url: NotRequired["capo_dax.types.string.String"]
    """<p>The URL that applications should use to connect to the endpoint. The default ports are 8111 for the "dax" protocol and 9111 for the "daxs" protocol.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    out["Port"] = value.get("port", 0)
    if "url" in value:
        out["URL"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    else:
        out["port"] = 0
    if data.get("URL") is not None:
        out["url"] = data["URL"]
    return out
