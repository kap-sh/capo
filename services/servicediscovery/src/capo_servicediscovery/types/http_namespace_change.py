"""Generated from Smithy shape ``com.amazonaws.servicediscovery#HttpNamespaceChange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.resource_description


class HttpNamespaceChange(TypedDict, closed=True):
    description: "capo_servicediscovery.types.resource_description.ResourceDescription"
    """<p>An updated description for the HTTP namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpNamespaceChange) -> dict:
    out: dict = {}
    out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpNamespaceChange:
    out: HttpNamespaceChange = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    return out
