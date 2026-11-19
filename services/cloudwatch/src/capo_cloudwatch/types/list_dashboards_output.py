"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListDashboardsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dashboard_entries
    import capo_cloudwatch.types.next_token


class ListDashboardsOutput(TypedDict, closed=True):
    dashboard_entries: NotRequired[
        "capo_cloudwatch.types.dashboard_entries.DashboardEntries"
    ]
    """<p>The list of matching dashboards.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDashboardsOutput) -> dict:
    out: dict = {}
    if "dashboard_entries" in value:
        import capo_cloudwatch.types.dashboard_entries

        out["DashboardEntries"] = (
            capo_cloudwatch.types.dashboard_entries.serialize_aws_json_1_0(
                value["dashboard_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDashboardsOutput:
    out: ListDashboardsOutput = {}  # type: ignore[typeddict-item]
    if data.get("DashboardEntries") is not None:
        import capo_cloudwatch.types.dashboard_entries

        out["dashboard_entries"] = (
            capo_cloudwatch.types.dashboard_entries.deserialize_aws_json_1_0(
                data["DashboardEntries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListDashboardsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dashboard_entries" in value:
        import capo_cloudwatch.types.dashboard_entries

        capo_cloudwatch.types.dashboard_entries.serialize_query(
            value["dashboard_entries"], pairs, f"{key_prefix}DashboardEntries"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListDashboardsOutput:
    out: ListDashboardsOutput = {}  # type: ignore[typeddict-item]
    child_dashboard_entries = el.find("DashboardEntries")
    if child_dashboard_entries is not None:
        import capo_cloudwatch.types.dashboard_entries

        out["dashboard_entries"] = (
            capo_cloudwatch.types.dashboard_entries.deserialize_query(
                child_dashboard_entries
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDashboardsOutput) -> dict:
    out: dict = {}
    if "dashboard_entries" in value:
        import capo_cloudwatch.types.dashboard_entries

        out["DashboardEntries"] = (
            capo_cloudwatch.types.dashboard_entries.serialize_cbor(
                value["dashboard_entries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListDashboardsOutput:
    out: ListDashboardsOutput = {}  # type: ignore[typeddict-item]
    if data.get("DashboardEntries") is not None:
        import capo_cloudwatch.types.dashboard_entries

        out["dashboard_entries"] = (
            capo_cloudwatch.types.dashboard_entries.deserialize_cbor(
                data["DashboardEntries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
