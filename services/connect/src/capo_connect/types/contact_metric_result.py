"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_metric_name
    import capo_connect.types.contact_metric_value


class ContactMetricResult(TypedDict, closed=True):
    name: "capo_connect.types.contact_metric_name.ContactMetricName"
    """<p>The name of the metric that was retrieved. This corresponds to the metric name specified in the request, such as POSITION_IN_QUEUE or ESTIMATED_WAIT_TIME.</p>"""
    value: "capo_connect.types.contact_metric_value.ContactMetricValue"
    """<p>The calculated value for the requested metric. This object contains the numeric result based on the contact's current state in the queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricResult) -> dict:
    out: dict = {}
    import capo_connect.types.contact_metric_name

    out["Name"] = capo_connect.types.contact_metric_name.serialize_json(value["name"])
    import capo_connect.types.contact_metric_value

    out["Value"] = capo_connect.types.contact_metric_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> ContactMetricResult:
    out: ContactMetricResult = {}  # type: ignore[typeddict-item]
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
    if data.get("Value") is not None:
        import capo_connect.types.contact_metric_value

        out["value"] = capo_connect.types.contact_metric_value.deserialize_json(
            data["Value"]
        )
    else:
        import capo_connect.types._unknown

        out["value"] = capo_connect.types._unknown.UnknownUnionMember("")
    return out
