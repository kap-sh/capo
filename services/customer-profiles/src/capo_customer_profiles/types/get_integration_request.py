"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255


class GetIntegrationRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    uri: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The URI of the S3 bucket or any other type of data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIntegrationRequest) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> GetIntegrationRequest:
    out: GetIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    else:
        out["uri"] = ""
    return out
