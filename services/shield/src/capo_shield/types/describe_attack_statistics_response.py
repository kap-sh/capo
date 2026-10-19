"""Generated from Smithy shape ``com.amazonaws.shield#DescribeAttackStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_shield.errors import DeserializationError

if TYPE_CHECKING:
    import capo_shield.types.attack_statistics_data_list
    import capo_shield.types.time_range


class DescribeAttackStatisticsResponse(TypedDict, closed=True):
    time_range: "capo_shield.types.time_range.TimeRange"
    """<p>The time range of the attack.</p>"""
    data_items: "capo_shield.types.attack_statistics_data_list.AttackStatisticsDataList"
    """<p>The data that describes the attacks detected during the time period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttackStatisticsResponse) -> dict:
    out: dict = {}
    import capo_shield.types.time_range

    out["TimeRange"] = capo_shield.types.time_range.serialize_aws_json_1_1(
        value["time_range"]
    )
    import capo_shield.types.attack_statistics_data_list

    out["DataItems"] = (
        capo_shield.types.attack_statistics_data_list.serialize_aws_json_1_1(
            value["data_items"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttackStatisticsResponse:
    out: DescribeAttackStatisticsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TimeRange") is not None:
        import capo_shield.types.time_range

        out["time_range"] = capo_shield.types.time_range.deserialize_aws_json_1_1(
            data["TimeRange"]
        )
    else:
        raise DeserializationError(
            "DescribeAttackStatisticsResponse.time_range required"
        )
    if data.get("DataItems") is not None:
        import capo_shield.types.attack_statistics_data_list

        out["data_items"] = (
            capo_shield.types.attack_statistics_data_list.deserialize_aws_json_1_1(
                data["DataItems"]
            )
        )
    else:
        out["data_items"] = []
    return out
