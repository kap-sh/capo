"""Generated from Smithy shape ``com.amazonaws.ses#DeleteReceiptFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_filter_name


class DeleteReceiptFilterRequest(TypedDict, closed=True):
    filter_name: "capo_ses.types.receipt_filter_name.ReceiptFilterName"
    """<p>The name of the IP address filter to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteReceiptFilterRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}FilterName", str(value["filter_name"])))


def deserialize_query(el: Element) -> DeleteReceiptFilterRequest:
    out: DeleteReceiptFilterRequest = {}  # type: ignore[typeddict-item]
    child_filter_name = el.find("FilterName")
    if child_filter_name is not None:
        out["filter_name"] = str(child_filter_name.text or "")
    else:
        out["filter_name"] = ""
    return out
