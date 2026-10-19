"""Generated from Smithy shape ``com.amazonaws.ses#AddHeaderAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.header_name
    import capo_ses.types.header_value


class AddHeaderAction(TypedDict, closed=True):
    header_name: "capo_ses.types.header_name.HeaderName"
    """<p>The name of the header to add to the incoming message. The name must contain at least one character, and can contain up to 50 characters. It consists of alphanumeric (a–z, A–Z, 0–9) characters and dashes.</p>"""
    header_value: "capo_ses.types.header_value.HeaderValue"
    r"""<p>The content to include in the header. This value can contain up to 2048 characters. It can't contain newline (<code>\n</code>) or carriage return (<code>\r</code>) characters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AddHeaderAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}HeaderName", str(value["header_name"])))
    pairs.append((f"{key_prefix}HeaderValue", str(value["header_value"])))


def deserialize_query(el: Element) -> AddHeaderAction:
    out: AddHeaderAction = {}  # type: ignore[typeddict-item]
    child_header_name = el.find("HeaderName")
    if child_header_name is not None:
        out["header_name"] = str(child_header_name.text or "")
    else:
        out["header_name"] = ""
    child_header_value = el.find("HeaderValue")
    if child_header_value is not None:
        out["header_value"] = str(child_header_value.text or "")
    else:
        out["header_value"] = ""
    return out
