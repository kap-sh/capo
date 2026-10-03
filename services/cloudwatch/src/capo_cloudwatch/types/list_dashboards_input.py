"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListDashboardsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dashboard_name_prefix
    import capo_cloudwatch.types.next_token


class ListDashboardsInput(TypedDict, closed=True):
    dashboard_name_prefix: NotRequired[
        "capo_cloudwatch.types.dashboard_name_prefix.DashboardNamePrefix"
    ]
    """<p>If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, ".", "-", and "_". </p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token returned by a previous call to indicate that there is more data available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDashboardsInput) -> dict:
    out: dict = {}
    if "dashboard_name_prefix" in value:
        out["DashboardNamePrefix"] = value["dashboard_name_prefix"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDashboardsInput:
    out: ListDashboardsInput = {}  # type: ignore[typeddict-item]
    if data.get("DashboardNamePrefix") is not None:
        out["dashboard_name_prefix"] = data["DashboardNamePrefix"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListDashboardsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dashboard_name_prefix" in value:
        pairs.append(
            (f"{key_prefix}DashboardNamePrefix", str(value["dashboard_name_prefix"]))
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListDashboardsInput:
    out: ListDashboardsInput = {}  # type: ignore[typeddict-item]
    child_dashboard_name_prefix = el.find("DashboardNamePrefix")
    if child_dashboard_name_prefix is not None:
        out["dashboard_name_prefix"] = str(child_dashboard_name_prefix.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
