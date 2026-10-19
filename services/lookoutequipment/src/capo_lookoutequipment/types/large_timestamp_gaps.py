"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LargeTimestampGaps``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.integer
    import capo_lookoutequipment.types.statistical_issue_status


class LargeTimestampGaps(TypedDict, closed=True):
    status: (
        "capo_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus"
    )
    """<p> Indicates whether there is a potential data issue related to large gaps in timestamps. </p>"""
    number_of_large_timestamp_gaps: NotRequired[
        "capo_lookoutequipment.types.integer.Integer"
    ]
    """<p> Indicates the number of large timestamp gaps, if there are any. </p>"""
    max_timestamp_gap_in_days: NotRequired[
        "capo_lookoutequipment.types.integer.Integer"
    ]
    """<p> Indicates the size of the largest timestamp gap, in days. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LargeTimestampGaps) -> dict:
    out: dict = {}
    import capo_lookoutequipment.types.statistical_issue_status

    out["Status"] = (
        capo_lookoutequipment.types.statistical_issue_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "number_of_large_timestamp_gaps" in value:
        out["NumberOfLargeTimestampGaps"] = value["number_of_large_timestamp_gaps"]
    if "max_timestamp_gap_in_days" in value:
        out["MaxTimestampGapInDays"] = value["max_timestamp_gap_in_days"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LargeTimestampGaps:
    out: LargeTimestampGaps = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_lookoutequipment.types.statistical_issue_status

        out["status"] = (
            capo_lookoutequipment.types.statistical_issue_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus",
            "",
        )
    if data.get("NumberOfLargeTimestampGaps") is not None:
        out["number_of_large_timestamp_gaps"] = data["NumberOfLargeTimestampGaps"]
    if data.get("MaxTimestampGapInDays") is not None:
        out["max_timestamp_gap_in_days"] = data["MaxTimestampGapInDays"]
    return out
