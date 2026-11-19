"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DashboardEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dashboard_arn
    import capo_cloudwatch.types.dashboard_name
    import capo_cloudwatch.types.last_modified
    import capo_cloudwatch.types.size


class DashboardEntry(TypedDict, closed=True):
    dashboard_name: NotRequired["capo_cloudwatch.types.dashboard_name.DashboardName"]
    """<p>The name of the dashboard.</p>"""
    dashboard_arn: NotRequired["capo_cloudwatch.types.dashboard_arn.DashboardArn"]
    """<p>The Amazon Resource Name (ARN) of the dashboard.</p>"""
    last_modified: NotRequired["capo_cloudwatch.types.last_modified.LastModified"]
    """<p>The time stamp of when the dashboard was last modified, either by an API call or through the console. This number is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.</p>"""
    size: NotRequired["capo_cloudwatch.types.size.Size"]
    """<p>The size of the dashboard, in bytes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardEntry) -> dict:
    out: dict = {}
    if "dashboard_name" in value:
        out["DashboardName"] = value["dashboard_name"]
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "last_modified" in value:
        import capo_cloudwatch.types.last_modified

        out["LastModified"] = (
            capo_cloudwatch.types.last_modified.serialize_aws_json_1_0(
                value["last_modified"]
            )
        )
    if "size" in value:
        out["Size"] = value["size"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DashboardEntry:
    out: DashboardEntry = {}  # type: ignore[typeddict-item]
    if data.get("DashboardName") is not None:
        out["dashboard_name"] = data["DashboardName"]
    if data.get("DashboardArn") is not None:
        out["dashboard_arn"] = data["DashboardArn"]
    if data.get("LastModified") is not None:
        import capo_cloudwatch.types.last_modified

        out["last_modified"] = (
            capo_cloudwatch.types.last_modified.deserialize_aws_json_1_0(
                data["LastModified"]
            )
        )
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DashboardEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dashboard_name" in value:
        pairs.append((f"{key_prefix}DashboardName", str(value["dashboard_name"])))
    if "dashboard_arn" in value:
        pairs.append((f"{key_prefix}DashboardArn", str(value["dashboard_arn"])))
    if "last_modified" in value:
        import capo_cloudwatch.types.last_modified

        capo_cloudwatch.types.last_modified.serialize_query(
            value["last_modified"], pairs, f"{key_prefix}LastModified"
        )
    if "size" in value:
        pairs.append((f"{key_prefix}Size", str(value["size"])))


def deserialize_query(el: Element) -> DashboardEntry:
    out: DashboardEntry = {}  # type: ignore[typeddict-item]
    child_dashboard_name = el.find("DashboardName")
    if child_dashboard_name is not None:
        out["dashboard_name"] = str(child_dashboard_name.text or "")
    child_dashboard_arn = el.find("DashboardArn")
    if child_dashboard_arn is not None:
        out["dashboard_arn"] = str(child_dashboard_arn.text or "")
    child_last_modified = el.find("LastModified")
    if child_last_modified is not None:
        import capo_cloudwatch.types.last_modified

        out["last_modified"] = capo_cloudwatch.types.last_modified.deserialize_query(
            child_last_modified
        )
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DashboardEntry) -> dict:
    out: dict = {}
    if "dashboard_name" in value:
        out["DashboardName"] = value["dashboard_name"]
    if "dashboard_arn" in value:
        out["DashboardArn"] = value["dashboard_arn"]
    if "last_modified" in value:
        import capo_cloudwatch.types.last_modified

        out["LastModified"] = capo_cloudwatch.types.last_modified.serialize_cbor(
            value["last_modified"]
        )
    if "size" in value:
        out["Size"] = value["size"]
    return out


def deserialize_cbor(data: dict) -> DashboardEntry:
    out: DashboardEntry = {}  # type: ignore[typeddict-item]
    if data.get("DashboardName") is not None:
        out["dashboard_name"] = data["DashboardName"]
    if data.get("DashboardArn") is not None:
        out["dashboard_arn"] = data["DashboardArn"]
    if data.get("LastModified") is not None:
        import capo_cloudwatch.types.last_modified

        out["last_modified"] = capo_cloudwatch.types.last_modified.deserialize_cbor(
            data["LastModified"]
        )
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    return out
