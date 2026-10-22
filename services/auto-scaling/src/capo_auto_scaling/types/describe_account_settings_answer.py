"""Generated from Smithy shape ``com.amazonaws.autoscaling#DescribeAccountSettingsAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.account_settings
    import capo_auto_scaling.types.xml_string


class DescribeAccountSettingsAnswer(TypedDict, closed=True):
    settings: NotRequired["capo_auto_scaling.types.account_settings.AccountSettings"]
    """<p> Information about the account settings. </p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p> A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is <code>null</code> when there are no more items to return. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAccountSettingsAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "settings" in value:
        import capo_auto_scaling.types.account_settings

        capo_auto_scaling.types.account_settings.serialize_query(
            value["settings"], pairs, f"{key_prefix}Settings"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAccountSettingsAnswer:
    out: DescribeAccountSettingsAnswer = {}  # type: ignore[typeddict-item]
    child_settings = el.find("Settings")
    if child_settings is not None:
        import capo_auto_scaling.types.account_settings

        out["settings"] = capo_auto_scaling.types.account_settings.deserialize_query(
            child_settings
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
