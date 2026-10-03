"""Generated from Smithy shape ``com.amazonaws.iam#EntityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.date_type
    import capo_iam.types.entity_info


class EntityDetails(TypedDict, closed=True):
    entity_info: "capo_iam.types.entity_info.EntityInfo"
    """<p>The <code>EntityInfo</code> object that contains details about the entity (user or role).</p>"""
    last_authenticated: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the authenticated entity last attempted to access Amazon Web Services. Amazon Web Services does not report unauthenticated requests.</p> <p>This field is null if no IAM entities attempted to access the service within the <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#service-last-accessed-reporting-period">tracking period</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EntityDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.entity_info

    capo_iam.types.entity_info.serialize_query(
        value["entity_info"], pairs, f"{key_prefix}EntityInfo"
    )
    if "last_authenticated" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["last_authenticated"], pairs, f"{key_prefix}LastAuthenticated"
        )


def deserialize_query(el: Element) -> EntityDetails:
    out: EntityDetails = {}  # type: ignore[typeddict-item]
    child_entity_info = el.find("EntityInfo")
    if child_entity_info is not None:
        import capo_iam.types.entity_info

        out["entity_info"] = capo_iam.types.entity_info.deserialize_query(
            child_entity_info
        )
    else:
        raise DeserializationError("EntityDetails.entity_info required")
    child_last_authenticated = el.find("LastAuthenticated")
    if child_last_authenticated is not None:
        import capo_iam.types.date_type

        out["last_authenticated"] = capo_iam.types.date_type.deserialize_query(
            child_last_authenticated
        )
    return out
