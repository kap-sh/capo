"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetSignalCatalogRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.resource_name


class GetSignalCatalogRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog to retrieve information about. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSignalCatalogRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSignalCatalogRequest:
    out: GetSignalCatalogRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
