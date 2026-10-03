"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutDashboardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dashboard_body
    import capo_cloudwatch.types.dashboard_name
    import capo_cloudwatch.types.tag_list


class PutDashboardInput(TypedDict, closed=True):
    dashboard_name: NotRequired["capo_cloudwatch.types.dashboard_name.DashboardName"]
    """<p>The name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, "-", and "_". This parameter is required.</p>"""
    dashboard_body: NotRequired["capo_cloudwatch.types.dashboard_body.DashboardBody"]
    """<p>The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required.</p> <p>For more information about the syntax, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Dashboard-Body-Structure.html">Dashboard Body Structure and Syntax</a>.</p>"""
    tags: NotRequired["capo_cloudwatch.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the dashboard. You can associate as many as 50 tags with a dashboard.</p> <p>Tags can help you organize and categorize your dashboards. You can also use them to scope user permissions by granting a user permission to access or change only dashboards with certain tag values.</p> <p>You can use this parameter only when creating a new dashboard. If you specify <code>Tags</code> when updating an existing dashboard, the tag updates are ignored. To add or update tags on an existing dashboard, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html">TagResource</a>. To remove tags, use <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutDashboardInput) -> dict:
    out: dict = {}
    if "dashboard_name" in value:
        out["DashboardName"] = value["dashboard_name"]
    if "dashboard_body" in value:
        out["DashboardBody"] = value["dashboard_body"]
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutDashboardInput:
    out: PutDashboardInput = {}  # type: ignore[typeddict-item]
    if data.get("DashboardName") is not None:
        out["dashboard_name"] = data["DashboardName"]
    if data.get("DashboardBody") is not None:
        out["dashboard_body"] = data["DashboardBody"]
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutDashboardInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dashboard_name" in value:
        pairs.append((f"{key_prefix}DashboardName", str(value["dashboard_name"])))
    if "dashboard_body" in value:
        pairs.append((f"{key_prefix}DashboardBody", str(value["dashboard_body"])))
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        capo_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> PutDashboardInput:
    out: PutDashboardInput = {}  # type: ignore[typeddict-item]
    child_dashboard_name = el.find("DashboardName")
    if child_dashboard_name is not None:
        out["dashboard_name"] = str(child_dashboard_name.text or "")
    child_dashboard_body = el.find("DashboardBody")
    if child_dashboard_body is not None:
        out["dashboard_body"] = str(child_dashboard_body.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_query(child_tags)
    return out
