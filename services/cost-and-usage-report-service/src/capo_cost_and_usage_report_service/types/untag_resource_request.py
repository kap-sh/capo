"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_and_usage_report_service.types.report_name
    import capo_cost_and_usage_report_service.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    report_name: "capo_cost_and_usage_report_service.types.report_name.ReportName"
    """<p>The report name of the report definition that tags are to be disassociated from.</p>"""
    tag_keys: "capo_cost_and_usage_report_service.types.tag_key_list.TagKeyList"
    """<p>The tags to be disassociated from the report definition resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ReportName"] = value["report_name"]
    import capo_cost_and_usage_report_service.types.tag_key_list

    out["TagKeys"] = (
        capo_cost_and_usage_report_service.types.tag_key_list.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReportName") is not None:
        out["report_name"] = data["ReportName"]
    else:
        out["report_name"] = ""
    if data.get("TagKeys") is not None:
        import capo_cost_and_usage_report_service.types.tag_key_list

        out["tag_keys"] = (
            capo_cost_and_usage_report_service.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
