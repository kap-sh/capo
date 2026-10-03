"""Generated from Smithy shape ``com.amazonaws.iam#RoleLastUsed``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.date_type
    import capo_iam.types.string_type


class RoleLastUsed(TypedDict, closed=True):
    last_used_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a> that the role was last used.</p> <p>This field is null if the role has not been used within the IAM tracking period. For more information about the tracking period, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period">Regions where data is tracked</a> in the <i>IAM User Guide</i>. </p>"""
    region: NotRequired["capo_iam.types.string_type.stringType"]
    """<p>The name of the Amazon Web Services Region in which the role was last used.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RoleLastUsed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "last_used_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["last_used_date"], pairs, f"{key_prefix}LastUsedDate"
        )
    if "region" in value:
        pairs.append((f"{key_prefix}Region", str(value["region"])))


def deserialize_query(el: Element) -> RoleLastUsed:
    out: RoleLastUsed = {}  # type: ignore[typeddict-item]
    child_last_used_date = el.find("LastUsedDate")
    if child_last_used_date is not None:
        import capo_iam.types.date_type

        out["last_used_date"] = capo_iam.types.date_type.deserialize_query(
            child_last_used_date
        )
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    return out
