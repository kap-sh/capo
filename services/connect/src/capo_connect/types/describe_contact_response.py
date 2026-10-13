"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact


class DescribeContactResponse(TypedDict, closed=True):
    contact: NotRequired["capo_connect.types.contact.Contact"]
    """<p>Information about the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactResponse) -> dict:
    out: dict = {}
    if "contact" in value:
        import capo_connect.types.contact

        out["Contact"] = capo_connect.types.contact.serialize_json(value["contact"])
    return out


def deserialize_json(data: dict) -> DescribeContactResponse:
    out: DescribeContactResponse = {}  # type: ignore[typeddict-item]
    if data.get("Contact") is not None:
        import capo_connect.types.contact

        out["contact"] = capo_connect.types.contact.deserialize_json(data["Contact"])
    return out


def redact_sensitive(value: DescribeContactResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contact" in value:
        import capo_connect.types.contact

        out["contact"] = capo_connect.types.contact.redact_sensitive(value["contact"])
    return out
