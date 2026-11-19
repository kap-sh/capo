"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListServiceActionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.service_action_summaries


class ListServiceActionsOutput(TypedDict, closed=True):
    service_action_summaries: NotRequired[
        "capo_service_catalog.types.service_action_summaries.ServiceActionSummaries"
    ]
    """<p>An object containing information about the service actions associated with the provisioning artifact.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceActionsOutput) -> dict:
    out: dict = {}
    if "service_action_summaries" in value:
        import capo_service_catalog.types.service_action_summaries

        out["ServiceActionSummaries"] = (
            capo_service_catalog.types.service_action_summaries.serialize_aws_json_1_1(
                value["service_action_summaries"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceActionsOutput:
    out: ListServiceActionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionSummaries") is not None:
        import capo_service_catalog.types.service_action_summaries

        out["service_action_summaries"] = (
            capo_service_catalog.types.service_action_summaries.deserialize_aws_json_1_1(
                data["ServiceActionSummaries"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListServiceActionsOutput) -> dict:
    out: dict = {}
    if "service_action_summaries" in value:
        import capo_service_catalog.types.service_action_summaries

        out["ServiceActionSummaries"] = (
            capo_service_catalog.types.service_action_summaries.serialize_cbor(
                value["service_action_summaries"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListServiceActionsOutput:
    out: ListServiceActionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionSummaries") is not None:
        import capo_service_catalog.types.service_action_summaries

        out["service_action_summaries"] = (
            capo_service_catalog.types.service_action_summaries.deserialize_cbor(
                data["ServiceActionSummaries"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
