"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#MonotonicValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.monotonicity
    import capo_lookoutequipment.types.statistical_issue_status


class MonotonicValues(TypedDict, closed=True):
    status: (
        "capo_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus"
    )
    """<p> Indicates whether there is a potential data issue related to having monotonic values. </p>"""
    monotonicity: NotRequired["capo_lookoutequipment.types.monotonicity.Monotonicity"]
    """<p> Indicates the monotonicity of values. Can be INCREASING, DECREASING, or STATIC. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonotonicValues) -> dict:
    out: dict = {}
    import capo_lookoutequipment.types.statistical_issue_status

    out["Status"] = (
        capo_lookoutequipment.types.statistical_issue_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "monotonicity" in value:
        import capo_lookoutequipment.types.monotonicity

        out["Monotonicity"] = (
            capo_lookoutequipment.types.monotonicity.serialize_aws_json_1_0(
                value["monotonicity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MonotonicValues:
    out: MonotonicValues = {}  # type: ignore[typeddict-item]
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
    if data.get("Monotonicity") is not None:
        import capo_lookoutequipment.types.monotonicity

        out["monotonicity"] = (
            capo_lookoutequipment.types.monotonicity.deserialize_aws_json_1_0(
                data["Monotonicity"]
            )
        )
    return out
