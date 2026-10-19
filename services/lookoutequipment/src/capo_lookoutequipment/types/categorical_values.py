"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CategoricalValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.integer
    import capo_lookoutequipment.types.statistical_issue_status


class CategoricalValues(TypedDict, closed=True):
    status: (
        "capo_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus"
    )
    """<p> Indicates whether there is a potential data issue related to categorical values. </p>"""
    number_of_category: NotRequired["capo_lookoutequipment.types.integer.Integer"]
    """<p> Indicates the number of categories in the data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CategoricalValues) -> dict:
    out: dict = {}
    import capo_lookoutequipment.types.statistical_issue_status

    out["Status"] = (
        capo_lookoutequipment.types.statistical_issue_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "number_of_category" in value:
        out["NumberOfCategory"] = value["number_of_category"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CategoricalValues:
    out: CategoricalValues = {}  # type: ignore[typeddict-item]
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
    if data.get("NumberOfCategory") is not None:
        out["number_of_category"] = data["NumberOfCategory"]
    return out
