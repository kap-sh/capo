"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetDashboardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dashboard_name


class GetDashboardInput(TypedDict, closed=True):
    dashboard_name: NotRequired["capo_cloudwatch.types.dashboard_name.DashboardName"]
    """<p>The name of the dashboard to be described.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDashboardInput) -> dict:
    out: dict = {}
    if "dashboard_name" in value:
        out["DashboardName"] = value["dashboard_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDashboardInput:
    out: GetDashboardInput = {}  # type: ignore[typeddict-item]
    if data.get("DashboardName") is not None:
        out["dashboard_name"] = data["DashboardName"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetDashboardInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dashboard_name" in value:
        pairs.append((f"{key_prefix}DashboardName", str(value["dashboard_name"])))


def deserialize_query(el: Element) -> GetDashboardInput:
    out: GetDashboardInput = {}  # type: ignore[typeddict-item]
    child_dashboard_name = el.find("DashboardName")
    if child_dashboard_name is not None:
        out["dashboard_name"] = str(child_dashboard_name.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDashboardInput) -> dict:
    out: dict = {}
    if "dashboard_name" in value:
        out["DashboardName"] = value["dashboard_name"]
    return out


def deserialize_cbor(data: dict) -> GetDashboardInput:
    out: GetDashboardInput = {}  # type: ignore[typeddict-item]
    if data.get("DashboardName") is not None:
        out["dashboard_name"] = data["DashboardName"]
    return out
