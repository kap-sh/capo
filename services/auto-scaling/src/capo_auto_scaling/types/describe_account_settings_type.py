"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeAccountSettingsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.ascii_string_max_len255
    import capo_auto_scaling.types.max_records
    import capo_auto_scaling.types.xml_string


class DescribeAccountSettingsType(TypedDict, closed=True):
    name: NotRequired[
        "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p> The name of the account setting to describe. If you omit this parameter, all account settings are described. </p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p> The token for the next set of items to return. (You received this token from a previous call.) </p>"""
    max_records: NotRequired["capo_auto_scaling.types.max_records.MaxRecords"]
    """<p> The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountSettingsType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeAccountSettingsType:
    out: DescribeAccountSettingsType = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
