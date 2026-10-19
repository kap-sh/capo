"""Generated from Smithy shape ``com.amazonaws.s3#RecordExpiration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.expiration_state
    import capo_s3.types.record_expiration_days


class RecordExpiration(TypedDict, closed=True):
    expiration: "capo_s3.types.expiration_state.ExpirationState"
    """<p> Specifies whether journal table record expiration is enabled or disabled. </p>"""
    days: NotRequired["capo_s3.types.record_expiration_days.RecordExpirationDays"]
    """<p> If you enable journal table record expiration, you can set the number of days to retain your journal table records. Journal table records must be retained for a minimum of 7 days. To set this value, specify any whole number from <code>7</code> to <code>2147483647</code>. For example, to retain your journal table records for one year, set this value to <code>365</code>. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: RecordExpiration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.expiration_state

    capo_s3.types.expiration_state.serialize_xml(value["expiration"], el, "Expiration")
    if "days" in value:
        SubElement(el, "Days").text = str(value["days"])


def deserialize_xml(el: Element) -> RecordExpiration:
    out: RecordExpiration = {}  # type: ignore[typeddict-item]
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import capo_s3.types.expiration_state

        out["expiration"] = capo_s3.types.expiration_state.deserialize_xml(
            child_expiration
        )
    else:
        import typing

        out["expiration"] = typing.cast(
            "capo_s3.types.expiration_state.ExpirationState", ""
        )
    child_days = el.find("Days")
    if child_days is not None:
        out["days"] = int(child_days.text or "")
    return out
