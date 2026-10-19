"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_metric_name


class ContactMetricInfo(TypedDict, closed=True):
    name: "capo_connect.types.contact_metric_name.ContactMetricName"
    """<p>The name of the metric to retrieve. Supported values are POSITION_IN_QUEUE (returns the contact's current position in the queue) and ESTIMATED_WAIT_TIME (returns the predicted wait time in seconds).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricInfo) -> dict:
    out: dict = {}
    import capo_connect.types.contact_metric_name

    out["Name"] = capo_connect.types.contact_metric_name.serialize_json(value["name"])
    return out


def deserialize_json(data: dict) -> ContactMetricInfo:
    out: ContactMetricInfo = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_connect.types.contact_metric_name

        out["name"] = capo_connect.types.contact_metric_name.deserialize_json(
            data["Name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_connect.types.contact_metric_name.ContactMetricName", ""
        )
    return out
