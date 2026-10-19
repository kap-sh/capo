"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetServiceViewInput``."""

from typing_extensions import TypedDict


class GetServiceViewInput(TypedDict, closed=True):
    service_view_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the service view to retrieve details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceViewInput) -> dict:
    out: dict = {}
    out["ServiceViewArn"] = value["service_view_arn"]
    return out


def deserialize_json(data: dict) -> GetServiceViewInput:
    out: GetServiceViewInput = {}  # type: ignore[typeddict-item]
    if data.get("ServiceViewArn") is not None:
        out["service_view_arn"] = data["ServiceViewArn"]
    else:
        out["service_view_arn"] = ""
    return out
