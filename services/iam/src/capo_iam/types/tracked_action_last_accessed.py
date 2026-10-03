"""Generated from Smithy shape ``com.amazonaws.iam#TrackedActionLastAccessed``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.arn_type
    import capo_iam.types.date_type
    import capo_iam.types.string_type


class TrackedActionLastAccessed(TypedDict, closed=True):
    action_name: NotRequired["capo_iam.types.string_type.stringType"]
    """<p>The name of the tracked action to which access was attempted. Tracked actions are actions that report activity to IAM.</p>"""
    last_accessed_entity: NotRequired["capo_iam.types.arn_type.arnType"]
    last_accessed_time: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when an authenticated entity most recently attempted to access the tracked service. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no IAM entities attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""
    last_accessed_region: NotRequired["capo_iam.types.string_type.stringType"]
    """<p>The Region from which the authenticated entity (user or role) last attempted to access the tracked action. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no IAM entities attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TrackedActionLastAccessed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "action_name" in value:
        pairs.append((f"{key_prefix}ActionName", str(value["action_name"])))
    if "last_accessed_entity" in value:
        pairs.append(
            (f"{key_prefix}LastAccessedEntity", str(value["last_accessed_entity"]))
        )
    if "last_accessed_time" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["last_accessed_time"], pairs, f"{key_prefix}LastAccessedTime"
        )
    if "last_accessed_region" in value:
        pairs.append(
            (f"{key_prefix}LastAccessedRegion", str(value["last_accessed_region"]))
        )


def deserialize_query(el: Element) -> TrackedActionLastAccessed:
    out: TrackedActionLastAccessed = {}  # type: ignore[typeddict-item]
    child_action_name = el.find("ActionName")
    if child_action_name is not None:
        out["action_name"] = str(child_action_name.text or "")
    child_last_accessed_entity = el.find("LastAccessedEntity")
    if child_last_accessed_entity is not None:
        out["last_accessed_entity"] = str(child_last_accessed_entity.text or "")
    child_last_accessed_time = el.find("LastAccessedTime")
    if child_last_accessed_time is not None:
        import capo_iam.types.date_type

        out["last_accessed_time"] = capo_iam.types.date_type.deserialize_query(
            child_last_accessed_time
        )
    child_last_accessed_region = el.find("LastAccessedRegion")
    if child_last_accessed_region is not None:
        out["last_accessed_region"] = str(child_last_accessed_region.text or "")
    return out
