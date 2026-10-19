"""Generated from Smithy shape ``com.amazonaws.ses#ListIdentitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.identity_list
    import capo_ses.types.next_token


class ListIdentitiesResponse(TypedDict, closed=True):
    identities: "capo_ses.types.identity_list.IdentityList"
    """<p>A list of identities.</p>"""
    next_token: NotRequired["capo_ses.types.next_token.NextToken"]
    """<p>The token used for pagination.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListIdentitiesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.identity_list

    capo_ses.types.identity_list.serialize_query(
        value["identities"], pairs, f"{key_prefix}Identities"
    )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> ListIdentitiesResponse:
    out: ListIdentitiesResponse = {}  # type: ignore[typeddict-item]
    child_identities = el.find("Identities")
    if child_identities is not None:
        import capo_ses.types.identity_list

        out["identities"] = capo_ses.types.identity_list.deserialize_query(
            child_identities
        )
    else:
        out["identities"] = []
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
