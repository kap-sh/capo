"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.report_name
    import capo_cost_and_usage_report_service.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName"
    """<p>The report name of the report definition that tags are to be associated with.</p>"""
    tags: "capo_cost_and_usage_report_service.types.tag_list.TagList"
    """<p>The tags to be assigned to the report definition resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    import capo_cost_and_usage_report_service.types.tag_list

    out["Tags"] = (
        capo_cost_and_usage_report_service.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReportName") is not None:
        out["report_name"] = data["ReportName"]
    else:
        out["report_name"] = ""
    if data.get("Tags") is not None:
        import capo_cost_and_usage_report_service.types.tag_list

        out["tags"] = (
            capo_cost_and_usage_report_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    else:
        out["tags"] = []
    return out
