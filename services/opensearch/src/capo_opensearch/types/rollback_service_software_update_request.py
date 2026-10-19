"""Generated from Smithy shape ``com.amazonaws.opensearch#RollbackServiceSoftwareUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_name


class RollbackServiceSoftwareUpdateRequest(TypedDict, closed=True):
    domain_name: "capo_opensearch.types.domain_name.DomainName"
    """<p>The name of the domain to roll back the service software update on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackServiceSoftwareUpdateRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    return out


def deserialize_json(data: dict) -> RollbackServiceSoftwareUpdateRequest:
    out: RollbackServiceSoftwareUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainName") is not None:
        out["domain_name"] = data["DomainName"]
    else:
        out["domain_name"] = ""
    return out
