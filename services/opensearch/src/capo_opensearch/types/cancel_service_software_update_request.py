"""Generated from Smithy shape ``com.amazonaws.opensearch#CancelServiceSoftwareUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name


class CancelServiceSoftwareUpdateRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>Name of the OpenSearch Service domain that you want to cancel the service software update on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelServiceSoftwareUpdateRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> CancelServiceSoftwareUpdateRequest:
    out: CancelServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    return out
