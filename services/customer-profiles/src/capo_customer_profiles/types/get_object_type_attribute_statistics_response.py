"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetObjectTypeAttributeStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.get_object_type_attribute_statistics_stats
    import capo_customer_profiles.types.timestamp


class GetObjectTypeAttributeStatisticsResponse(TypedDict, closed=True):
    statistics: "capo_customer_profiles.types.get_object_type_attribute_statistics_stats.GetObjectTypeAttributeStatisticsStats"
    """<p>The statistics.</p>"""
    calculated_at: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Time when this statistics was calculated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectTypeAttributeStatisticsResponse) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.get_object_type_attribute_statistics_stats

    out["Statistics"] = (
        capo_customer_profiles.types.get_object_type_attribute_statistics_stats.serialize_json(
            value["statistics"]
        )
    )
    import capo_customer_profiles.types.timestamp

    out["CalculatedAt"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["calculated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetObjectTypeAttributeStatisticsResponse:
    out: GetObjectTypeAttributeStatisticsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Statistics") is not None:
        import capo_customer_profiles.types.get_object_type_attribute_statistics_stats

        out["statistics"] = (
            capo_customer_profiles.types.get_object_type_attribute_statistics_stats.deserialize_json(
                data["Statistics"]
            )
        )
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsResponse.statistics required"
        )
    if data.get("CalculatedAt") is not None:
        import capo_customer_profiles.types.timestamp

        out["calculated_at"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["CalculatedAt"]
        )
    else:
        import datetime

        out["calculated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
