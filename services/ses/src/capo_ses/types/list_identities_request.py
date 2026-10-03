"""Generated from Smithy shape ``com.amazonaws.ses#ListIdentitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.identity_type
    import capo_ses.types.max_items
    import capo_ses.types.next_token


class ListIdentitiesRequest(TypedDict, closed=True):
    identity_type: NotRequired["capo_ses.types.identity_type.IdentityType"]
    """<p>The type of the identities to list. Possible values are "EmailAddress" and "Domain". If this parameter is omitted, then all identities are listed.</p>"""
    next_token: NotRequired["capo_ses.types.next_token.NextToken"]
    """<p>The token to use for pagination.</p>"""
    max_items: NotRequired["capo_ses.types.max_items.MaxItems"]
    """<p>The maximum number of identities per page. Possible values are 1-1000 inclusive.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListIdentitiesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "identity_type" in value:
        import capo_ses.types.identity_type

        capo_ses.types.identity_type.serialize_query(
            value["identity_type"], pairs, f"{key_prefix}IdentityType"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_items" in value:
        pairs.append((f"{key_prefix}MaxItems", str(value["max_items"])))


def deserialize_query(el: Element) -> ListIdentitiesRequest:
    out: ListIdentitiesRequest = {}  # type: ignore[typeddict-item]
    child_identity_type = el.find("IdentityType")
    if child_identity_type is not None:
        import capo_ses.types.identity_type

        out["identity_type"] = capo_ses.types.identity_type.deserialize_query(
            child_identity_type
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    return out
