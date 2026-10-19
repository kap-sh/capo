"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardLinksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.link_entity_arn_list
    import capo_quicksight.types.short_restrictive_resource_id


class UpdateDashboardLinksRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard whose links you want to update.</p>"""
    dashboard_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for the dashboard.</p>"""
    link_entities: "capo_quicksight.types.link_entity_arn_list.LinkEntityArnList"
    """<p> list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardLinksRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.link_entity_arn_list

    out["LinkEntities"] = capo_quicksight.types.link_entity_arn_list.serialize_json(
        value["link_entities"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDashboardLinksRequest:
    out: UpdateDashboardLinksRequest = {}  # type: ignore[typeddict-item]
    if data.get("LinkEntities") is not None:
        import capo_quicksight.types.link_entity_arn_list

        out["link_entities"] = (
            capo_quicksight.types.link_entity_arn_list.deserialize_json(
                data["LinkEntities"]
            )
        )
    else:
        out["link_entities"] = []
    return out
