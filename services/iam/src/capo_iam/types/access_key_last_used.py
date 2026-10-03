"""Generated from Smithy shape ``com.amazonaws.iam#AccessKeyLastUsed``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.date_type
    import capo_iam.types.string_type


class AccessKeyLastUsed(TypedDict, closed=True):
    last_used_date: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>, when the access key was most recently used. This field is null in the following situations:</p> <ul> <li> <p>The user does not have an access key.</p> </li> <li> <p>An access key exists but has not been used since IAM began tracking this information.</p> </li> <li> <p>There is no sign-in data associated with the user.</p> </li> </ul>"""
    service_name: "capo_iam.types.string_type.stringType"
    """<p>The name of the Amazon Web Services service with which this access key was most recently used. The value of this field is "N/A" in the following situations:</p> <ul> <li> <p>The user does not have an access key.</p> </li> <li> <p>An access key exists but has not been used since IAM started tracking this information.</p> </li> <li> <p>There is no sign-in data associated with the user.</p> </li> </ul>"""
    region: "capo_iam.types.string_type.stringType"
    """<p>The Amazon Web Services Region where this access key was most recently used. The value for this field is "N/A" in the following situations:</p> <ul> <li> <p>The user does not have an access key.</p> </li> <li> <p>An access key exists but has not been used since IAM began tracking this information.</p> </li> <li> <p>There is no sign-in data associated with the user.</p> </li> </ul> <p>For more information about Amazon Web Services Regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">Regions and endpoints</a> in the Amazon Web Services General Reference.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessKeyLastUsed, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "last_used_date" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["last_used_date"], pairs, f"{key_prefix}LastUsedDate"
        )
    pairs.append((f"{key_prefix}ServiceName", str(value["service_name"])))
    pairs.append((f"{key_prefix}Region", str(value["region"])))


def deserialize_query(el: Element) -> AccessKeyLastUsed:
    out: AccessKeyLastUsed = {}  # type: ignore[typeddict-item]
    child_last_used_date = el.find("LastUsedDate")
    if child_last_used_date is not None:
        import capo_iam.types.date_type

        out["last_used_date"] = capo_iam.types.date_type.deserialize_query(
            child_last_used_date
        )
    child_service_name = el.find("ServiceName")
    if child_service_name is not None:
        out["service_name"] = str(child_service_name.text or "")
    else:
        raise DeserializationError("AccessKeyLastUsed.service_name required")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    else:
        raise DeserializationError("AccessKeyLastUsed.region required")
    return out
