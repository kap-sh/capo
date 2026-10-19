"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteDeliverySourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_source_name


class DeleteDeliverySourceRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName"
    """<p>The name of the delivery source that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDeliverySourceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDeliverySourceRequest:
    out: DeleteDeliverySourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
