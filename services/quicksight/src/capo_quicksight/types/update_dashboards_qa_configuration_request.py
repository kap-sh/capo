"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardsQAConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.dashboards_qa_status


class UpdateDashboardsQAConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard QA configuration that you want to update.</p>"""
    dashboards_qa_status: (
        "capo_quicksight.types.dashboards_qa_status.DashboardsQAStatus"
    )
    """<p>The status of dashboards QA configuration that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardsQAConfigurationRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.dashboards_qa_status

    out["DashboardsQAStatus"] = (
        capo_quicksight.types.dashboards_qa_status.serialize_json(
            value["dashboards_qa_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDashboardsQAConfigurationRequest:
    out: UpdateDashboardsQAConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("DashboardsQAStatus") is not None:
        import capo_quicksight.types.dashboards_qa_status

        out["dashboards_qa_status"] = (
            capo_quicksight.types.dashboards_qa_status.deserialize_json(
                data["DashboardsQAStatus"]
            )
        )
    else:
        import typing

        out["dashboards_qa_status"] = typing.cast(
            "capo_quicksight.types.dashboards_qa_status.DashboardsQAStatus", ""
        )
    return out
