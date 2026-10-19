"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#MultipleOperatingModes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.statistical_issue_status


class MultipleOperatingModes(TypedDict, closed=True):
    status: (
        "capo_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus"
    )
    """<p> Indicates whether there is a potential data issue related to having multiple operating modes. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultipleOperatingModes) -> dict:
    out: dict = {}
    import capo_lookoutequipment.types.statistical_issue_status

    out["Status"] = (
        capo_lookoutequipment.types.statistical_issue_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MultipleOperatingModes:
    out: MultipleOperatingModes = {}  # type: ignore[typeddict-item]
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
    return out
