"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#Duration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.duration_value
    import capo_elasticsearch_service.types.time_unit


class Duration(TypedDict, closed=True):
    value: NotRequired["capo_elasticsearch_service.types.duration_value.DurationValue"]
    """<p> Integer to specify the value of a maintenance schedule duration. See the <a href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html" target="_blank">Developer Guide</a> for more information.</p>"""
    unit: NotRequired["capo_elasticsearch_service.types.time_unit.TimeUnit"]
    """<p>Specifies the unit of a maintenance schedule duration. Valid value is HOURS. See the <a href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html" target="_blank">Developer Guide</a> for more information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Duration) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "unit" in value:
        import capo_elasticsearch_service.types.time_unit

        out["Unit"] = capo_elasticsearch_service.types.time_unit.serialize_json(
            value["unit"]
        )
    return out


def deserialize_json(data: dict) -> Duration:
    out: Duration = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Unit") is not None:
        import capo_elasticsearch_service.types.time_unit

        out["unit"] = capo_elasticsearch_service.types.time_unit.deserialize_json(
            data["Unit"]
        )
    return out
