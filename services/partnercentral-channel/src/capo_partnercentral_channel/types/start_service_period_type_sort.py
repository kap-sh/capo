"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#StartServicePeriodTypeSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.sort_order
    import capo_partnercentral_channel.types.start_service_period_type_sort_name


class StartServicePeriodTypeSort(TypedDict, closed=True):
    sort_order: "capo_partnercentral_channel.types.sort_order.SortOrder"
    """<p>The sort order (ascending or descending).</p>"""
    sort_by: "capo_partnercentral_channel.types.start_service_period_type_sort_name.StartServicePeriodTypeSortName"
    """<p>The field to sort by.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartServicePeriodTypeSort) -> dict:
    out: dict = {}
    import capo_partnercentral_channel.types.sort_order

    out["sortOrder"] = (
        capo_partnercentral_channel.types.sort_order.serialize_aws_json_1_0(
            value["sort_order"]
        )
    )
    import capo_partnercentral_channel.types.start_service_period_type_sort_name

    out["sortBy"] = (
        capo_partnercentral_channel.types.start_service_period_type_sort_name.serialize_aws_json_1_0(
            value["sort_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartServicePeriodTypeSort:
    out: StartServicePeriodTypeSort = {}  # type: ignore[typeddict-item]
    if data.get("sortOrder") is not None:
        import capo_partnercentral_channel.types.sort_order

        out["sort_order"] = (
            capo_partnercentral_channel.types.sort_order.deserialize_aws_json_1_0(
                data["sortOrder"]
            )
        )
    else:
        import typing

        out["sort_order"] = typing.cast(
            "capo_partnercentral_channel.types.sort_order.SortOrder", ""
        )
    if data.get("sortBy") is not None:
        import capo_partnercentral_channel.types.start_service_period_type_sort_name

        out["sort_by"] = (
            capo_partnercentral_channel.types.start_service_period_type_sort_name.deserialize_aws_json_1_0(
                data["sortBy"]
            )
        )
    else:
        import typing

        out["sort_by"] = typing.cast(
            "capo_partnercentral_channel.types.start_service_period_type_sort_name.StartServicePeriodTypeSortName",
            "",
        )
    return out
