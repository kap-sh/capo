"""Generated from Smithy shape ``com.amazonaws.ses#DeleteIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.identity


class DeleteIdentityRequest(TypedDict, closed=True):
    identity: "capo_ses.types.identity.Identity"
    """<p>The identity to be removed from the list of identities for the Amazon Web Services account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteIdentityRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Identity", str(value["identity"])))


def deserialize_query(el: Element) -> DeleteIdentityRequest:
    out: DeleteIdentityRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        out["identity"] = ""
    return out
