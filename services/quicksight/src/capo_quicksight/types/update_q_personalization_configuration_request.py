"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateQPersonalizationConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.personalization_mode


class UpdateQPersonalizationConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account account that contains the personalization configuration that the user wants to update.</p>"""
    personalization_mode: (
        "capo_quicksight.types.personalization_mode.PersonalizationMode"
    )
    """<p>An option to allow Amazon Quick Sight to customize data stories with user specific metadata, specifically location and job information, in your IAM Identity Center instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQPersonalizationConfigurationRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.personalization_mode

    out["PersonalizationMode"] = (
        capo_quicksight.types.personalization_mode.serialize_json(
            value["personalization_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateQPersonalizationConfigurationRequest:
    out: UpdateQPersonalizationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("PersonalizationMode") is not None:
        import capo_quicksight.types.personalization_mode

        out["personalization_mode"] = (
            capo_quicksight.types.personalization_mode.deserialize_json(
                data["PersonalizationMode"]
            )
        )
    else:
        import typing

        out["personalization_mode"] = typing.cast(
            "capo_quicksight.types.personalization_mode.PersonalizationMode", ""
        )
    return out
