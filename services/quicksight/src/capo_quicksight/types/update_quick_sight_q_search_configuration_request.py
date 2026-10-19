"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateQuickSightQSearchConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.q_search_status


class UpdateQuickSightQSearchConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the Quick Sight Q Search configuration that you want to update.</p>"""
    q_search_status: "capo_quicksight.types.q_search_status.QSearchStatus"
    """<p>The status of the Quick Sight Q Search configuration that the user wants to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuickSightQSearchConfigurationRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.q_search_status

    out["QSearchStatus"] = capo_quicksight.types.q_search_status.serialize_json(
        value["q_search_status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateQuickSightQSearchConfigurationRequest:
    out: UpdateQuickSightQSearchConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("QSearchStatus") is not None:
        import capo_quicksight.types.q_search_status

        out["q_search_status"] = capo_quicksight.types.q_search_status.deserialize_json(
            data["QSearchStatus"]
        )
    else:
        import typing

        out["q_search_status"] = typing.cast(
            "capo_quicksight.types.q_search_status.QSearchStatus", ""
        )
    return out
